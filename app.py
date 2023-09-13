from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sarvesh98#",
    database="todolist"
)

@app.route('/')
def index():
    # Fetch tasks from the database
    cursor = db.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    cursor.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task']
        cursor = db.cursor()
        cursor.execute('INSERT INTO tasks (task_name) VALUES (%s)', (task_name,))
        db.commit()
        cursor.close()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    cursor = db.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
