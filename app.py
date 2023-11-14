from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='wjddbwjd72',
        database='biztime'
    )

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
