# -*- coding:utf-8 -*-

from flask import Flask, redirect, url_for, request, make_response
import json
app = Flask(__name__)

# 注册接口
@app.route('/signup', methods = ['POST'])
def signup():
   # account = request.form['account']
   # password = request.form['password']
   # name = request.form['name']
   # if request.method=='POST':
   #    print(request.get_data())

   user = request.get_data()
   print(user)
   return "2333"

   

# 注册登录接口
@app.route('/signin', methods = ['POST'])
def signin():
   account = request.form['account']
   password = request.form['password']

   return redirect(url_for('success',name = user))

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       print(request)
#       return redirect(url_for('success',name = user))


if __name__ == '__main__':
   app.run(debug = True)
