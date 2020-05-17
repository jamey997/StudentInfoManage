from flask import Flask, redirect, url_for, request, make_response
app = Flask(__name__)


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
#    if request.method == 'POST':
#    user = request.form['nm']
   
   resp = make_response('23333')
   resp.set_cookie('userID', "666")
   
   return resp


if __name__ == '__main__':
   app.run(debug = True)