from testapp import app


@app.route('/')
def index():
    return "Hello World!"

@app.route('/test')
def other1():
    return "テストページです！"