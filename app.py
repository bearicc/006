import mysql.connector
from flask import Flask, render_template

conn = mysql.connector.connect(user='root', password='2015', host='localhost', database='bearicc')
db = conn.cursor(dictionary=True)
app = Flask(__name__)


@app.route("/")
def home():
    db.execute('select * from pc_info')
    pc_info = list(db.fetchall())
    conn.commit()
    return render_template('index.html', pc_info=pc_info)

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

    db.close()
    conn.close()
