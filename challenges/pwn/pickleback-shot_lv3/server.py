import pickle
import base64
import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/get_pickle', methods=['GET'])
def get_pickle():
    def mix(s1: str, s2: str) -> str:
        if len(s1) != len(s2):
            raise ValueError('Invalid input')
        
        result = ""
        for c1, c2 in zip(s1, s2):
            r = 0
            
            for i in range(0, 8):
                bc1 = (ord(c1) >> i) & 1
                bc2 = (ord(c2) >> i) & 1
                
                bc_result = (bc1 == 0 or bc2 == 1) and (bc2 == 0 or bc1 == 1)
                
                r += (bc_result << i)
            
            result += chr(r)
        
        return result
    
    ingredients = ["apple", "mango", "peach", "grape", "lemon", "bread", "steak", "flour", "yeast", "sugar", "olive", "honey", "basil", "beans", "onion", "nutty", "melon", "sauce", "cream"]

    data = base64.urlsafe_b64decode(request.form['data'])
    new_ingredients = pickle.loads(data)

    try:
        random.shuffle(ingredients)
        ingredients += new_ingredients

        preparation = ingredients[0]
        for ingredient in ingredients[1:]:
            preparation = mix(preparation, ingredient)

        if preparation == "flag-":
            return "???", 200
    except:
        pass

    return 'Invalid input', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')