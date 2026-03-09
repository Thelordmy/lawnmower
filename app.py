from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    cmd = request.form['cmd']
    print(f"Command received: {cmd}")
    return cmd

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
