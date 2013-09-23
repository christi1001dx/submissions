#!/usr/local/bin/python

from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pvwatts.html', methods=['GET', 'POST'])
def pvwatts():
  if request.method == 'GET':
    abort(404)
  latitude = request.form['lat']
  longitude = request.form['lon']
  return render_template('pvwatts.html',latitude=latitude,longitude=longitude)

if __name__ == '__main__':
  app.run(debug=True)