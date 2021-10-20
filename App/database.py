import psycopg2
from App.config import HOST, USER, PASSWORD, DATABASE,SCHEMA
from flask import jsonify
import pandas as pd #type:ignore

def InsertData(columns,values):
    try:
        conn = psycopg2.connect(host=HOST, database=DATABASE,user=USER, password=PASSWORD)
        query = 'INSERT INTO {0}."guest" {1} VALUES {2}'.format(SCHEMA,columns,values)
        cur=conn.cursor
        cur.execute(query)
        rowcount = cur.rowcount
        print(rowcount)
        conn.commit()
        return jsonify({'message': 'success', 'rowcount': rowcount})
    except Exception as e:
        conn.rollback()
        print("error in Insert")
        return jsonify({"message":"error","message":e})

def UpdateData(values):
    try:
        conn = psycopg2.connect(host=HOST, database=DATABASE,user=USER, password=PASSWORD)
        query = 'Update {0}."guest" SET "name"={1}, "price"={2} where "id"={3}'.format(SCHEMA,values['name'],values['price'],values['id'])
        cur=conn.cursor
        cur.execute(query)
        rowcount = cur.rowcount
        print(rowcount)
        conn.commit()
        return jsonify({'message': 'success', 'rowcount': rowcount})
    except Exception as e:
        conn.rollback()
        print("error in Update")
        return jsonify({"message":"error","message":e})

def ViewData(id):
    try:
        conn = psycopg2.connect(host=HOST, database=DATABASE,user=USER, password=PASSWORD)
        query = 'SELECT * from {0}."guest" where "id"=\'{0}\' '.format(id)
        columns = ['id','name','price']
        df=pd.read_sql(conn,query)
        return df
    except Exception as e:
        print("error in View",e)
        df=pd.DataFrame({})
        return df


def DeleteData(id):
    try:
        conn = psycopg2.connect(host=HOST, database=DATABASE,user=USER, password=PASSWORD)
        query = 'Delete from {0}."guest" where "id"=\'{0}\''.format(SCHEMA,id)
        cur=conn.cursor
        cur.execute(query)
        rowcount = cur.rowcount
        print(rowcount)
        conn.commit()
        return jsonify({'message': 'success', 'rowcount': rowcount})
    except Exception as e:
        conn.rollback()
        print("error in Insert")
        return jsonify({"message":"error","message":e})