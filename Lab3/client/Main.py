import client as sender


###############################################################################
def NewUser(first_name, mid_name, last_name, login, password):
    sender.sendtoserver('adduser '+first_name+" "+mid_name+" "+last+name+" "+login+" "+password)

def login(login, password):
    info=sender.sendtoserver('checkin '+login+" "+password).split()
    print(info)
    if(info[0]!="EnterAs"):
        print("wrong user, try again")
    else:
        return CurrentUser(info[1], info[2], info[3], login)
    

###############################################################################

class UserBasic(object):
    
    def __init__(self, first_name, mid_name, last_name):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name+' '+self.mid_name+' '+self.last_name

###############################################################################

class CurrentUser(UserBasic):
    def __init__(self, first_name, mid_name, last_name, login):
        UserBasic.__init__(self, first_name, mid_name, last_name)
        self.login=login
        print("entered as", login)
        ##add login action to history

    def GetBudget(self):
        sender.sendtoserver('getbudget')
        ##add GetBudget by CurrentUser action to history
        pass

    def AddMoneyToBudget(self, money_amount):
        sender.sendtoserver('addtobudget '+  +str(money_amount))
        ##add money_amount to main budget
        ##add AddMoneyToBudget by CurrentUser action to history
        pass

    def AddToPersonalFromBudget(self, money_amount):
        sender.sendtoserver('giveme '+str(money_amount))
        ##take money_amount from badget and add in to personal cash in db
        ##add AddToPersonalFromBudget by CurrentUser action to history
        pass

    def ChangePersonal(self, operation, money_amount):
        if(operation!='add' or operation!='sub'):
            print('wrong operation, first argument recives "add" or "sub" and second recive money amount you want to add or substract')
        else:
            sender.sendtoserver('changeme '+operation+str(money_amount))

    def commandlist():
        print("GetBudget() - returns current budget of your family")
        print("")



def main():
    login=input("enter you login: ")
    password=input("enter your password: ")
    current_user=login(login, password)
