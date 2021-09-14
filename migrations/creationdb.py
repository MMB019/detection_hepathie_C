import sqlite3

#creation of the database
def creation_tableau(database="database.db"):

    conn=sqlite3.connect(database)

    conn.execute("CREATE TABLE prediction (id integer auto_increment primary key, firstName TEXT,lastName TEXT, sex varchar, age varchar,alb varchar,alp varchar,alt varchar, ast varchar, bil varchar,che varchar , chol varchar, crea varchar,ggt varchar, port varchar,result integer)")

    print("la creation de la table prediction ok!")

    conn.close()

#execution du code 

if __name__=="__main__":
    creation_tableau()