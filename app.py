from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rado/')
def radio():
    return render_template('radio.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/single/')
def single():
    return render_template('single.html')


@app.route('/404/')
def error():
    return render_template('404.html')


@app.route('/typography/')
def typography():
    return render_template('typography.html')


@app.route('/browse/')
def browse():
    return render_template('browse.html')


if __name__ == '__main__':
    app.run(debug=True)
    
