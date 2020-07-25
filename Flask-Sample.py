from flask import Flask

app=Flask(__name__)

@app.route('/')
def method1():
  return "Hello Karan"

app.run(port=8000)


