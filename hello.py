from flask import Flask, render_template, request,redirect, url_for

from markupsafe import escape
app = Flask(__name__)


# @app.route('/login')
# def test():
#     return render_template('login.html')
# if __name__ == '__main__':
#     app.run()    


# @app.route('/login/<loginame>')
# def hello(loginame):
#     return render_template('login.html',loginame=loginame)


# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         return ' testing panggil halaman post' + request.form['username']
#     else:  
#         return render_template('login.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        return ' testing panggil halaman post  ' + request.form['username']+ '\n' + request.form['password']

    return render_template('login.html', error=error)