#Just For Backup, currently Not in use
import mysql.connector as mysql


def insert(steps_count,timer,wl):
    conn = mysql.connect(host="localhost",user="root",password="",database="GameScore")
    cur = conn.cursor()
    cur.execute("INSERT INTO score (steps, time,winlose) VALUES (%s, %s,%s)",(steps_count,timer,wl))
    print("working")
    cur.execute("commit")
    conn.close()


