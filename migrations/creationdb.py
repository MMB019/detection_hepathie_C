import sqlite3

def creation_tableau(database="database.db"):

    conn=sqlite3.connect(database)

    conn.execute("CREATE TABLE prediction (firstName TEXT,lastName TEXT, sex varchar, age varchar,alb varchar,alp varchar,alt varchar, ast varchar, bil varchar,che varchar , chol varchar, crea varchar,ggt varchar, port varchar)")

    print("la creation de la table prediction ok!")

    conn.close()