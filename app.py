from flask import Flask, render_template
import glob
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

@app.route("/list/", methods=['GET'])
def listPictures():
	list = glob.glob("static/img/cam/*.jpg")
	listPic = []
	for file in list:
		listPic.append("<img src='/" + file + "'>")
	flash(BLUE)
	return render_template('listPictures.jade', listPic=listPic)

@app.route("/current/",methods=['GET'])
def current():
	flash(RED)
	return render_template('current.jade')


if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")
