# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:49:55 2022

@author: Ozdemir Can
"""

from tkinter import *
# from PIL import Image
import tkinter as tk
from getNBAFunc_diff_final import getRecord,getTeamData

# add widgets here
from PIL import ImageTk, Image
# from calendar import month_name
from tkinter import ttk
# import only_tablev4_comparison
import os
import os.path
import math

import random
from numpy import mean

window=Tk()
# new2=Tk()
# exec(open("only_tablev4_comparison.py").read())
record_team = getRecord()
teamData = getTeamData()
# record_team={'a':'1','b':'2','c':'3','d':'4'}
# teamname=[]
list_teamnames=list(record_team.keys())
# for i in range(0,len(list_teamnames)):
#     teamname[i]=list_teamnames
image1 = Image.open("atlanta.png")
testimage1 = ImageTk.PhotoImage(image1)
image2 = Image.open("boston.png")
testimage2 = ImageTk.PhotoImage(image2)
image3 = Image.open("charlotte.png")
testimage3 = ImageTk.PhotoImage(image3)
image4 = Image.open("chicago.png")
testimage4 = ImageTk.PhotoImage(image4)
image5 = Image.open("cleveland.png")
testimage5 = ImageTk.PhotoImage(image5)
image6 = Image.open("dallas.jpg")
testimage6 = ImageTk.PhotoImage(image6)
image7 = Image.open("denver.jpg")
testimage7 = ImageTk.PhotoImage(image7)
image8 = Image.open("detroit.jpg")
testimage8 = ImageTk.PhotoImage(image8)
image9 = Image.open("goldenstate.png")
testimage9 = ImageTk.PhotoImage(image9)
image10 = Image.open("houston.png")
testimage10 = ImageTk.PhotoImage(image10)
image11 = Image.open("indianapolis.png")
testimage11 = ImageTk.PhotoImage(image11)
image12 = Image.open("clippers.png")
testimage12 = ImageTk.PhotoImage(image12)
image13 = Image.open("lakers.png")
testimage13 = ImageTk.PhotoImage(image13)
image14 = Image.open("memphis.png")
testimage14 = ImageTk.PhotoImage(image14)
image15 = Image.open("miami.png")
testimage15 = ImageTk.PhotoImage(image15)
image16 = Image.open("milwaukee.png")
testimage16 = ImageTk.PhotoImage(image16)
image17 = Image.open("minnesota.png")
testimage17 = ImageTk.PhotoImage(image17)
image18 = Image.open("neworleans.png")
testimage18 = ImageTk.PhotoImage(image18)
image19 = Image.open("newyork.png")
testimage19 = ImageTk.PhotoImage(image19)
image20 = Image.open("brooklyn.png")
testimage20 = ImageTk.PhotoImage(image20)
image21 = Image.open("oklohama.png")
testimage21 = ImageTk.PhotoImage(image21)
image22 = Image.open("orlando.png")
testimage22 = ImageTk.PhotoImage(image22)
image23 = Image.open("philadelphia.png")
testimage23 = ImageTk.PhotoImage(image23)
image24 = Image.open("phoenix.png")
testimage24 = ImageTk.PhotoImage(image24)
image25 = Image.open("portland.png")
testimage25 = ImageTk.PhotoImage(image25)
image26 = Image.open("sacramento.png")
testimage26 = ImageTk.PhotoImage(image26)
image27 = Image.open("sanantonio.png")
testimage27 = ImageTk.PhotoImage(image27)
image28 = Image.open("toronto.jpg")
testimage28 = ImageTk.PhotoImage(image28)
image29 = Image.open("utah.jpg")
testimage29 = ImageTk.PhotoImage(image29)
image30 = Image.open("washington.png")
testimage30 = ImageTk.PhotoImage(image30)


dict_im={'ATL':testimage1,'BOS':testimage2,'CHO':testimage3,'CHI':testimage4,'CLE':testimage5,'DAL':testimage6,'DEN':testimage7,
            'DET':testimage8,'GSW':testimage9,'HOU':testimage10,'IND':testimage11,'LAC':testimage12,'LAL':testimage13,'MEM':testimage14,
            'MIA':testimage15,'MIL':testimage16,'MIN':testimage17,'NOP':testimage18,'NYK':testimage19,'BRK':testimage20,'OKC':testimage21,
            'ORL':testimage22,'PHI':testimage23,'PHO':testimage24,'POR':testimage25,'SAC':testimage26,'SAS':testimage27,'TOR':testimage28,
            'UTA':testimage29,'WAS':testimage30}










class NewWindow(Toplevel):
     
    def __init__(self, master = None):
         
        super().__init__(master = master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text ="This is a new Window")
        label.pack()




global abc
global abc1
abc=''
abc1=''

bgimage= Image.open("lebron.jpg")
bgimagee = bgimage.resize((700,700))
testimagee = ImageTk.PhotoImage(bgimagee)
bgimage1= Image.open("curry.jpg")
bgimage11 = bgimage1.resize((700,700))
testimagee1 = ImageTk.PhotoImage(bgimage11)

#background image
img = PhotoImage(file="nba_bg_cropped_50.png")
img2 = PhotoImage(file="NBA-Player-PNG-Picture.png")
# label = Label(
#     window,
#     image=img
# )
# label.place(x=0, y=0) 
  



canvas = Canvas(window, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=img, anchor='nw')

def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("nba_bg_cropped_50.png")
#    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)

    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')

window.bind("<Configure>", resize_image)




# btn1=Button(window, text="Select Team - Comparison", fg='red')
# btn1.place(x=300, y=100)

# btn2=Button(window, text="Who wins?", fg='green')
# btn2.place(x=150, y=200)



#new window open version 1
# btn3 = Button(window,
             # text ="Click to open a new window")
# btn3.place(x=150, y=500)
# btn3.bind("<Button>",
         # lambda e: NewWindow(window))
# btn3.pack(pady = 10)
# def print_it(event):
#   print var.get()





def open_win_records():
    def close():
        new1.destroy()
    #    # new2.quit()
    new1= Toplevel(window)
    new1.geometry("750x750")
    new1.title('Stats')
    def clear_all():
        for item in tree.get_children():
            tree.delete(item)
    def OptionMenu_CheckButton(event):
        clear_all()
        print(variable.get())
        vals=list(record_team[variable.get()].values())
        tree.insert('', 'end', text="1", values=vals)
        pass
    # btns1=Button(new1, text="Which team", fg='green')
    # btns1.place(x=150, y=200)
    variable = StringVar(window)
    variable.set("ATL") # default value
    w = OptionMenu(new1, variable, *list_teamnames,command=OptionMenu_CheckButton)
    global str_out
    str_out=StringVar(new1)
    str_out.set("ATL")
    str_out2=StringVar(new1)
    str_out2.set("ATL")
    # l2 = Label(new1,  textvariable=str_out, width=40 ) 
    # l2.place(x=350, y=200)
    clearbutton=Button(new1, text= "Clear", command= clear_all).pack(pady=10)
    # w.pack()
    style = ttk.Style() #this is for table creation
    style.theme_use('clam')
    headline=list(record_team['ATL'].keys())
# vals=list(record_team['ATL'].values())
    Button(new1, text= "Close the Window", font=("Calibri",14,"bold"), command=close).pack(pady=20)
    tree = ttk.Treeview(new1, column=headline, show='headings', height=1)
    for i in range(0,len(headline)):
        tree.column("# "+str(i+1), anchor=CENTER)
        tree.heading("# "+str(i+1), text=headline[i])
    tree.pack()
    w.pack()
    w.config(bg = "GREEN")
    w["menu"].config(bg="BLUE")
def open_win_compstats():
    global l100
    global l10
    global l99
    global l9
    global l3
    global l4
    global l40
    global l6
    global l5
    # global correct
    new2=Toplevel(window)
    new2.geometry("2000x2000")
    new2.title('Stats Comparison')
    image1 = Image.open("dissapoint.jpg")
    testimage = ImageTk.PhotoImage(image1)
    # testimage = PhotoImage(file="dissapoint.jpg",master=window)

    correct="You entered same teams, please change one of them!"
    correctt1="Team 1: You entered same teams, please change one of them!"
    correctt2="Team 2: You entered same teams, please change one of them!"
    correct3="Team 1: Please Fill the Blank"
    correct4="Team 2: Please Fill the Blank"
    l99 = Label(new2,  text=correct, width=40 )
    l100=Label(new2, width=500,image=testimage ) 
    l10=Label(new2, width=500,image=testimage ) 
    l5 = Label(new2,  text=correct3, width=40 ) 
    l6 = Label(new2,  text=correct, width=40 )
    l9 = Label(new2,  text=correct, width=40 ) 
    mistake="Team 1: OOPS Wrong Team, Please Enter the Team again"
    mistake1="Team 2: OOPS Wrong Team, Please Enter the Team again"
    l3 = Label(new2,  text=mistake, width=40 ) 
    l4 = Label(new2,  text=mistake, width=40 ) 
    l40 = Label(new2,  text=mistake, width=53 ) 


    lebronlabel=tk.Label(new2, width=700,image=testimagee) 
    lebronlabel.place(x=1215, y=0)
    # bgimage1= ImageTk.PhotoImage(file="./curry.jpg")

    currylabel=Label(new2, width=700,image=testimagee1) 
    currylabel.place(x=0, y=0)
    team1t=tk.StringVar()
    team1t.set("")
    str_out=tk.StringVar()
    team2t=tk.StringVar()
    str_out2=tk.StringVar()
    team1text=Entry(new2, textvariable=team1t,bg="orange",fg="green", font=("Comic Sans MS",14,"bold"), bd=20)
    team1text.place(x=0, y=620)
    # team1text.pack(side=LEFT)
    team2text=Entry(new2, textvariable=team2t,bg="orange",fg="blue",font=("Comic Sans MS",14,"bold"), bd=20)
    team2text.place(x=1600, y=620)
    def close():
        new2.destroy()
        global abc   #added for multiusage after entering to the program this variables should be reset 
        global abc1
        abc=""
        abc1=""
    #    # new2.quit()

    Button(new2, text= "Close the Window",bg='yellow',fg='red', font=("Calibri",16,"bold"),relief=RAISED, command=close).place(x=1680,y=1015)

    def clear_all():
        for item in tree3.get_children():
            tree3.delete(item)
    def clear_all2():
        for item in tree4.get_children():
            tree4.delete(item)        

    def my_show(*args): ##showing the selected option
        str_out.set(team1t.get())

    def my_show2(*args): ##showing the selected option
        str_out2.set(team2t.get())


    def login_clicked(*args):
        global abc
        abc=team1t.get().upper()
        global count1
        count1=0
        clear_all()
        teamData[""]={"":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":""}

        if abc == "":
            global l5
            global l3
            global l10
            global l9
            l3 = Label(new2,  text=mistake, width=40 ) 
            l9 = Label(new2,  text=correct, width=40 ) 
            l10=Label(new2, width=400,image=testimage )
            # correct3="Please Fill the Blank"
            print(correct3)
            l5 = Label(new2,  text=correct3, width=53 ) 
            l5.place(x=750, y=20)
            l10.destroy()
            l9.destroy()
            l3.destroy()
            l100.destroy()
        else:

            
            if abc in teamData:
                # clear_all()
                l100.destroy()
                l10.destroy()
                if abc==abc1:

                    # correct="Team 1: You entered same teams, please change one of them!"
                    print(correctt1)
                    l9 = Label(new2,  text=correctt1,bg="darkviolet",fg="black", width=53 ) 
                    l10=Label(new2, width=350,image=testimage ) 
                    l10.place(x=780, y=100)
                    l9.place(x=750, y=20)
                    l100.destroy()
                    l5.destroy()
                    l6.destroy()
                    l3.destroy()
                else:
                    data_selectedteam1=list((teamData.get(abc)).values())
                    data_selectedteam1.pop(0)
                    data_selectedteam1.pop(0)
                    correct2="Team 1: GOOOD, Let me Retrieve the Stats for you"
                    print(correct2)
                    l33 = Label(new2,  text=correct2,bg="lime",fg="black", width=53 ) 
                    l33.place(x=750, y=20) 
                    l12=Label(new2, width=300,image=dict_im[abc]) 
                    l12.place(x=100, y=710)
                    # tree3.insert('', 'end', text="1", values=data_selectedteam1)
                    for record in data_selectedteam1:
                          
                        tree3.insert(parent='',index='end',text='',values=(data_selectedteam1[count1]))
                           
                        count1 += 1
                    # tree3.insert(parent='',index='1',iid = 'a1',text='',values=(data2[1][1]))
                    l100.destroy()
                    l10.destroy()
                    l5.destroy()
                    l6.destroy()
                    l9.destroy()
                    l3.destroy()
            else:
                # mistake="Wrong Team, Please Enter the Team again"
                # global l3
                print(mistake)
                l3 = Label(new2,  text=mistake,bg="red",fg="black", width=53 ) 
                l3.place(x=750, y=20)
                l100.destroy()
                l10.destroy()
                l5.destroy()
                # l6.destroy()
                l9.destroy()
    def login_clicked2(*args):
        global abc1
        abc1=team2t.get().upper()
        global count2
        count2=0
        clear_all2()
        teamData[""]={"":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":""}

        


        if abc1 == "":
            global l6
            global l99
            global l100
            global l4
            global l40
            l40 = Label(new2,  text=mistake, width=53 ) 
            l100=Label(new2, width=400,image=testimage )
            # l14=Label(new2, width=300,image=dict_im[abc1]) 
            # correct="Please Fill the Blank"
            l99 = Label(new2,  text=correct3, width=40 ) 
            l4 = Label(new2,  text=mistake, width=53 )
            print(correct3)
            l6 = Label(new2,  text=correct4, width=53 ) 
            l6.place(x=750, y=70) 
            # l5.destroy()
            l10.destroy()
            # l9.destroy()
            l99.destroy()
            l100.destroy()
            l40.destroy()
            # l14.destroy()
        else:

            if abc1 in teamData:
                l10.destroy()
                l100.destroy()
                if abc==abc1:
                    # global correct1
                    # correct="You entered same teams, please change one of them!"
                    print(correctt2)
                    # global l100
                    # global l99
                    l99 = Label(new2,  text=correctt2,bg="darkviolet",fg="black", width=53 ) 
                    l100=Label(new2, width=350,image=testimage ) 
                    l100.place(x=780, y=100) 
                    l99.place(x=750, y=70) 
                    l10.destroy()
                    # l5.destroy()
                    l6.destroy()
                    # l9.destroy()
                    l4.destroy()
                    l40.destroy()
                else:
                    # global l14
                    l99.destroy()
                    data_selectedteam2=list((teamData.get(abc1)).values())
                    data_selectedteam2.pop(0)
                    data_selectedteam2.pop(0)
                    correct1="Team 2: GOOOD, Let me Retrieve the Stats for you"
                    print(correct1)
                    l44 = Label(new2,  text=correct1,bg="lime",fg="black", width=53 ) 
                    l44.place(x=750, y=70)
                    l14=Label(new2, width=300,image=dict_im[abc1]) 
                    l14.place(x=1400, y=710)
                    for record in data_selectedteam2:
                          
                        tree4.insert(parent='',index='end',text='',values=(data_selectedteam2[count2]))
                        # tree4.tag_configure('1', background="yellow")                       
                        count2 += 1
                    l10.destroy()
                    l100.destroy()
                    # l5.destroy()
                    l6.destroy()
                    # l9.destroy()
                    l4.destroy()
                    l40.destroy()
            else:
                l99.destroy()
                # mistake="Wrong Team, Please Enter the Team again"
                print(mistake)
                l40 = Label(new2,  text=mistake1,bg="red",fg="black", width=53 ) 
                l40.place(x=750, y=70)  
                l10.destroy()
                l100.destroy()
                l6.destroy()
                # l9.destroy()
                l4.destroy()
                # l14.destroy()

    team1t.trace('w',my_show)
    team2t.trace('w',my_show2)
    # T = Text(new2,height = 5, width = 52)

    # l2 = Label(new2,  textvariable=str_out, width=40 ) 
    # l2.place(x=500, y=400)
    s22 = ttk.Style()
    # s22.configure('Treeview', rowheight=22,font=('Comic Sans MS', 11),borderwidth= 0,background="green", 
      # foreground="white", fieldbackground="red")
    # ttk.Style().configure("Treeview", background="#383838", 
    #  foreground="white", fieldbackground="red")
    s22.theme_use("clam") 
    s22.configure("mystyle.Treeview", rowheight=24, highlightthickness=0,background="Dark Blue",foreground="white", 
                    fieldbackground="red", bd=0, font=('Comic Sans MS', 12))# Modify the font of the body
    s22.configure("mystyle.Treeview.Heading",background="blue", foreground="white", font=('Comic Sans MS', 13,'bold')) # Modify the font of the headings
    s22.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    # s22.map('mysteyle.Treeview', background=[('alternate', '#BFBFBF')], foreground=[('alternate', 'black')])
    # s2=ttk.Style()
    # s2.configure('Treeview', rowheight=22,font=('Comic Sans MS', 11),borderwidth= 0,background="green", 
     # foreground="white", fieldbackground="red")
    # s2.configure('Treeview.Heading',font=('Comic Sans MS', 12,'bold'))
    s22.map('Treeview',background=[('disabled',"green")],foreground=[('disabled',"green")])
    # s2.theme_use("clam")

    # s3=ttk.Style()
    # s3.configure('Treeview', rowheight=22,font=('Comic Sans MS', 11),borderwidth= 0)
    # s3.configure('Treeview.Heading',font=('Comic Sans MS', 12,'bold'))
    # s3.theme_use("vista")
    tree3=ttk.Treeview(new2, column=('AVGTeam1'), show='headings', height=22,style='mystyle.Treeview')
    tree3.column("#0", width=0,anchor=CENTER,  stretch=YES)
    tree3.column("AVGTeam1",anchor=CENTER, width=160,stretch=YES)

    # tree3.column("AVG Team 2", width=120,stretch=YES)
    tree3.heading("#0",anchor=CENTER,text="")
    tree3.heading("AVGTeam1",anchor=CENTER,text="AVG Team 1")
    # tree3.heading("AVG Team 2",text="AVG Team 2")
    tree3.place(x=590, y=100)
    tree4=ttk.Treeview(new2, column=( 'AVGTeam2'), show='headings', height=22,style='mystyle.Treeview')
    tree4.column("#0", width=0,anchor=CENTER,  stretch=YES)
    # tree4.column("AVG Team 1", width=120,stretch=YES)
    tree4.column("AVGTeam2",anchor=CENTER, width=160,stretch=YES)
    tree4.heading("#0",anchor=CENTER,text="")
    # tree4.heading("AVG Team 1",text="AVG Team 1")
    tree4.heading("AVGTeam2",anchor=CENTER,text="AVG Team 2")
    tree4.place(x=1170, y=100)

    # tree2 = ttk.Treeview(new2)
    # tree2.pack()
    tree2=ttk.Treeview(new2, column=('OnlyStats','NBA Average'), show='headings', height=22,style='mystyle.Treeview')
    # s2.configure(tree2,height=20)
    # tree2['columns']= ('Stat Name', 'AVG Team 1', 'AVG Team 2')
    tree2.column("#0", width=0,  stretch=YES)
    tree2.column('OnlyStats',anchor=CENTER, width=160,stretch=YES)
    tree2.column("NBA Average",anchor=CENTER, width=160,stretch=YES)
    # tree2.column("AVG Team 2",anchor=CENTER, width=120,stretch=YES)
    # tree2.column("award",anchor=CENTER, width=80)

    tree2.heading("#0",text="",anchor=CENTER)
    tree2.heading('OnlyStats',text="Stat Name",anchor=CENTER)
    tree2.heading("NBA Average",text="NBA Average",anchor=CENTER)
    # tree2.heading("AVG Team 2",text="AVG Team 2",anchor=CENTER)
    tree2.place(x=800, y=100)
    # tree2.tag_configure('odd', background='#E8E8E8')
    # tree2.tag_configure('even', background='#DFDFDF')

    # tree2.heading("award",text="Award",anchor=CENTER)



    login_button = Button(new2,bg='blue',fg='white', text="Click",font=("Calibri",14,"bold"), command=login_clicked)
    login_button.place(x=325,y=630)
    # login_button.pack()
    login_button2 = Button(new2,bg='blue',fg='white', text="Click",font=("Calibri",14,"bold"), command=login_clicked2)
    login_button2.place(x=1532,y=630)
    l8 = Label(new2,fg='darkorange',bg='teal',  text='ABBREVIATIONS \n ATL-Atlanta Hawks BOS-Boston Celtics \n CHA-Charlotte Hornets \
            CHI-Chicago Bulls \n CLE-Cleveland Cavaliers  DAL-Dallas Mavericks \n DEN-Denver Nuggets  \
            DET-Detroit Pistons \n GSW-Golden State Warriors  HOU-Houston Rockets \n IND-Indiana Pacers LAC-Los Angeles Clippers\n \
            LAL-Los Angeles Lakers MEM-Memphis Grizzlies\n MIA-Miami Heat MIL-Milwaukee Bucks \n  MIN-Minnesota Timberwolves NOH-New Orleans Pelicans\n \
            NYK-New York Knicks BKN-Brooklyn Nets\n OKC-Oklahoma City Thunder ORL-Orlando Magic \n PHI-Philadelphia 76ers PHO-Phoenix Suns\n \
            POR-Portland Trail Blazers SAC-Sacramento Kings \n SAS-San Antonio Spurs TOR-Toronto Raptors \n \
            UTH-Utah Jazz WAS-Washington Wizards',borderwidth=10,relief="solid", width=50 ) 
    l8.place(x=770, y=730) 
    data=list(teamData['ATL'].keys())
    data_nba=list(teamData['NBA'].values())
    data_nba.remove('0F')
    data_nba.remove('0F')
    data.remove('G')
    # data.remove('Team/G')
    data.remove('Unnamed: 0')
    global count
    count=0

    # data2  = [
    #     [1,"Jack","gold"],
    #     [2,"Tom","Bronze"]

    # ]
    for record in data:
          
        tree2.insert(parent='',index='end',iid = count,text='',values=(data[count],data_nba[count]))
           
        count += 1
    new2.config(bg='teal')
    new2.attributes('-fullscreen', True)



def game_probability(home_team, away_team):

    # teams = getRecord()

    home = record_team.get(home_team)

    away = record_team.get(away_team)

    home_total_games = home['Home Wins'] + home['Home Losses']

    away_total_games = away['Away Wins'] + away['Away Losses']

    home_win_perc = home['Home Wins'] / home_total_games

    away_win_perc = away['Away Wins'] / away_total_games

    home_total_win_perc = home['Wins'] / (home['Wins'] + home['Losses'])

    away_total_win_perc = away['Wins'] / (away['Wins'] + away['Losses'])

    home_streak_perc = home['Streak Wins'] / (home['Streak Wins'] + home['Streak Losses'])

    away_streak_perc = away['Streak Wins'] / (away['Streak Wins'] + away['Streak Losses'])



    return 0.6 * prob_helper(home_win_perc, away_win_perc) + 0.3 * prob_helper(home_total_win_perc, away_total_win_perc) + 0.1 * prob_helper(home_streak_perc, away_streak_perc)


    
    




def perform_series(window, inputtxt, team1, team2, label1, label2, label3):
    team_1 = team1.get()
    team_2 = team2.get()
    if team_1 == team_2:
        label1.config(text = "Error: Can't have same team facing each other")
        label2.config(text = "")
        label3.config(text = "")
        return
    inp = inputtxt.get(1.0, END)
    if int(inp) > 0 and int(inp) % 2 == 1:
        team_1 = team1.get()
        team_2 = team2.get()
        if team_1 == team2:
            label1.config(text = "Error: Can't have same team facing each other")
            label2.config(text = "")
            label3.config(text = "")
        else: 
            predictor = game_probability(team_1, team_2)
            predictor = round(predictor, 3)
            predictor = predictor * 100
            label1.config(text= str(team_1) + " faces off against " + str(team_2) + "!")
            winner = sim_game(team_1, team_2, int(inp))

            series = winner[2]
            series_seq = ""
            game_num = 1
            for i in series:
                if game_num == len(series):
                    series_seq = series_seq + str(i) + " wins game " + str(game_num)
                    game_num += 1
                else:
                    series_seq = series_seq + str(i) + " wins game " + str(game_num) + ", "
                    game_num += 1
            result = str(team_1) + " has a " + str(predictor) + " percent chance of winning a game."
            series_winner = str(winner[0]) + " wins the series in " + str(winner[1]) + " games!"
            label1.config(text = result,foreground='orange',background='black')
            label2.config(text = series_seq,foreground='orange',background='black')
            label3.config(text = series_winner,foreground='orange',background='black')
    else:
        label1.config(text = "Series length must be odd number and greater than 0")
        label2.config(text = "")
        label3.config(text = "")
def prob_helper(perc1, perc2):

    return (perc1 - (perc1 * perc2)) / (perc1 + (perc2 - (2 * perc1 * perc2)))

def sim_game(team_1, team_2, series_len):

    series_games = []

    win_perc = game_probability(team_1, team_2)

    series_threshold = series_len / 2

    series = [0, 0]

    num_games = 0

    for i in range(series_len):

        game = random.uniform(0.0, 1.0)

        if game <= win_perc:

            series[0] += 1

            series_games.append(team_1)

            print(team_1 + ' wins game ' + str(i + 1))

            if(series[0] > series_threshold):
                
                num_games = i + 1

                break

        else:

            series[1] += 1

            series_games.append(team_2)

            print(team_2 + ' wins game ' + str(i + 1))

            if(series[1] > series_threshold):

                num_games = i + 1

                break

    if series[0] > series[1]:

        return team_1, num_games, series_games

    else:

        return team_2, num_games, series_games


def perform_predic(window, team1, team2, button):
    
    tk.Label(window, text='Enter number of games for series',fg='red', font=("Helvetica", 15)).pack(padx=10, pady=10)
    inputtxt = tk.Text(window, width= 5, height=1)
    label1 = ttk.Label(window, text="")
    label2 = ttk.Label(window, text="", wraplengt=400)
    label3 = ttk.Label(window, text="")
    printButton = tk.Button(window,
        text = "Simulate Series",fg='darkgreen',bg='cyan' ,
        command= lambda: perform_series(window, inputtxt, team1, team2, label1, label2, label3))
    inputtxt.pack()
    printButton.pack()
    label1.pack(padx=10, pady=10)
    label2.pack(padx=10, pady=10)
    label3.pack(padx=10, pady=10)
    label1.config(text= "It's gametime!",foreground="GREEN")
    button.pack_forget()
    
    
def open_predic():
    new3= Toplevel(window)
    #img = PhotoImage(file="NBA-Player-PNG-Picture.png")

    #new = Canvas(window, width=700, height=3500)
    #new.pack(fill=BOTH, expand=True)
    #new.create_image(0, 0, image=img, anchor='nw')
    #img = PhotoImage(file="download.jpg")
    background_label = tk.Label(new3, image=img2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    new3.geometry("750x600")
    new3.title("")

    # team_list = ['ATL', 'BOS', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'BRK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']
    team_list = list_teamnames
    variable11 = StringVar(new3)
    variable11.set(team_list[0])
    variable22 = StringVar(new3)
    variable22.set(team_list[0])

    team_1 = OptionMenu(new3, variable11, *team_list)
    team_1.pack()
    team_2 = OptionMenu(new3, variable22, *team_list)
    team_2.pack()
    team_1.config(bg = "GREEN")
    team_1["menu"].config(bg="BLUE")
    team_2.config(bg = "MAGENTA")
    team_2["menu"].config(bg="RED")
    # inputtxt = tk.Text(new, width= 10, height=1)
    printButton = tk.Button(new3,
        text = "Simulate", 
        command= lambda: perform_predic(new3,variable11, variable22, printButton))
    #inputtxt.pack()
    printButton.pack()
    
btn_statsnew=Button(window, text="Records_OpenButton", command=open_win_records, fg='orange',bg='black',font=("Helvetica",25))
btn_statsnew.place(x=650, y=800) 

btn_statcomp=Button(window, text="Stats_Comparison", command=open_win_compstats, fg='orange',bg='blue',font=("Helvetica",25))
btn_statcomp.place(x=1250, y=800) 

btn_predictor = Button(window, text= "Game Predictor", command= open_predic ,fg='purple',bg='magenta',font=("Helvetica", 25))
btn_predictor.place(x = 150, y=800)

#naming the buttons
lbl=Label(window, text="NBA Game Prediction and Statistics", fg='red', font=("Helvetica", 40))
lbl.place(x=60, y=50)

lbl=Label(window, text="D.O.G", fg='red', font=("Helvetica", 40))
lbl.place(x=1600, y=50)


def closefull():
    window.destroy()
exitbutton=Button(window, text= "Want to Leave :(", font=("Helvetica",15,"bold"),fg='white',bg='red', command=closefull)
exitbutton.place(x=1700,y=900)


#user input part
# txtfld=Entry(window, text="This is Entry Widget", bd=5)
# txtfld.place(x=80, y=150)


window.title('DOG - NBA Prediction - Statistics Program')
window.geometry("1500x900")
# window.config(bg='yellow')
window.mainloop()




