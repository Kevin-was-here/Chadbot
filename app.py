from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send_message():
    user_message = request.form.get('message')
    if user_message:
        messages.append(user_message)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
