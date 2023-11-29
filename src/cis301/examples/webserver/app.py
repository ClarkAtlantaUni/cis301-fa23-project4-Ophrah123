#what we need to use flask(library modile python based web server
# (understands http)(need to know high level version/general idea about hot it works))
#setup.py already has line 11: look for the flask in general
import csv
import json

from flask import Flask, render_template, request, session

from cis301.project4.phonecall import PhoneCall

app = Flask(__name__)#path to the correct directory/instantiate first flask application
#routing to handle the url
app.secret_key="14Xw76JMtsbcFI9fKXLE"
@app.route("/")#hey application if the user is asking for the route of the website
def homepage():
    return "Welcome to CIS301!"
@app.route("/cis301")
def cis301_page():
    return ("<h1>This is so much fun!</h1>")

@app.route("/homepage")
def cis301_homepage():
    return render_template(calc.html)
    #instead of having multiple webpages, we use python to pull
    # data from the database and restructure it so the page is generated according to the user
@app.route("/sample_phonecall")
def get_sample_phonecall():
    phonecall = PhoneCall("404-123-1234","404-657-1234","11/15/2023 15:02","11/15/2023 15:04")
    return "<ul><li>"+str(phonecall)+"</ul></li>"

@app.route("/calc", methods=["GET", "POST"])#diff
def calc():
    if request.method=="GET":
        x = request.args.get("x")
        y = request.args.get("y")
        op = request.args.get("op")
        if not(x and y and op):
            return "Bad input: Try again."
        result = None
        x = int(x)
        y = int(y)
        if op == 'add':
            return f"{x} + {y} = {(x+y)}"
        elif op =='sub':
            return f"{x} - {y} = {(x - y)}"
        elif op =='mul':
            return f"{x} * {y} = {(x * y)}"
        elif op =='divide':
            if y>0:
                return f"{x} / {y} = {(x / y)}"
            else:
                return "Divide by 0 error."
        else:
            return "Operation not supported!"

    elif request.method == "POST":
        x = request.form.get("x")
        y = request.form.get("y")
        op = request.form.get("op")
        #if not()


        #print(x)
        #return "You entered:"+x
        #HW:complete calculator for monday/complete parsing piece on client side
        #?-typical gitrequest notation that opens the request to ask for values that are seperated by && values



@app.route("/auth", methods=["POST"])
def authenticate():
    if request.method != "POST":
        return "Operation not supported!"

    data = request.json
    user = data['username']
    passwd = data['password']
    if str(user).lower()=='admin' and str(passwd)=="fall2023":
        session["uid"] = 1
        session["uname"] = user
        return '{"res":"success"}'
    else:
        return '{"res":"Authentication failed"}'
@app.route("/search", methodds=["GET"])
def search_by_name():
    search_query = request.args.get("name")
    if not search_query:
        return '{"res":"did not find a valid search keyword"}'
    if session["uid"] and session["uname"]:
            #open the file/search by first name & return matches
        result=[]
        with open("employee_data.csv","r") as csvdata_file:
            reader = csv.reader(csvdata_file)
            for row in reader:
                if search_query.lower() in row["FIRST_NAME"].LOWER():
                    result.append({"name":f"{row['FIRST_NAME']} {row['LAST_NAME']}", "phone": f"{row['PHONE_NUMBER']}"})

        return json.dumps(result)
    else:
        return '{"res":"Authentication failed"}'

if __name__ == '__main__':
    app.run()
    #needed for authentication"

















