from flask import Flask, render_template

from markupsafe import escape
app = Flask(__name__)


# @app.route('/login')
# def test():
#     return render_template('login.html')
# if __name__ == '__main__':
#     app.run()    


@app.route('/login')
def hello(name=None):
    return render_template('login.html', name=name)