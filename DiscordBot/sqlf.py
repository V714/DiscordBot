import pymysql
import mysql.connector

### Taking list of users from database
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

### Taking only one person from database by nickname
def load_sp(nickname):
    rf = open("rootpsw.txt")
    rpsw = rf.readline()
    rf.close()

    conn = mysql.connector.connect(host='localhost',user='dicbot',passwd=rpsw,db='discordbot')
    cursor = conn.cursor(buffered=True)


    sql = ('SELECT nick FROM drrruserslist WHERE nick LIKE "%s" ;' % nickname)
    cursor.execute(sql)
    nick=cursor.fetchall()

    ### If there is no user with that nickname
    if not nick:
        return "Nie ma kogoś takiego na liście :cry:"
    sql = ('SELECT yo FROM drrruserslist WHERE nick LIKE "%s" ;' % nickname)
    cursor.execute(sql)
    yo=cursor.fetchall()
    sql = ('SELECT name FROM drrruserslist WHERE nick LIKE "%s" ;' % nickname)
    cursor.execute(sql)
    name=cursor.fetchall()
    database=''
    n,y,m=[],[],[]
    ### This code could be smaller I know
    for el in nick:
        n.append(str(el))
    for el in yo:
        y.append(str(el))
    for el in name:
        m.append(str(el))
    conn.close()

    for i in range(0,len(nick)):
       database+=str('{:-<10}{:-^10}{:->10}'.format(n[i],y[i],m[i]))+" --- :heart: For {0.author.mention}!"
    return database 

### Adding new user to database directly from Discord channel
def add_db(nick, yo, name):
    rf = open("rootpsw.txt")
    rpsw = rf.readline()
    rf.close()


    conn = mysql.connector.connect(host='localhost',user='dicbot',passwd=rpsw,db='discordbot')
    cursor = conn.cursor(buffered=True)

    sql = 'INSERT INTO drrruserslist(nick, yo, name) VALUES(%s,%s,%s)'
    data = (nick,int(yo),name)
    cursor.execute(sql,data)
    conn.commit()
    if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
    else:
            print('last insert id not found')
 

    conn.close()