from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://sports_db_test_user:g8aauJvZfEyKIjvreUETtztPSWSSRX83@dpg-cgk8lc0rddleudth6pkg-a.oregon-postgres.render.com/sports_db_test")
    conn.close()
    return 'Database Connection Successful'