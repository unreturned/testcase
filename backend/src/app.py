from flask import Flask, request
import psycopg2
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():

    if request.method == 'POST':
        if request.form.get('data') != None:
            data = request.form.get('data')
            conn = psycopg2.connect(host=os.environ['DB_HOST'],
                                    database=os.environ['DB_NAME'],
                                    user=os.environ['DB_USERNAME'],
                                    password=os.environ['DB_PASSWORD'])
            cur = conn.cursor()
            cur.execute('INSERT INTO posts (postdata) VALUES (%s);', (data, ))
            conn.commit()
            cur.close()
            conn.close()
            return '''The data value is: {}'''.format(data)
        else:
            return '''Something went wrong'''

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>data: <input type="text" name="data"></label></div>
               <input type="submit" value="Submit">
           </form>'''

@app.route("/selftest")
def selftest():
    return "OK"

@app.route('/about')
def about():
    return 'Made by Kovalkov Dmitrii kovalkov.dmitriy@gmail.com'