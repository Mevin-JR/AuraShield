from flask import Flask, request, render_template, jsonify, abort
from database import check_brand, check_product, check_brand_prodcut, check_toxins
from model import predict
import os

app = Flask(__name__)

def get_file_path():
    app_directory = os.path.dirname(os.path.abspath(__file__))
    return app_directory

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/database')
def database():
    return render_template('page2.html')

@app.route('/team')
def team():
    return  render_template('team.html')

@app.route('/short-text', methods=['POST'])
def shortText():
    product = request.form.get('productName')

    if product == "":
        abort(404)
    row = check_product(product)
    if row is None:
        row = check_brand(product)
        if row is None:
            abort(404)
    column_names = ['id', 'brand', 'product_name', 'ingredients', 'skin_type']
    data_dict = dict(zip(column_names, row))
    toxins = check_toxins(data_dict.get("ingredients"))
    data_dict['toxins'] = toxins

    return jsonify(data_dict)

@app.route('/text-input', methods=['POST'])
def textInput():
    brand = request.form.get('brand')
    product = request.form.get('productName')
    ingredients = request.form.get('ingredients')

    if brand == "" and product != "":
        row = check_product(product)
    elif brand != "" and product == "":
        row = check_brand(brand)
    elif brand == "" and product == "":
        abort(404)
    else:
        row = check_brand_prodcut(brand, product)

    if row is None:
        abort(404)
    column_names = ['id', 'brand', 'product_name', 'ingredients', 'skin_type']
    data_dict = dict(zip(column_names, row))
    toxins = check_toxins(ingredients)
    data_dict['toxins'] = toxins
    return jsonify(data_dict)

@app.route('/ing-input', methods=['POST'])
def ingInput():
    ingredient = request.form.get('ingredient')
    if ingredient == "":
        abort(404)
    
    if ',' in ingredient:
        toxins = check_toxins(ingredient)
        return jsonify({"result": "list", "toxins": toxins})
    else:
        result = predict(ingredient)
        if result == "Harmful":
            return jsonify({"result": "string", "ingredient": ingredient, "isToxic": 1})
        elif result == "Not Harmful":
            return jsonify({"result": "string", "ingredient": ingredient, "isToxic": 0})
        else:
            return jsonify({"result": "string", "ingredient": ingredient, "isToxic": -1})

if __name__=='__main__':
   app.run(host='0.0.0.0')