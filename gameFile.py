# import the required libraries
from tkinter import *
from PIL import ImageTk,Image
import random
# global variables for user score (userV) and computer score (computerV)
userV=0
computerV=0
root = Tk()
root.geometry("1000x1000")
root.title("Rock Paper Scissor")
evaluationSheet = {
    "Rock":"Scissor",
    "Paper":"Rock",
    "Scissor":"Paper"
}
# Evaluation function
def evaluation(uValue,cValue):
    if uValue==cValue:
        pass
    elif evaluationSheet[cValue]==uValue:
        global computerV
        computerV+=1
    else:
        global userV
        userV+=1

# Function that chooses answer for the computer
def answer():
    return random.choice(["Paper","Rock","Scissor"])

# Function that displays the score
def scoreCard():
    for i in root.winfo_children():
        i.destroy()
    root.config(bg="#fcfc81")
    if userV==computerV:
        label1= Label(root,text="DRAW",bg="#fcfc81",fg="#00cc00",font="{Comic sans MS} 45")
        label1.grid(row=2,column=5,columnspan=5,padx=500)
        label2 =Label(root,text="Congratulations!!!",fg="#00cc00",bg="#fcfc81",font="{Comic sans MS} 45")
        label2.grid(row=3,column=5,columnspan=5,padx=500,pady=50)
    elif userV>computerV:
        label1= Label(root,text="YOU WON",bg="#fcfc81",fg="#00cc00",font="{Comic sans MS} 45")
        label1.grid(row=2,column=5,columnspan=5,padx=500)
        label2 =Label(root,text="Congratulations!!!",fg="#00cc00",bg="#fcfc81",font="{Comic sans MS} 45")
        label2.grid(row=3,column=5,columnspan=5,padx=500,pady=50)
    else:
        label1= Label(root,text="COMPUTER WON",fg="#00cc00",bg="#fcfc81",font="{Comic sans MS} 45")
        label1.grid(row=2,column=5,columnspan=5,padx=450)
        label2 =Label(root,text="Better LUCK next TIME",fg="#00cc00",bg="#fcfc81",font="{Comic sans MS} 45")
        label2.grid(row=3,column=5,columnspan=5,padx=450,pady=50)
    menuButton = Button(root,text="Main Menu",cursor="hand2",borderwidth=0,bg="#fcfc81",fg="#6600cc",command=mainMenu,font="{Comic sans MS} 20")
    menuButton.grid(row=10,column=5,columnspan=5,padx=450,pady=20)
    lastQuitButton = Button(root,text="QUIT",cursor="hand2",fg="#ff0000",borderwidth=0,bg="#fcfc81",font="{Comic sans MS} 20",command=root.destroy)
    lastQuitButton.grid(row=12,column=5,columnspan=5,padx=450)
    spaces= Label(root,text="""




    """,bg="#fcfc81").grid(row=13,column=0,columnspan=50)
    label = Label(root,text="click 'Main Menu' to go to main menu and 'QUIT' to quit the game",bg="#fcfc81",font="{Comic sans MS} 15")
    label.grid(row=14,column=0,columnspan=20)

# Function that is executed when the each round ends   
def action(option):
    for i in root.winfo_children():
        i.destroy()
    root.config(bg="#d1f78b")
    userLabel= Label(root,text="YOU",bg="#d1f78b",fg="#6600cc",font="{Comic sans MS} 35 bold underline").grid(row=2,column=5,columnspan=5,padx=200)
    
    computerLabel = Label(root,text="COMPUTER",bg="#d1f78b",fg="#6600cc",font="{Comic sans MS} 35 bold underline").grid(row=2,column=10,columnspan=8)
    root.grid_rowconfigure(0,minsize=100)
    root.grid_columnconfigure(0,minsize=100)
    userChoiceLabel = Label(root,text=option,bg="#d1f78b",font="{Comic sans MS} 20")
    userChoiceLabel.grid(row=5,column=5,columnspan=5,padx=350,pady=30)
    computerChoiceLabel = Label(root,text=answer(),bg="#d1f78b",font="{Comic sans MS} 20")
    computerChoiceLabel.grid(row=5,column=10,columnspan=4,padx=100,pady=50)
    root.grid_rowconfigure(5,minsize=100)
    root.grid_columnconfigure(8,minsize=100)
    scoreLabel=Label(root,text="Score",bg="#d1f78b",fg="#800000",font="{Comic sans MS} 32 bold underline")
    scoreLabel.grid(row=6,column=5,columnspan=8,pady=30)
    evaluation(option,computerChoiceLabel["text"])
    userScore = Label(root,text=userV,bg="#d1f78b",font="sans 32 bold")
    userScore.grid(row=8,column=5,columnspan=5)
    computerScore= Label(root,text=computerV,bg="#d1f78b",font="sans 32 bold")
    computerScore.grid(row=8,column=10,columnspan=4)
    espace= Label(root,text="""
    
    






    """,bg="#d1f78b")
    espace.grid(row=9,column=2,columnspan=4)
    continueButton = Button(root,text="Continue",borderwidth=0,bg="#d1f78b",fg="#006600",cursor="hand2",font = "{Comic sans MS} 15",command=play)
    continueButton.grid(row=10,column=5,columnspan=8,pady=30)
    stopButton = Button(root,text="STOP",cursor="hand2",borderwidth=0,bg="#d1f78b",fg="red",font = "{Comic sans MS} 15",command=scoreCard)
    stopButton.grid(row=10,column=8,columnspan=8)
    noteLabel = Label(root,bg="#d1f78b",text="click 'Continue' to GO to NEXT STEP and 'STOP' to see the results.",font="{Comic sans MS} 15")
    noteLabel.grid(row=12,column=2,columnspan=8)

# Function that is executed when the PLAY button is clicked   
def play():
    global rock
    global paper
    global scissor
    root.config(bg="#d3edf0")
    for i in root.winfo_children():
        i.destroy()
    
    nLabel = Label(root, text = "Lets play",bg="#d3edf0",fg="#1409e3",font ="{Comic sans MS} 40")
    nLabel.grid(row = 0, column =10,columnspan=5)
    root.grid_columnconfigure(10,weight=1)
    quitButton = Button(root,text = "QUIT",bg="#d3edf0",fg="red",cursor="hand2",font = "{Comic sans MS} 34 bold",borderwidth=0,command=root.destroy)
    quitButton.grid(row =2, column =5)
    chooseLabel= Label(root,text="Choose an option",bg="#d3edf0",font="{Comic sans MS} 20")
    chooseLabel.grid(row =5,column=5,padx=20,pady=35)
    rock= ImageTk.PhotoImage(Image.open("C:\\Users\\soorya\\Desktop\\game\\IMG_20201001_122814.jpg"))
    paper = ImageTk.PhotoImage(Image.open("C:\\Users\\soorya\\Desktop\\game\\IMG_20201001_121013.jpg"))
    scissor = ImageTk.PhotoImage(Image.open("C:\\Users\\soorya\\Desktop\\game\\IMG_20201001_120535.jpg"))
    rockButton =Button(root,image=rock,text="Rock",cursor="hand2",bg="#00004d",fg="#ffffff",borderwidth=0,compound="top",font="{Comic sans MS} 12",command=lambda : action(rockButton["text"]))
    rockButton.grid(row=7,column=5,padx=10)
    paperButton =  Button(root,image = paper,text="Paper",cursor="hand2",bg="#00004d",fg="white",borderwidth=0,compound="top",font="{Comic sans MS} 12",command=lambda : action(paperButton["text"]))
    paperButton.grid(row=7,column=6)
    scissorButton = Button(root,image=scissor,text="Scissor",cursor="hand2",bg="#00004d",fg="white",borderwidth=0,compound="top",font="{Comic sans MS} 12 ",command=lambda : action(scissorButton["text"]))
    scissorButton.grid(row=7,column=7,padx=10)
    labelC = Label(root,text="Computer will automatically\nChoose an option",bg="#d3edf0",font="{Comic sans MS} 32")
    labelC.grid(row=7,column=8,columnspan=10)

# The main  function from where the GAME STARTS       
def mainMenu():
    for i in root.winfo_children():
        i.destroy()
    global userV
    global computerV
    userV=0
    computerV=0
    root.config(bg="#fadcf4")
    heading = Label(root,text = "Rock-Paper-Scissor",font = "{Comic sans MS} 42 bold underline",bg="#fadcf4",fg="#ba1298")
    heading.grid(row=0, column = 5,columnspan=5)
    canvas = Canvas(root,height = 500,width = 600,bg="#c714a3")
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\soorya\\Desktop\\game\\dce307fdedcd262062d719590efc96ae.jpg"))
    canvas.create_image(302,255,image=img)
    canvas.grid(row = 5, column = 4,padx=30)
    canvas2= Canvas(root,width=700,height=500)
    guideLines = Label(canvas2,text="HOW TO PLAY ?\n\nRULES\n\n1. Rock VS Paper => Paper WINS\n      2. Paper VS  Scissor => Scissor WINS\n 3. Scissor VS Rock => Rock WINS",font="{Comic sans MS} 22")
    guideLines.grid(row=0,column=0,columnspan=6,pady=60,padx=10)
    statement = Label(canvas2,text="NOTE:\nYou need to select an option and Computer will automatically Choose its option.\nScores will be displayed at the end of each cycle.",font="{Comic sans MS} 10")
    statement.grid(row=5,column=0,columnspan=6,pady=45,padx=10)
    canvas2.grid(row=5,column=5)
    spaces = Label(root, text= """



    """,bg="#fadcf4")
    spaces.grid(row= 3,column =0)

    playButton = Button(root,text = "PLAY",cursor="hand2",font="{Comic sans MS} 30 bold", borderwidth=0,bg="#fadcf4",fg="#c714a3",command = play)
    playButton.grid(row=6,column = 5,pady=1)
    spacesTwo = Label(root,text ="""

    """,bg="#fadcf4")
    spacesTwo.grid(row=6,column = 0)
    root.mainloop()


# THE STARTING POINT, calling the main function
mainMenu()





