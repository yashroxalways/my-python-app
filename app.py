from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello_world():
    return'Hello, Jenkins!'

if __name__=='__main__':
   app.run(host='0.0.0.0',port=5000)
