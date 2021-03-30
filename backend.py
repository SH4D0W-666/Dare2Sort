#Just For Backup, currently Not in use
import mysql.connector as mysql

records=""
def insert(namevalue,point):
    conn = mysql.connect(host="localhost",user="root",password="",database="GameScore")
    cur = conn.cursor()
    cur.execute("INSERT INTO score (Name,Points) VALUES (%s,%s)",(namevalue,point))
    print("working")
    cur.execute("commit")
    conn.close()

def fetch():
    global  records,x
    conn = mysql.connect(host="localhost",user="root",password="",database="GameScore")
    cur = conn.cursor()
    cur.execute("SELECT * from score order by Points DESC")
    records = cur.fetchall()
    print("working")
    cur.execute("commit")
    conn.close()