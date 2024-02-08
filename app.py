from flask import Flask, render_template, request
import requests

app = Flask(__name__)
print("Hello World: ", __name__)


@app.route('/')
def hello():
    ip = request.remote_addr
    print("request: ", dir(request))
    if ip == '127.0.0.1' or ip == 'localhost':
        city = 'Home'
    else:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()

        if 'city' in data:
            city = data['city']
        else:
            city = 'Unknown'
    return render_template('index.html', city=city)

@app.route('/hello/<name>')
def hello2(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)