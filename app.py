from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def encode_text(text):
    words = text.split()
    encoded_words = []
    for word in words:
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        random_chars1 = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        if len(word) <= 3:
            encoded_words.append(word[::-1])
        else:
            encoded = random_chars + word[1:] + word[0] + random_chars1
            encoded_words.append(encoded)
    return ' '.join(encoded_words)

def decode_text(text):
    words = text.split()
    decoded_words = []
    for word in words:
        if len(word) <= 3:
            decoded_words.append(word[::-1])
        else:
            terminated = word[3:-4]
            decoded = word[-4] + terminated
            decoded_words.append(decoded)
    return ' '.join(decoded_words)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        mode = request.form['mode']
        if mode == 'encode':
            result = encode_text(text)
        else:
            result = decode_text(text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
