import sqlite3 as sq

conn=sq.connect('main.db')
curs=conn.cursor()

def GetLogPasDict():
    log_pas={}
    curs.execute('SELECT login, password FROM users')
    row=curs.fetchall()
    print(row)
    log_pas={el[0] : el[1] for el in row}
    return log_pas

def createFamily(name1, start_budget):
    curs.execute("INSERT INTO familys ( name, budget ) VALUES ( '%s', '%d' )"%(name1, int(start_budget)))
    conn.commit()
    print("added")

def createUser(login, first_name, second_name, last_name, family, start_budget, password):
    curs.execute('''INSERT
    INTO users ( login, password, names, personal, family )
    VALUES ( '%s', '%s', '%s', '%d', '%s' )'''%(login, password, first_name+' '+second_name+' '+last_name, start_budget, family))
    curs.execute('''SELECT members
    FROM familys 
    WHERE name = '%s'
    '''%(family))
    members_temp=curs.fetchone()
    members=members_temp[0]+", "+login
    curs.execute('''UPDATE familys
    SET members =  '%s'
    WHERE name = '%s'
    '''%(members, family))
    conn.commit()
    print("added")

##class DB(object): 
##    def __init__(self):
##        self.conn=sq.connect('main.db')
##        curs=self.conn.cursor()
##
##    def createDB(self):
##        username="hello"
##        userpass="world"
##        self.conn=sq.connect('main.db')
##        curs=self.conn.cursor()
##        curs.execute("INSERT INTO users (name, password) VALUES ('%s' , '%s')"%(username,userpass))
##        self.conn.commit()
##        curs.execute('SELECT * FROM users')
##        row=curs.fetchone()
##        while row is not None:
##            print("id: "+str(row[0])+" Логин: "+row[1]+" | Пароль: "+row[2])
##            row = curs.fetchone()
        
def GetNames(table, keycolumn, cellname, needcolumn):
    curs.execute('''
        SELECT names
        FROM users
        WHERE id = '%s'
        '''%(cellname))
    result=curs.fetchone()
    conn.commit()
    return result
##    return curs.fetchone()[0]

def SetCellWhere(table, needcolumn, value, keycolumn, cellname):
    curs.execute('''
        UPDATE '%s'
        SET '%s' = '%d'
        WHERE '%s' = '%s'
        '''%(table, needcolumn, value, cellname, keycolumn))
##    return curs.fetchone()[0]




