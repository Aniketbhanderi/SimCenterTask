from flask import Flask, render_template, request, redirect
import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index():
    name = request.form['uname']
    role = request.form['role']
    connection = sqlite3.connect(currentdirectory + "\demo.db")
    cursor =  connection.cursor()
    if(role=="Software Developer"):
        x=1
    elif(role=="Software Manager"):
        x=2
    elif(role=="Data Scientist"):
        x=3
    else:
        x=4

    query1 = "INSERT INTO temp VALUES('{n}','{r}')".format(n=name, r=role)
    cursor.execute("INSERT INTO User (username,role_id) VALUES('{n}','x')".format(n=name))
    cursor.execute("INSERT INTO Role (name) VALUES('{r}')".format(r=role))
    cursor.execute(query1)
    connection.commit()
    return 'Success'


if __name__ == '__main__':
    app.run(debug=True)
