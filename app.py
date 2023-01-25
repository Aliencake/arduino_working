from flask import Flask, request

app = Flask(__name__)


@app.route('/ip')
def hello():
    ip_addr = request.remote_addr
    print(ip_addr)
    return f'<h1> Your IP address is: {ip_addr}'


@app.route('/')
def index():
    return 'Index Page'


if __name__ == '__main__':
    app.run(debug=True)
