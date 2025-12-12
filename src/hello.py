from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!!"

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes')
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
