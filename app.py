from flask import Flask, render_template
import os
import time
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


##Anything of modeling 

RED = "100"
GREEN = "010"
BLUE  = "001"
OFF = "000"

def writeColour(colour):
	led = open("/dev/ledborg","w")
	led.write(colour)
	led.close()

def flash(colour):
	writeColour(colour)
	time.sleep(0.5)
	writeColour(OFF)


@app.route("/", methods=['GET'])
def home():
	flash(GREEN)
	return render_template('index.jade')	

@app.route("/list", methods=['GET'])
def listPictures():
	listPic = []
	for filenames in os.walk('/static/img/cam'):
		for filename in filenames:
			listPic.append('<img src=/static/img/cam/' + filename)

	return render_template('listPictures.jade', listPic=listPic)

@app.route("/current",methods=['GET'])
def current():
	return render_template('current.jade')


if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")
