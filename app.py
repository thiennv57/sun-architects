from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Response
import os

app = Flask(__name__)

# src = '''@app.route("/")
# def index():
#    return render_template("index.html", src = src)

# if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=5000 )'''

@app.route("/")
def index():
   return render_template("index.html")


@app.route("/robots.txt")
def robots_dot_txt():
   r = Response(response="User-Agent: *\nDisallow: /\n", status=200, mimetype="text/plain")
   r.headers["Content-Type"] = "text/plain; charset=utf-8"
   return r

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
