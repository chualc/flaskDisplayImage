from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    imageList = ['Programming.JPG', 'isSo.JPG', 'Easy.JPG']
    return render_template('home.html', imageList=imageList )


if __name__ == '__main__':
    app.run()
