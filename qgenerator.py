
from openpyxl import Workbook
import json
import test
from sys import argv

sheettitle = 'Sheetname'

wb = Workbook()
wb['Sheet'].title = sheettitle
sh1 = wb.active
def nextcollumn (cell):
    c = cell[1:]
    r = cell[0]
    return chr(ord(r)+1)+c
def nextrow (cell):
    c = cell[1]
    r = cell[0]
    return r+str(int(c)+1)
def gen_titles(sh,na):
    # sh['A1'] = '#'
    sh['A1'] = 'Question'
    sh['B1'] = 'Question Type'

    curr = 'B1'
    for i in range(na):
        curr = nextcollumn(curr)
        sh[curr] = f"Option {i+1}"
    curr = nextcollumn(curr)
    sh[curr] = "Correct Answer"
    curr = nextcollumn(curr)
    sh[curr] = "Time"
    curr = nextcollumn(curr)
    sh[curr] = "Image Link"
def add_list(sh,l,r):
    curr = f"A{r}"
    for i in l:
        # _ = input(f" {curr} <-- {i}")
        sh[curr] = i
        curr = nextcollumn(curr)
def to_list(d,maxi):
    id = d["id"]
    title = d["title"]
    questions = [d["answ"][i] for i in d["answ"]]
    questions = questions+['']*(maxi - len(questions))
    return [title,"MultipleChoice"]+questions+[1,'','']

if __name__ == "__main__":
    filename = argv[2]
    file = argv[1]
    # file = file
    data = json.load(open(file,'r'))
    m = test.maxi(data)
    gen_titles(sh1,m)

    for i,d in enumerate(data):
        add_list(sh1,to_list(d,m),i+3)

    try:
        wb.save(filename)
    except PermissionError:
        print('File might be opened, please close it before writing')