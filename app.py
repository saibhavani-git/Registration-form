
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/submit', methods=['POST'])
def submit():
    registration = {
        'name': request.form.get('name', '').strip(),
        'email': request.form.get('email', '').strip(),
        'event': request.form.get('event', '').strip()
    }

    if not registration['name'] or not registration['email'] or not registration['event']:
        return render_template('registration.html', error='Please complete all required fields.'), 400

    return render_template('success.html', **registration)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
