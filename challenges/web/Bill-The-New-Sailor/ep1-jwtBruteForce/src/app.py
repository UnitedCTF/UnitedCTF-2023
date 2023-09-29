from flask import Flask, jsonify, make_response, redirect, render_template, request, url_for
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, set_access_cookies, get_jwt

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from database_control import get_user_by_username, register_user

app = Flask(__name__)

app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_CSRF_PROTECT"] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config['JWT_SECRET_KEY'] = 'monkeypirate'

jwt = JWTManager(app)


# Handle unauthorized access and expired token
@jwt.unauthorized_loader
def unauthorized_callback(error):
    print(error)
    return redirect('/login')  # Redirect to the login page


@jwt.expired_token_loader
def expired_callback(error1, error2):
    print(error1, error2)
    return redirect('/login')  # Redirect to the login page


# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response


# Login route
@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = get_user_by_username(username)

        if user and user['password'] == password:
            access_token = create_access_token(identity=username, additional_claims={'role': user['role']})
            response = make_response(redirect('/'))
            response.set_cookie('access_token_cookie', access_token)
            response.set_cookie('role', user['role'])

            return response
        
        else:
            return jsonify(message="Invalid credentials"), 401
    
    else:
        return render_template("login.html")


# Logout route
@app.route("/logout")
def logout():
    # Create a response object
    response = make_response(redirect(url_for('login')))

    # Clear the access token and user name cookies
    if request.cookies.get('access_token_cookie'):
        response.delete_cookie('access_token_cookie')
    
    if request.cookies.get('role'):
        response.delete_cookie('role')

    return response


@app.route('/')
@jwt_required()
def index():
    user = get_jwt_identity()
    return render_template('index.html', user=user)


@app.route('/hold')
@jwt_required()
def hold():
    role = get_jwt().get('role')
    return render_template('hold.html', role=role)


if __name__ == '__main__':
    register_user("cook.bill@tortuga.pirate", "SIXUndi/5Xs2$31#", "Cook")
    app.run(host="0.0.0.0", debug=False)
