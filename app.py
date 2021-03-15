# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:58:46 2021

@author: Dell
"""

from flask import Flask, request,jsonify,render_template
import requests
# import json

app=Flask(__name__)

url='https://jsonplaceholder.typicode.com/posts'
data=requests.get(url).json()

@app.route('/result')
def result():
    start_id=request.args.get('start_id')
    end_id=request.args.get('end_id')
    # type_=request.args.get('type_')
    token=request.args.get('token')
    
    d=0
    if token=='1234':
        # with open('posts.json') as g:
                # data=json.load(g)
        # if type_:
            # filename=type_+'.json'
            # with open(filename) as f:
                # data=json.load(f)
        if start_id:
            if isinstance(start_id,str):    
                start_id=int(start_id)
            
        if end_id:    
            if isinstance(end_id,str):
                end_id=int(end_id)
            
            
        if start_id and end_id:
            d=data[start_id:end_id]
        elif isinstance(start_id,int):
            d=data[start_id]
        elif isinstance(end_id,int):
            d=data[end_id]
        if d==0:
            return "Enter the Start and End ID"
        else:
            return jsonify(d)
    else:
        return "Authentication Error"
    return 'nothing to show here'

 

@app.route('/')
def home_page():
    return render_template ('home_page.html')
    
    
'''    return """
    <!doctype html>
    <body>
    <center>
    <style>
    *{
      box-sizing: border-box;
     }
        input[type=text], select, textarea 
        {
          width: 100%;
          padding: 12px;
          border: 1px solid #ccc;
          border-radius: 4px;
          resize: vertical;
         }
    <h3>Enter Details to Get Data</h3>
    <form action="/result">
    <label for ="token">Enter token to authenticate:</label>
    <input type ="text" id="token" name="token"><br>
    <label for ="start_id">Enter Start iD:</label>
    <input type="text" id="start_id" name="start_id"><br>
    <label for ="end_id">Enter End ID:</label>
    <input type="text" id="end_id" name="end_id"><br>
    <label for ="type_"> Select the Type of required data:</label>
    <select name="type_" id="type_">
        <option value="Posts">Posts</option>
        <option value="Comments">comments</option>
        <option value="Albums">Albums</option>
        <option value="Photos">photos</option>
        <option value="Todos">todos</option>
        <option value="Users">users</option>
        </select><br><br>
    <button type="submit">Submit</button>
    </form>
    </center>
    </body>
    </html>
    """
 '''   
if __name__=='__main__':
        app.run(debug=True)
        