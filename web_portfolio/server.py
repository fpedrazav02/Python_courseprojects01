
from email import message
from operator import mod
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def ft_mainweb():
    return render_template('index.html')

@app.route("/<string:page_name>")
def ft_index(page_name):
    return render_template(page_name)

def ft_transferdata_F(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}\n{subject}\n{message}\n')

def ft_transferdata_C(data):
    with open('database.csv',newline="", mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write = csv.writer(database2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

@app.route("/ft_submit", methods = ['POST', 'GET'])
def ft_submit():
    if request.method == 'POST':
        data = request.form.to_dict()
    ft_transferdata_C(data)
    ft_transferdata_F(data)
    return redirect('ty.html')