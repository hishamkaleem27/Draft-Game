from tkinter import *
import random

root = Tk()
screen = Canvas(root, height = 1400, width = 2000, bg = 'grey12')
screen.pack()
root.config(cursor = 'circle')

bgImage = PhotoImage(file = 'bgi.gif')
bgCreate = screen.create_image(1000, 700, image = bgImage)

pgList = ['curry.gif', 'george.gif', 'johnson.gif', 'lillard.gif', 'morant.gif', 'murray.gif', 'paul.gif', 'rose.gif', 'walker.gif', 'westbrook.gif']
sgList = ['bryant.gif', 'butler.gif', 'carter.gif', 'derozan.gif', 'harden.gif', 'iverson.gif', 'jordan.gif', 'smith.gif', 'thompson.gif', 'wade.gif']
sfList = ['anthony.gif', 'durant.gif', 'erving.gif', 'hayward.gif', 'iguodala.gif', 'james.gif', 'leonard.gif', 'middleton.gif', 'oubre.gif', 'wiggins.gif']
pfList = ['akumpo.gif', 'bird.gif', 'bosh.gif', 'davis.gif', 'garnett.gif', 'green.gif', 'griffin.gif', 'malone.gif', 'nowitzki.gif', 'siakam.gif']
cList = ['cousins.gif', 'embiid.gif', 'fall.gif', 'gobert.gif', 'howard.gif', 'kareem.gif', 'ming.gif', 'russell.gif', 'shaq.gif', 'wilt.gif']   

def pgSelect():
    global pgNum, pgImage, pgCreate
    pgNum = random.choice(pgList)
    pgImage = PhotoImage(file = pgNum)
    pgCreate = screen.create_image(335, 300, image = pgImage)
    
def sgSelect():
    global sgNum, sgImage, sgCreate
    sgNum = random.choice(sgList)
    sgImage = PhotoImage(file = sgNum)
    sgCreate = screen.create_image(985, 300, image = sgImage)
    
def sfSelect():
    global sfNum, sfImage, sfCreate
    sfNum = random.choice(sfList)
    sfImage = PhotoImage(file = sfNum)
    sfCreate = screen.create_image(1635, 300, image = sfImage)

def pfSelect():
    global pfNum, pfImage, pfCreate
    pfNum = random.choice(pfList)
    pfImage = PhotoImage(file = pfNum)
    pfCreate = screen.create_image(660, 950, image = pfImage)
    
def cSelect():
    global cNum, cImage, cCreate
    cNum = random.choice(cList)
    cImage = PhotoImage(file = cNum)
    cCreate = screen.create_image(1310, 950, image = cImage)

pgB = Button(root, text = 'PG', width = 10, height = 2, cursor = 'target', command = pgSelect)
pgButton = screen.create_window(335, 600, window = pgB)


sgB = Button(root, text = 'SG', width = 10, height = 2, cursor = 'target', command = sgSelect)
sgButton = screen.create_window(985, 600, window = sgB)

sfB = Button(root, text = 'SF', width = 10, height = 2, cursor = 'target', command = sfSelect)
sfButton = screen.create_window(1635, 600, window = sfB)

pfB = Button(root, text = 'PF', width = 10, height = 2, cursor = 'target', command = pfSelect)
pfButton = screen.create_window(660, 1250, window = pfB)

cB = Button(root, text = 'C', width = 10, height = 2, cursor = 'target', command = cSelect)
cButton = screen.create_window(1310, 1250, window = cB)
