from secure import cnxpool
from flask import Flask, render_template
import sys
import logging


cnx = cnxpool.get_connection()
db = cnx.cursor(dictionary=True)
app = Flask(__name__)


@app.route("/")
def home():
    db.execute('select * from pc_info')
    pc_info = list(db.fetchall())
    cnx.commit()
    return render_template('index.html', pc_info=pc_info)


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    from flask import send_from_directory

    @app.route('/static/<path:path>')
    def send_static(path):
        return send_from_directory('static', path)

    @app.route('/bootstrap/<path:path>')
    def send_bootstrap(path):
        return send_from_directory('static/bootstrap', path)

    @app.route('/font-awesome/<path:path>')
    def send_font_awesome(path):
        return send_from_directory('static/font-awesome', path)

    @app.route('/leaflet/<path:path>')
    def send_leaflet(path):
        return send_from_directory('static/leaflet', path)

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

    #db.close()
    #cnx.close()
else:
    logging.basicConfig(stream=sys.stderr)
