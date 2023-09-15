# importing required modules
import json
from PyPDF2 import PdfReader
from sys import argv
ALPHA = list("αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔ∆ΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ")
input = print
part = 1
data= []
batchsize = 500
tmp = {}
def isint(str):
    try :
         _ = int(str)
         return True
    except:
         return False
def cleanint(s):
     res = ""
     for i in s:
        try:
                res+=str(int(i))
        except:
                return int(res)
def addq(str):
    try:
        tmp["answ"][str[0]] = str[1:].replace('\n',' ')
    except: 
        tmp["answ"] = {}
        tmp["answ"][str[0]] = str[1:].replace('\n',' ')
         
def istitle(str):
    if (isint(str[0])):
        return True
    else: return False     
    
def isa(str):
    if (str[0] =='α' or str[0] =='Α' or str[0] =='a' or str[0] =='A' ) and isq(str):
         return True
    return False
def isq(str):
    if str[0] in ALPHA and (str[1] == ' 'or str[1] == '.'):
         return True
    return False
def addt(str):
    tmp["title"] = str.replace('\n',' ')
    tmp["id"] = cleanint(str)
def appt(str):
     tmp["title"] += str.replace('\n',' ')
def commit():
    global tmp
    global data
    global part
    if (len(tmp.keys()) != 0):
        data.append(tmp)
    tmp = {}
    if len(data) >= batchsize:
        
        json.dump(data,open(argv[2].split('.')[0]+f"_pt{part}."+argv[2].split('.')[1],'w'), ensure_ascii=False)
        part +=1
        data = []
if __name__ == "__main__":  
    file = open(argv[1],'r')
    
    tphase = False 
    if len(argv) >= 4:
        batchsize = int(argv[3]) 
    for i in file.readlines():
        print(f"""
              '{i}'
              Is Title Phase: {tphase},   
              Is Title : {istitle(i)},   
              Is question : {isq(i)},   
              Is a : {isa(i)},   
              
              {tmp}
              """)
        # _ = input()
        if (tphase and not isa(i) ):
             print("APPEND TITLE")
             
             appt(i)
        if not tphase and istitle(i):
             print("ADD TITLE AND SET PHASE TO TITLE")
             commit()
             tphase = True
             addt(i)

        if (isa(i) and tphase):
             print("ADD Q AND DISABLE TITLE")
             
             tphase = False
             addq(i)
        if ( not tphase and isq(i) and not isa(i)):
             print("ADD Q ")
             
             tphase = False
             addq(i)
        _ = input()




    if len(tmp.keys()) != 0:

               data.append(tmp)
    for d in data:
        try:
         print (f'=={d["title"]}==')
         for a in d["answ"]:
              print (f"({a}) {d['answ'][a]}")
        except:
            _ = input(d)
    if part == 1 :
        json.dump(data,open(argv[2],'w'), ensure_ascii=False)
    else:
        json.dump(data,open(argv[2].split('.')[0]+f"_pt{part}."+argv[2].split('.')[1],'w'), ensure_ascii=False)
         

# print(len(data))