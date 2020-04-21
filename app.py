import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#connecting to the database
connection = sqlite3.connect("todo.db")

#cursor
crsr = connection.cursor()

#SQL command to create a table in the database
sql = """CREATE TABLE IF NOT EXISTS Todo(
PID INTEGER PRIMARY KEY AUTOINCREMENT,
text VARCHAR(200),
complete BOOLEAN)"""

crsr.execute(sql)




@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/add', methods=['POST'])
def add():
    #todo = Todo(text=request.form['todoitem'], complete=False)
    get_new_todo = request.form['todoitem']
    sql =  "INSERT INTO Todo (text, complete) VALUES (get_new_todo, False)
    crsr.execute(sql)
    crsr.commit()
    return redirect(url_for('index'))







connection.close()
if __name__ == '__main__':
    app.run(debug = True)
