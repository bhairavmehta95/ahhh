import MySQLdb

db_data = MySQLdb.connect(host="localhost", user="root", passwd="root", db="ahhh_data")
db_admins = MySQLdb.connect(host="localhost", user="root", passwd="root", db="ahhh_admins")
cursor_data = db_data.cursor()
cursor_admins = db_admins.cursor()
db_data.autocommit(True)
db_admins.autocommit(True)

def add_admin(admin_number,namespace):
    cursor_admins.execute("""INSERT INTO admins (admin_number,namespace)
                       VALUE (%s,%s)""", (admin_number,namespace))

def get_admin_number(namespace):
    cursor_admins.execute("SELECT * FROM admins WHERE namespace='"+namespace)

def remove_admin(admin_number):
    cursor_admins.execute("DELETE FROM admins WHERE admin_number="+str(admin_number))

def remove_question(unique_id):
    cursor_data.execute("DELETE FROM questions WHERE QuestionID="+str(unique_id))

def add_question(string,namespace):
    cursor_data.execute("""INSERT INTO questions (string,upvotes,posted_time,namespace,answered)
                       VALUE (%s,1,NOW(),%s,0)""", (string,namespace))

def get_questions_sorted_top_unanswered(namespace_value):
    cursor_data.execute("SELECT * FROM questions WHERE namespace='"+namespace_value+"'AND answered=0 ORDER BY upvotes")
    return cursor_data.fetchall()

def get_questions_sorted_new_unanswered(namespace_value):
    cursor_data.execute("SELECT * FROM questions WHERE namespace='"+namespace_value+"'AND answered=0 ORDER BY posted_time")
    return cursor_data.fetchall()

def get_questions_sorted_answered(namespace_value):
    cursor_data.execute("SELECT * FROM questions WHERE namespace='"+namespace_value+"' AND answered=1")
    return cursor_data.fetchall()

def increment_upvotes_by_one(unique_id):
    cursor_data.execute("SELECT upvotes FROM questions WHERE QuestionID="+str(unique_id))
    upvotes_value = cursor_data.fetchone()
    upvotes_value = upvotes_value[0]+1
    cursor_data.execute("UPDATE questions SET upvotes="+str(upvotes_value)+" WHERE QuestionID="+str(unique_id))

