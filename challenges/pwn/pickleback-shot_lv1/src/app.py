import os
import subprocess
import pickle
import base64
from flask import Flask, request

app = Flask(__name__)

uid = int(subprocess.check_output(["id", "-u", "johndoe"]).decode().strip())
gid = int(subprocess.check_output(["id", "-g", "johndoe"]).decode().strip())

os.setgid(gid)
os.setuid(uid)

@app.route('/get_glass', methods=['GET'])
def get_glass():
	"""
	Go fetch a glass for your pickleback shot!
	
	Hint:
	- https://davidhamann.de/2020/04/05/exploiting-python-pickle/
	"""
	data = base64.urlsafe_b64decode(request.form['data'])
	glass = pickle.loads(data)

	if not isinstance(glass, str):
		return 'You are not allowed to drink with this glass!', 400
	
	return glass, 200

if __name__ == '__main__':
	app.run(host='0.0.0.0')