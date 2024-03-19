import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# Funkcja do pobierania danych z bazy danych SQLite
def get_data_from_database():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM my_data')  # Zapytanie o wszystkie dane z tabeli
    data = cursor.fetchall()
    connection.close()
    return data

@app.route('/')
def index():
    # Pobierz dane z bazy danych
    data = get_data_from_database()
    # Renderowanie szablonu HTML i przekazanie danych
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

