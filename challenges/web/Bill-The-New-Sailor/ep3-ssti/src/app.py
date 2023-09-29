from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pirates.html')

@app.route('/crew/<id>')
def crew_member(id):
    return render_template('/crew/' + id + '.html')


@app.route('/secretBetaApp', methods=['GET', 'POST'])
def secretBetaApp():
    page = '''
{% extends 'layout.html' %}

{% block title %}Captain's Secret Beta App - My App{% endblock %}

{% block content %}
<h1>Looks like you found something the captain didn’t want you to find.. His parrot that repeats everything you say!</h1>
<form method="post" action="/secretBetaApp">
<input type="text" name="text" placeholder="Enter text" style="width:50%;height:25px;margin:10px">
<button type="submit">Send</button>
</form>
<div class="ascii-art">
<img src="/static/parrot.jpg">
</div>
<div class="ascii-art">
    '''

    # Vulnerable block
    if request.method == 'POST':
        target = f"<h1>{request.form.get('text')}</h1>"
        page = page + target + "{% endblock %}"

    else : 
        target = "<h1>Yahoy Mates!</h1>"
        page = page + target + "{% endblock %}"

    return render_template_string(page)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)




