import json
def maxi(data):
    # data = json.load(open(file,'r'))
    max = 0
    id = 0
    for i in data:
        if len(i["answ"]) >= max:
            max = len(i["answ"])
            id = i["id"]
    return(max)
if __name__ == "__main__":
    print(maxi(json.load(open("data.json",'r'))))