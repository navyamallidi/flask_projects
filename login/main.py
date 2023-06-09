from flask import Flask, request, render_template
import pickle

app =  Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("login.html")
database={'navya':'123','james':'145','krishna':'123'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html',info='invalid user')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='invalid password')
        else:
            return render_template('home.html',name=name1)


if __name__ == '__main__':
    app.run()
