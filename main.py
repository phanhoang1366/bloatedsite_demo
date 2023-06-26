from flask import Flask, request, session, url_for, redirect, render_template, Response, send_from_directory
import secrets

app = Flask(__name__, template_folder=".")
app.secret_key = secrets.token_bytes()

@app.after_request
def after_request_callback(response: Response):
  print(response.__dict__)
  if response.headers["Content-Type"].startswith("text/html"):
    updated = render_template("template.html", status=response.status_code, message=response.response[0].decode())
    response.set_data(updated)
  return response

@app.errorhandler(404)
def not_found(e):
    return "Not Found", 404
    return render_template("template.html", status=404, message="Not Found"), 404

@app.route("/")
def home():
    return "OK", 200
    return render_template("template.html", status=200, message="OK")

@app.route('/css/<path:filename>')
def css_content(filename):
    return send_from_directory('css', filename)

@app.route("/index.js")
def get_playlist():
    return send_from_directory('.', 'index.js')

@app.route("/undefined")
def empty_response():
    return ('', 204)
@app.route('/audio/<path:filename>')
def serve_music(filename):
    return send_from_directory('audio', filename)
