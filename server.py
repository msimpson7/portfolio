import os
import csv
from flask import Flask, render_template, send_from_directory, request, redirect

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('./database.txt', mode='a', encoding='utf-8') as data_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        data_file.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('./database.csv', mode='a', encoding='utf-8', newline='') as data_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong. Try again'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'pikachu.ico')
