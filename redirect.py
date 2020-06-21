from flask import Flask, redirect
 
 
app = Flask(__name__)
 
 
@app.route("/index.html")
@app.route("/")
def go_to_external_url():
    return redirect('http://google.com')
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
