from flask import Flask, render_template, request,make_response,redirect, url_for
import sqlite3
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


@app.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    db = sqlite3.connect('users.sqlite')
    cursor = db.cursor()
    if request.method == 'POST':
        acusername = request.form['username']
        acpassword = request.form['password']
        acemail = request.form['email']

        cursor.execute('INSERT INTO akun(username,password,email) VALUES (?,?,?)', (acusername, acpassword,acemail))
        db.commit()
    return render_template('login.html', error=error)

@app.route('/getcookie')
def getCookie():
    email = request.cookies.get('email_user')
    return  'email yang tersimpan di Cookie adalah' + email


@app.route('/')
def sendb():
    db = sqlite3.connect('users.sqlite')
    cursor = db.cursor()

    # if request.method == 'POST':
    #     nmphone = request.form['namephone']
    #     phnumber = request.form['phonenumber']
    #
    #     cursor.execute('INSERT INTO pbook(namephone,phonenumber) VALUES (?,?)', (nmphone, phnumber))
    #     db.commit()
    # cursor.execute('INSERT INTO pbook(namephone,phonenumber) VALUES ("kot","443")')
    # db.commit()

    cursor.execute('SELECT * FROM akun')
    data = cursor.fetchall()
    return  str(data)
