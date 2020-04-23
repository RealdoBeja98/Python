from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

#create a database sqlite3
conn = sqlite3.connect('todo.db', check_same_thread = False)
#create the cursor for the database
cursor = conn.cursor()

#create the tabble
sql = """CREATE TABLE  IF NOT EXISTS Task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content VARCHAR,
    done BOOLEAN
)"""

cursor.execute(sql)

@app.route('/')
def tasks_list():
    sql = 'SELECT * FROM Task'
    cursor.execute(sql)
    rows = cursor.fetchall() #has all information of the table Task
    return render_template('index.html', rows = rows)

@app.route('/task', methods = ['POST'])
def add_task():
    content_of_task = request.form['content']
    if not content_of_task:
        return redirect()
    #add in the database the content
    sql = "INSERT INTO Task (content, done) VALUES ('{}', False)".format(content_of_task)
    cursor.execute(sql)
    conn.commit()
    return redirect('/')




if __name__ == '__main__':
    app.run(debug = True)

conn.close()