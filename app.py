from flask import Flask, render_template, request, jsonify
import motors

app = Flask(__name__)
motors.setup()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    cmd = request.form['cmd']

    if cmd == 'forward':
        motors.forward()
    elif cmd == 'backward':
        motors.backward()
    elif cmd == 'left':
        motors.turn_left()
    elif cmd == 'right':
        motors.turn_right()
    elif cmd == 'stop':
        motors.stop()
    elif cmd == 'spray_on':
        motors.spray_on()
    elif cmd == 'spray_off':
        motors.spray_off()
    elif cmd == 'mower_on':
        motors.mower_on()
    elif cmd == 'mower_off':
        motors.mower_off()
    elif cmd == 'auto_on':
        motors.auto_on()
    elif cmd == 'auto_off':
        motors.auto_off()
    elif cmd == 'override_on':
        motors.override_on()
    elif cmd == 'override_off':
        motors.override_off()

    print(f"Command received: {cmd}")
    return cmd

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
