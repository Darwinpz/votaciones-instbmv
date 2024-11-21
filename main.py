from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='')
app.secret_key = os.getenv("KEY")

if __name__ == '__main__':
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)