from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

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

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    audio_file = request.files['audio_data'].read()
    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(audio_file, 16000, 2)

    try:
        text = recognizer.recognize_google(audio_data)
        messages.append(text)
        return jsonify({'message': text})
    except:
        return jsonify({'error': 'Could not recognize the audio.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
