from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Halo! Aplikasi web Python sudah berjalan di Docker."

if __name__ == '__main__':
    # Host WAJIB 0.0.0.0 agar bisa diakses dari luar container Docker
    # Port disesuaikan dengan target port di docker-compose (5000)
    app.run(host='0.0.0.0', port=5000, debug=True)