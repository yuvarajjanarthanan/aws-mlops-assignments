#Import Libraries
from flask import Flask,render_template,request
import boto3

app = Flask(__name__)

#index page where folder is to be specified
@app.route('/get-files')
def form():
    return render_template('index.html')
 
@app.route('/list-files/', methods = ['POST', 'GET'])
def data():
    
    #to avoid direct connection to list-files URL
    if request.method == 'GET':
        return f"The URL /list-files is accessed directly. Try going to '/get-files' to see the files"
    
    #get the files from the bucket prefix
    if request.method == 'POST':
        
        #folder specified in get-files page
        folder = request.form['folder']
        
        #connect to s3 and get files
        s3_client = boto3.client('s3')
        response = s3_client.list_objects(Bucket = "tiger-mlops-training",    #bucket
                                          Prefix = "home/yuvaraj.janartha/mlops-training/"+folder)    #prefix where the folders reside
        
        #parse response to get file names
        files = [file["Key"].replace("home/yuvaraj.janartha/mlops-training/"+folder+"/","") for file in response["Contents"]]
        
        #return list of files in folder to be displayed
        return render_template('files.html',files = files)
 
 
app.run(host='0.0.0.0', port=8085, debug=True)