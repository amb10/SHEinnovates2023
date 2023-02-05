from flask import Flask, render_template
import os

app = Flask(__name__)

picFolder = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def index():
    banner = os.path.join(app.config['UPLOAD_FOLDER'], 'banner.jpeg')
    return render_template('index.html', user_image = banner)

@app.route("/index")
def index1():
    return "hello"
    
if __name__ == '__main__':
    app.run(debug=True)
