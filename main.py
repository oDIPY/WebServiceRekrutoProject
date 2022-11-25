from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_tasks():
    name = request.args.get('name')
    message = request.args.get('message')

    if name is None or message is None:
        return "Не переданы нужные аргументы!"

    return f"{name}! {message}!"


if __name__ == '__main__':
    app.run()

