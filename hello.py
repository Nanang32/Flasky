from flask import Flask, render_template

from markupsafe import escape
app = Flask(__name__)


# @app.route('/login')
# def test():
#     return render_template('login.html')
# if __name__ == '__main__':
#     app.run()    


@app.route('/login/<loginame>')
def hello(loginame):
    return render_template('login.html',loginame=loginame)