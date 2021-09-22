from flask import Flask, render_template, request,make_response,redirect, url_for

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
        users = request.form['username']
        pwd = request.form['password']
        respo = make_response(' testing panggil halaman post  ' + users + '\n' + pwd)
        respo.set_cookie('email_user',users)
        return respo
    return render_template('login.html', error=error)

@app.route('/getcookie')
def getCookie():
    email = request.cookies.get('email_user')
    return  'email yang tersimpan di Cookie adalah' + email


@app.route('/handle-data', methods=['POST'])
def sendb():
    db = sqlite3.connect('phonebook.sqlite')
    cursor = db.cursor()

    if request.method == 'POST':
        nmphone = request.form['namephone']
        phnumber = request.form['phonenumber']

        cursor.execute('INSERT INTO pbook(namephone,phonenumber) VALUES (?,?)', (nmphone, phnumber))
        db.commit()
    # cursor.execute('INSERT INTO pbook(namephone,phonenumber) VALUES ("kot","443")')
    # db.commit()

    # cursor.execute('SELECT * FROM pbook')
    # data = cursor.fetchall()

    # return  str(data)