#!/usr/bin/python

import emotiscrape
import flask
import json
import os
#import logging
import sys


app = flask.Flask(__name__)
#logging.basicConfig(stream=sys.stderr)

@app.route("/")
def index():
	return flask.send_from_directory("./html", "index.html")

@app.route("/search/", methods=["GET"])
def doSearch():
	q = flask.request.args["q"]
	emo = emotiscrape.Emotiscrape()
	result = emo.analyze_string(q)
	return json.dumps(result)


@app.route("/<path:filename>")
def passThrough(filename):
	return flask.send_from_directory("./html", filename);


if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	#app.run(host='127.0.0.1', port=port)
	app.run(host='0.0.0.0', port=port, debug=True)
