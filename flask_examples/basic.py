from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>hello Pavan tanniru !</h1>"

@app.route('/answer') # 127.0.0:5000; error # 127.0.0:5000/answer right ...

def info():
    return "</h1> r u programemr ?"

@app.route('/info/<name>')
def your_name(name):
    return "<h2>Welcome {} as guest </h2>".format(name[99])



if __name__ =="__main__":
    app.run(debug=True)
