def logg(commar):
    line=""
    for el in commar:
        line+=str(el)+" "
    line+="\n"
    with open("logg.txt", 'a') as log:    
        log.write(str(line)+" \n")

def GetLogEvents():
    allevents=[]
    with open("logg.txt", "r") as log:
        for lines in log:
            line=lines[0:-2]
            allevents.append(line)
    return allevents
