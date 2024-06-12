import sqlite3
from model import predict
import os

def check_brand(brand):
    from main import get_file_path
    conn = sqlite3.connect(os.path.join(get_file_path(), 'AuraShieldDB.db'))
    cursor = conn.cursor()
    brand = '%' + brand + '%'
    cursor.execute("SELECT * FROM soap WHERE brand LIKE ?", (brand,))
    row = cursor.fetchone()
    conn.close()
    return row

def check_product(product):
    from main import get_file_path
    conn = sqlite3.connect(os.path.join(get_file_path(), 'AuraShieldDB.db'))
    cursor = conn.cursor()
    product = '%' + product + '%'
    cursor.execute("SELECT * FROM soap WHERE product_name LIKE ?", (product,))
    row = cursor.fetchone()
    conn.close()
    return row

def check_brand_prodcut(brand, product):
    from main import get_file_path
    conn = sqlite3.connect(os.path.join(get_file_path(), 'AuraShieldDB.db'))
    cursor = conn.cursor()
    brand = '%' + brand + '%'
    product = '%' + product + '%'
    cursor.execute("SELECT * FROM soap WHERE brand LIKE ? AND product_name LIKE ?", (brand, product,))
    row = cursor.fetchone()
    conn.close()
    return row

def check_toxins(ingredients):
    ing_list = ingredients.split(",")
    check_list = []
    for item in ing_list:
        if predict(item) == "Harmful" or "Not Harmful":
            check_list.append(predict(item))
    return check_list.count("Harmful")