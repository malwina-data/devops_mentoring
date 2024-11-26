from flask import Flask, render_template, request
import argparse

app = Flask(__name__)

def get_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--db_user', type=str, required=True, help='Database user')
    parser.add_argument('--db_password', type=str, required=True, help='Database password')
    parser.add_argument('--db_name', type=str, required=True, help='Database name')
    parser.add_argument('--db_ip_address', type=str, required=True, help='Database host')
    return parser.parse_args()

@app.route('/')
def index():
    args = get_args()
    return render_template('index.html', 
                           db_user=args.db_user, 
                           db_password=args.db_password, 
                           db_name=args.db_name, 
                           db_ip_address=args.db_ip_address)  # Poprawiona nazwa zmiennej

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
