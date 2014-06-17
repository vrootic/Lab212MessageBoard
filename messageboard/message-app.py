from flask import Flask, request, redirect, render_template
import MySQLdb

app = Flask(__name__)
db_config = {
    'host': "",
    'user': "",
    'passwd': "",
    'db': "",
}


def connect_db():
    db = MySQLdb.connect(db_config["host"], db_config["user"],
        db_config["passwd"], db_config["db"], charset='utf8')
    return db

@app.route("/db/version")
def db_version():
    db = MySQLdb.connect(db_config["host"], db_config["user"],
        db_config["passwd"], db_config["db"])
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()

    return "Database version: %s" % data

@app.route("/db/databases")
def db_databases():
    # to do 
    return 'show me dbs'

@app.route("/", methods=['GET'])
def index():
    cursor = connect_db().cursor()
    # to do
    # show me how to display message by other order
    cursor.execute("SELECT * From message")
    data = cursor.fetchall()

    return render_template("index.html", messages=data)

@app.route("/message", methods=['POST'])
def create():
    db = connect_db()
    cursor = db.cursor()
    if request.method == 'POST':
        name = request.form["name"]
        message = request.form["message"]
        if len(name) != 0 and len(message) != 0:
            cursor.execute('INSERT INTO message (name, message_body) \
            VALUES (%s, %s)',
            [name, message])
            db.commit()
            return redirect('/')
        else:
           return redirect('/')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
