from flask import Flask, render_template
import time
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


##Anything of modeling 

RED = "100"
GREEN = "010"
BLUE  = "001"
OFF = "000"

def writeColour(colour):
	led = ("/dev/ledborg","w")
	led.write(colour)
	led.close()

def flash(colour):
	writeColour(colour)
	time.sleep(0.5)
	writeColour(OFF)


@app.route("/", methods=['GET'])
def home():
	writeColour(BLUE)
	return render_template('index.jade')	


if __name__ == "__main__":
	app.run(debug=True)