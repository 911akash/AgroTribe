import turtle
import time
import json
import requests

import csv

url = "https://api.thingspeak.com/channels/752531/fields/1.json?results=19"
r = requests.get(url)

def getStartingIndex():
    for each in r.json()['feeds']:
        if each['field1'] == "0.00000":
            return each['entry_id']

def returnFieldValue(idvalue):
    for each in r.json()['feeds']:
        if each['entry_id'] == idvalue:
            return each['field1']

def getNWavelength(n):
    entryID_0 = getStartingIndex()
    new_id = n + int(entryID_0)
    wavelenght = returnFieldValue(new_id)
    return wavelenght

def getcolor():
    # with open('readings.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     mylist = []
    #     for row in csv_reader:
    #         mylist=row
    #     print(mylist)
    #     color = ""
    #     item = float(mylist[4])*100
    print(getNWavelength(5))
    wave = int(float(getNWavelength(5)))
    print(str(wave))
    color = ""
    #print(item)
    if wave in range(1, 200):
        color = "red"
    if wave in range(200, 350):
        color = "orange"
    if wave in range(350, 600):
        color = "green"

    return color

def drawCircle(colour):
    font = ("Arial", 28, 'normal', 'bold', 'italic', 'underline')
    myturtle = turtle.Turtle()
    turtle.Screen().title("Agro Tribe")
    #turtle.title("Agro Tribe")
    t = turtle.Pen()
    t.begin_fill()
    t.circle(100)
    text = ""
    if colour == "red":
        text = "Shelf life is 3 days"
    if colour == "green":
        text = "Shelf life is 7 days"
    if colour == "orange":
        text = "Shelf life is 5 days"
    t.color(colour)
    t.speed(10)
    t.end_fill()

    t.hideturtle()
    t_text = turtle.Pen()
    t_text.write(text, align="center", font=font)


def readFile(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content

def parseJson():
    fjson = open('data.json', 'r')
    jsoncontent = fjson.read()
    jsonText = json.loads(jsoncontent)
    print(jsonText['channel']['field1'])


while True:
    #parseJson()
    whatcolor = getcolor()
    drawCircle(whatcolor)
