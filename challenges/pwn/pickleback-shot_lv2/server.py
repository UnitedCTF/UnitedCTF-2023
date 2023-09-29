import pickle
import base64
from flask import Flask, request
from typing import Tuple

app = Flask(__name__)

class Movement:
    def __init__(self, move: str):
        self.__move = move
    
    def __reduce__(self) -> Tuple:
        return (self.__class__, (self.__move,))
    
    def move(self) -> str:
        return self.__move
    
class Movements:
    def __init__(self, movements: list):
        self.__movements = movements
    
    def __reduce__(self) -> Tuple:
        return (self.__class__, (self.__movements,))
        
    def movements(self) -> list:
        return self.__movements

@app.route('/get_whisky', methods=['GET'])
def get_whisky():
    """
    Challenge 2:
    You need to unlock the padlock to get the whiskey.
    """

    data = base64.urlsafe_b64decode(request.form['data'])
    padlock = ['a', 'b', 'b', 'a', 'T', 'n']
    padlaock_pos = 0

    result = pickle.loads(data)

    if not isinstance(result, Movements):
        return 'Invalid input', 400
    
    for movement in result.movements():
        if not isinstance(movement, Movement):
            return 'Invalid input', 400
        
        if movement.move() == 'STOP':
            break

        if movement.move() == "UP":
            padlock[padlaock_pos] = chr(ord(padlock[padlaock_pos]) + 1)

        if movement.move() == "DOWN":
            padlock[padlaock_pos] = chr(ord(padlock[padlaock_pos]) - 1)

        if movement.move() == "RIGHT":
            padlaock_pos += 1

    if "".join(padlock) == 'kraken':
        return 'flag-****', 200
    
    return 'Invalid input', 400

if __name__ == '__main__':
	app.run(host='0.0.0.0')