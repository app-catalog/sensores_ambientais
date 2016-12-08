import flask
import serial
from time import sleep
import datetime

app = flask.Flask(__name__)
app.debug = True

def event_barcodecliente():
    teste = open('teste.txt', 'wb')
    while True:
	leitura = serial.Serial('/dev/ttyACM0',9600).readline() + '\n\n'
	teste.write(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") + " - " + leitura)
        yield serial.Serial('/dev/ttyACM0',9600).readline() + '\n\n'
	sleep(1)


@app.route('/barcodecliente')
def barcodecliente():
    newresponse = flask.Response(event_barcodecliente(), mimetype="text/event-stream")
    newresponse.headers.add('Access-Control-Allow-Origin', '*')
    newresponse.headers.add('Cache-Control', 'no-cache')
    return newresponse

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
