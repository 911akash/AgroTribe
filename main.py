import turtle
import time
import json
import requests

import csv

url = "https://api.thingspeak.com/channels/752531/fields/1.json?results=19"
r = ''

def getStartingIndex(r):
    for each in r.json()['feeds']:
        if each['field1'] == "0.00000":
            return each['entry_id']

def returnFieldValue(idvalue,r):
    for each in r.json()['feeds']:
        if each['entry_id'] == idvalue:
            return each['field1']

def getNWavelength(n):
    r = requests.get(url)
    entryID_0 = getStartingIndex(r)
    new_id = n + int(entryID_0)
    wavelenght = returnFieldValue(new_id,r)
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
    print(getNWavelength(2))
    wave = int(float(getNWavelength(5))*100)
    print(str(wave))
    color = ""
    #print(item)
    if wave in range(1, 400):
        color = "red"
    if wave in range(400, 800):
        color = "orange"
    if wave in range(800, 1400):
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
        text = "Red Tomato: Shelf life is 3 days"
    if colour == "green":
        text = "Green Tomato: Shelf life is 7 days"
    if colour == "orange":
        text = "Orange Tomato: Shelf life is 5 days"
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
