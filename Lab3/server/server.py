from socket import *
import DatabaseConnector as dbcon


####################################################################

def killserver():
    return "server is shutting down..."

def commander(comm):
    comar=comm.split()
    for i in range(0, 5):
        comar.append('0')
    print(comar)
    ##identificate command and calls function needed
    ##return result of function needed
    if (comar[0]=="checkin"):
        returnvar=checkin(comar[1], comar[2])
    elif (comar[0]=="shutdown"):
        returnvar=killserver(),
    elif (comar[0]=="getbudget"):            
        returnvar=getbudget(comar[1]),
    elif (comar[0]=="addtobudget"):
        returnvar=addtobudget(comar[1]),
    elif (comar[0]=="giveme"):
        returnvar=addtopersonalfrombudget(comar[1]),
    elif (comar[0]=="adduser"):
        returnvar=addnewusertoDB(),
    elif (comar[0]=="addfamily"):
        returnvar=addnewfamilytoDB(comar[1], comar[2]),
    else:
        returnvar=returnerror()
     
    return returnvar
    ##return result
    ##pass

############# function list #####################

def getbudget():
    ##return 
    pass

def returnerror():
    return "ErrorWrongCommand"

def addtobudget(money_amount):
    ##add to family budget amount of money
    ##return
    pass

def addnewfamilytoDB(name, start_budget):
    dbcon.createFamily(name, start_budget)

def addnewusertoDB():
    pass

def addtopersonalfrombudget(money_amount):
    ##set budget=budget-money_amount
    ##set personal=personal+money_amount
    pass
    
def checkin(login, password):
    ##request to database for givin` logins and passwords dictionary
    enterlist=dbcon.GetLogPasDict()
    returncommand=""
    print(enterlist)
    ##check if login and password entered is correct
    try:
        if (enterlist[login]==password):
            returncommand="EnterAs "+ dbcon.GetNames('users', 'login', login, 'names')
        else:
            returncommand="wrong user"
    except (ValueError, KeyError):
        returncommand="wrong user"
    print(returncommand)
    return returncommand




####################################################################

#данные сервера
host = 'localhost'
port = 25015


addr = (host,port)
tcp_socket = socket(AF_INET, SOCK_STREAM)

#bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)

#listen - запускает прием TCP
tcp_socket.listen(1)

data=''
while data!='shutdown':
    print('wait connection...')
    
    conn, addr = tcp_socket.accept()
    print('client addr: ', addr)
    #recv - получает сообщение TCP
    data = bytes.decode(conn.recv(1024))
    
    #если ничего не прислали, завершим программу
    if not data:
        conn.close()
        break
    else:
        print("command: ", data)
        command=commander(data)
        #send - передает сообщение TCP
        conn.send(str.encode(command))
        #close - закрывает сокет
        conn.close()
    
tcp_socket.close()



