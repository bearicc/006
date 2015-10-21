from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    from flask import send_from_directory

    @app.route('/css/<path:path>')
    def send_css(path):
        return send_from_directory('static/css', path)

    @app.route('/js/<path:path>')
    def send_js(path):
        return send_from_directory('static/js', path)

    @app.route('/js/vendor/<path:path>')
    def send_js_vendor(path):
        return send_from_directory('static/js/vendor', path)

    @app.route('/img/<path:path>')
    def send_img(path):
        return send_from_directory('static/img', path)

    @app.route('/doc/<path:path>')
    def send_doc(path):
        return send_from_directory('static/doc', path)

    app.run(host='localhost', port=8080, debug=True)
