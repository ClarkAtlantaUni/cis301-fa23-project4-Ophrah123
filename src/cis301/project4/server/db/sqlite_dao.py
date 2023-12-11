import sqlite3
import uuid
from hashlib import md5

from cis301.phonebill.phonebill_dao import AbstractPhoneBill_DAO
from cis301.phonebill.phonecall_dao import AbstractPhoneCall_DAO
from cis301.project4 import phonecall


# TODO Finish Implementing the abstract methods

class PhoneBill_DAO(AbstractPhoneBill_DAO, AbstractPhoneCall_DAO):
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def insert_phonebill(self, phonebill):
        pass

    def update_phonebill(self, phonebill):
        pass

    def delete_phonebill(self, phonebill):
        pass

    def select_phonebill(self, phonebill_id):
        pass

    def search_phonebills_bydate(self, startdate, enddate):
        pass

    def insert_phonecall(self, phonecall):
        conn = sqlite3.connect( self.dbfile )
        c = conn.cursor()
        data = (phonecall.get_caller(), phonecall.get_callee(), phonecall.get_starttime_string(), phonecall.get_endtime_string())
        c.execute( 'INSERT INTO phonecalls ( caller,callee, startdate, enddate) VALUES (?,?,?,?);', data )
        conn.commit()
        pid = c.lastrowid
        data = (phonecall.get_uid(), pid)
        c.execute( 'INSERT INTO phonebills ( uid, pid ) VALUES (?,?);', data )
        conn.commit()
        conn.close()
        return pid

    def update_phonecall(self, phonecall,phonecall_id):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        data = (phonecall.get_caller(), phonecall.get_callee(), phonecall.get_starttime_string(),
                phonecall.get_endtime_string(),phonecall_id)
        c.execute('UPDATE phonecalls SET caller=?,callee=?, startdate=?, enddate=? WHERE id =? ',data)
        conn.commit()
        conn.close()

    def delete_phonecall(self, phone_call_id):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        data = phone_call_id
        c.execute('DELETE from phonecall where id=?;', data)
        conn.commit()
        c.execute('DELETE from phonebills where pid=?;', data)
        conn.commit()
        conn.close()

    def select_phonecall(self, phonecall_id):
        pass

    def search_phonecalls_bydate(self, user, start_date, end_date):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        c.execute('select * from users where users.start_date=?, users.end_date=?', (user["start_date"],user["end_date"]))
        return c.fetchone()
    def search_phonecalls_bycaller(self, user, caller, callee):
        #phonecall =phonecall(caller,callee)
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        c.execute('select * from users where users.caller=?,users.callee=?', (user["caller"],(user["callee"])))
        return c.fetchone()
        conn.commit()
        conn.close()

    def search_phonecalls_bycustomername(self, customer_id):
        pass



    def insert_user(self, user):
        if not self.is_user_exists(user):
            conn = sqlite3.connect(self.dbfile)
            c = conn.cursor()
            data = (user["id"], user["name"], user["email"],user["password"])
            c.execute('INSERT INTO users (id, name,email, password) VALUES (?,?,?,?);', data)
            conn.commit()
            conn.close()
            return  True
        else:
            return False

    def authenticate_user(self,user):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        #passwd = str(md5(user['password'].encode()).digest())
        c.execute('select * from users where users.email=? and users.password=?', (user["email"] , user['password']))
        if c.fetchone():
            conn.close()
            return True
        else:
            conn.close()
            return False

    def get_user_by_email(self, user):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        c.execute('select * from users where users.email=?', (user["email"],))
        return c.fetchone()

    def is_user_exists(self, user):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        c.execute('select * from users where users.email=?', (user["email"],))
        rows =c.fetchone()
        if rows:
            return True
        else:
            return False
    def is_valid_phone_id(self, phonecall_id):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        c.execute('select * from phonecalls where phonecalls.id=?', (phonecall_id,))
        rows =c.fetchone()
        if rows:
            return True
        else:
            return False
#TODO  Implement Data Object Access(DAO) functionalities for Phonebills and PhoneCalls


if __name__ == '__main__':
    DAO = PhoneBill_DAO('../data/phonebill.db')
    user = dict()
    user['id'] = str(uuid.uuid4())
    user['email'] = 'abc@abc.com'
    user['name']="Test User"
    user['password'] = "123456"
    user['password'] = str(md5(user['password'].encode()).digest())
    DAO.insert_user(user)
    print(DAO.is_user_exists(user))