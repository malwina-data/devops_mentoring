import json
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Wczytanie konfiguracji z pliku JSON
with open('/home/ec2-user/myproject/config.json') as config_file:
    app.config.update(json.load(config_file))

def get_data_from_database():
    try:
        connection = psycopg2.connect(
            dbname=app.config['DB_NAME'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASSWORD'],
            host=app.config['DB_IP_ADDRESS']
        )
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM netflix_titles')
        data = cursor.fetchall()
        connection.close()
        return data
    except Exception as e:
        app.logger.error(f"Error connecting to the database: {e}")
        return []

@app.route('/')
def index():
    data = get_data_from_database()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
