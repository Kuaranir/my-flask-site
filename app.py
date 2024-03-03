from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('404page.html'), 404


@app.route('/go')
def go():
    return render_template('404page.html')


if __name__ == '__main__':
    app.run(debug=False)
