import os
import sqlite3
import uuid
from hashlib import md5

db_location = None
def select_phonecalls_by_ownerid(uid):
    with sqlite3.connect(db_location) as conn:
        cur = conn.cursor()
        sql_query = "select "\
                    " u.name, u.email, phonecalls.id, phonecalls.caller, phonecalls.callee,"\
                    " phonecalls.startdate, phonecalls.enddate " \
                    " from phonecalls" \
                    " join phonebills on phonecalls.id = phonebills.pid " \
                    " join users u on phonebills.uid = u.id " \
                    " where u.id = ?" #we're using double quotes because the user type is tsring
        print(sql_query, (uid,))
        cur.execute(sql_query, (uid,))
        return cur.fetchall()

def select_phonecalls():
    with sqlite3.connect(db_location) as conn:
        cur = conn.cursor()
        sql_query = "select "\
                    " phonecalls.id, phonecalls.caller, phonecalls.callee,"\
                    " phonecalls.startdate, phonecalls.enddate " \
                    " from phonecalls"
        print(sql_query)
        cur.execute(sql_query)
        return cur.fetchall()
def register_new_user(name,email,password):
    uid = str(uuid.uuid4())
    password_md5 = str(md5(password.encode()).digest())
    #digest has the bit code representtaion//sqlite cannot store bit code must convert to string
    data = (uid,name,email,password_md5)
    insert_query = 'INSERT INTO users(id, name, email,password) VALUES (?,?,?,?)'

    with sqlite3.connect(db_location) as conn:
        cur = conn.cursor()
        cur.execute(insert_query, data)
        conn.commit()
    return uid


def test_db():
    name = input("Name:")
    email = input("Email:")
    password = input("Password:")
    uid = register_new_user(name, email, password)
    #uid=""
    print("New User", uid)
    # uid = input("Enter user ID:")
    # result_set = select_phonecalls_by_ownerid(user_id)
    # for row in result_set:
    #     print(row)

    # sql injection = if you do not filter the user input then teh user can run other sql quieres that are not inteded (no quthentication)
    # -- comment in sql ' or 1=1 --/just wants the last clause to be equal to true

if __name__ == '__main__':
    print("file", __file__)

    import pathlib #allows us to
    print("parent of file",pathlib.Path(__file__).parent)
    print("absolute path to parent of file", pathlib.Path(__file__).parent.absolute())

    db_location = os.path.join(pathlib.Path(__file__).parent.absolute(), "data")
    print("path to db location", db_location)

    result_set = select_phonecalls()
    for row in result_set():
        print(row)
'''
November 15, 2023
Discussing how to open a file
'''