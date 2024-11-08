#!/usr/bin/python3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

rooms = {
            'Hall': {
                  'south': 'Kitchen',
                  'east': 'Dining Room',
                  'item': 'key',
                  'desc': 'You are in a dusty hall. A kitchen that smells of death is to the south. An equally dusty dining room lies to the east.'
                },
            'Kitchen': {
                  'north': 'Hall',
                  'item': 'monster',
                  'desc': 'You barely have time to take in the bone-strewn kitchen before a monster rises from the shadows and LUNGES AT YOU!'
                },
            'Dining Room': {
                  'west': 'Hall',
                  'south': 'Garden',
                  'item': 'potion',
                  'desc': 'This dining room is caked with dust. All of the food has long since been eaten by rats.'
               },
            'Garden': {
                  'north': 'Dining Room',
                  'desc': 'This garden has long since gone to ruin. A rusty gate with a barely legible sign reads "I OPEN ONLY FOR THE HOLDER OF BOTH KEY AND POTION."'
               },
         }

inventory = []
currentRoom = "Hall"
message = ""
gameover = False

@app.route("/")
def start():
    x = rooms[currentRoom]
    return render_template("status.html", inv=inventory, currentRoom=x, currentroomdict=rooms, msg=message, gameover=gameover)

@app.route("/action", methods=["POST"])
def action():
    global message
    if request.form.get("nm"):
        move = request.form.get("nm").lower().split(" ", 1)
        message = goget(move)
        if endcheck():
            message = endcheck()
    else:
        message = ""
    return redirect("/")

def endcheck():
    global gameover
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        gameover = True
        return 'You escaped the house with the ultra rare key and magic potion... YOU WIN!'
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        gameover = True
        return 'A monster has got you... GAME OVER!'
    else:
        return None

def goget(move):
    global currentRoom
    global inventory
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            return ""
        else:
            return "You can't go that way!"
    elif move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            del rooms[currentRoom]['item']
            return f"{move[1]} got!"
        else:
            return f"Can't get {move[1]}!"
    return ""

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
