import subprocess
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activate-assistant')
def activate_assistant():
    try:
        # Use subprocess to call main.py
        subprocess.run(['python', 'main.py'], check=True)
        return jsonify({'status': 'success', 'message': 'Assistant activated'})
    except subprocess.CalledProcessError as e:
        # Handle errors if main.py fails
        return jsonify({'status': 'error', 'message': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
