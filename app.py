from flask import Flask,render_template,request
import boto3
import pymysql
import os
import socket

app = Flask(__name__)


def insert_records():
    """
    Function to interact with the DB
    
    Inserts a record with a timestamp into the RDS database

    Parameters
    ----------
    None

    Returns
    -------
    Number of records in the database
    """
    #Information and credentials for the database
    ENDPOINT="yuvaraj-mlops-db-instance.ctimzeuxnbbb.us-east-1.rds.amazonaws.com"
    PORT=3306
    USER="admin"
    passwd='CentauR2'
    DBNAME="yuvaraj_mlops_db"

    #connector to connect to the database
    conn =  pymysql.connect(host=ENDPOINT, user=USER, passwd=passwd, port=PORT, database=DBNAME)
    cur = conn.cursor()
    #insert record into the database
    cur.execute("""INSERT INTO logs VALUES(now())""")
    conn.commit()
    #fetch number of records currently in the database
    cur.execute("""SELECT COUNT(*) FROM logs""")
    num_records = cur.fetchall()

    return num_records[0][0]


 
#html page to interact with the database
@app.route('/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        ip = socket.gethostname()
        return render_template('index.html', text='Inserting records through '+ip+' .Click to insert record')
    if request.method == 'POST':
        num_records = insert_records()
        return render_template('index.html', text='Number of records : '+str(num_records))
 
 
app.run(host='0.0.0.0', port=80)       
