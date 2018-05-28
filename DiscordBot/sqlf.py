import pymysql
import mysql.connector

def load_db():
    rf = open("rootpsw.txt")
    rpsw = rf.readline()
    rf.close()


    conn = mysql.connector.connect(host='localhost',user='dicbot',passwd=rpsw,db='discordbot')
    cursor = conn.cursor(buffered=True)

    sql = ('SELECT nick FROM drrruserslist;')
    cursor.execute(sql)
    nick=cursor.fetchall()
    sql = ('SELECT yo FROM drrruserslist;')
    cursor.execute(sql)
    yo=cursor.fetchall()
    sql = ('SELECT name FROM drrruserslist;')
    cursor.execute(sql)
    name=cursor.fetchall()
    database=''
    n,y,m=[],[],[]
    for el in nick:
        n.append(str(el))
    for el in yo:
        y.append(str(el))
    for el in name:
        m.append(str(el))
    conn.close()

    for i in range(0,len(nick)):
       database+=str('{:-<15}{:-^15}{:->15}'.format(n[i],y[i],m[i]))
       database+="\n"
    return database 
