from flask import Flask, jsonify, send_file
import random
import os
from os import path

app = Flask(__name__)

# Assume we have a directory called 'dishes' with images of dishes
DISHES_DIR = 'dishes'

@app.route('/random-dish', methods=['GET'])
def random_dish():
    try:
        path = './dishes'
        os.mkdir(path)
        pass
        files = os.listdir(r"C:\Users\maneck.khanna\im")
        images = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        random_image = random.choice(images)
        random_image_path = send_file(r"C:\Users\maneck.khanna\im", random_image)
        print(f"This is a dish:")
        return random_image_path
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)