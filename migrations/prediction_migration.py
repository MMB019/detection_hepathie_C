import sqlite3


#insertion des données dans la base données
def insert_to_database(fname,lname,data,result):
    
    try:
        conn=sqlite3.connect("database.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO prediction (firstName,lastName,sex,age,alb,alp,alt, ast, bil,che, chol, crea,ggt,port,result) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ",(fname,lname,*data,*result))
        conn.commit()
        print("insertion effectuer !!!",*result)
    except:

        conn.rollback()
        print("insertion non effectuer!")
    finally:
        conn.close()

#lecture de toutes les donner
def select_all():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM prediction")
    rows=cur.fetchall()
    return rows