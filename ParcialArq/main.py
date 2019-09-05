from flask import Flask, render_template
import csv

app= Flask(__name__)



def comments():
    with open('09052019.csv') as inFile: 
      reader = csv.reader(inFile)
      for row in reader:
        print(row)

@app.route("/")
def index():
  return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)

