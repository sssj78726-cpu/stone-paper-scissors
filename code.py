import tkinter as tk
import random as ra
import sqlite3

win_streak = 0

conn = sqlite3.connect('srs.db') # your file
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sps
(win_streak INTEGER)''')
conn.commit()


def play(user):
        global win_streak
        options = ['stone','paper','scissors']
        computer = ra.choice(options)

        if computer == user:
            result = 'draw'

        elif (user == 'paper' and computer == 'stone') or \
         (user == 'stone' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper'):
            result = 'win'
            win_streak += 1
            cursor.execute("UPDATE sps SET win_streak = ?",(win_streak,))
            conn.commit()
        else:
            result = 'lose'
            win_streak = 0
            cursor.execute("UPDATE sps SET win_streak = ? ",(win_streak,))
            conn.commit()
        label_a.config(text =f'computer: {computer}, you {result}' )


root = tk.Tk()
root.title('STONE-PAPER-SCISSORS')
root.geometry('500x400')


label = tk.Label(root,text = 'WELKOME TO STONE-PAPER-SCISSORS')
label.pack()

label_a = tk.Label(root,text = '')
label_a.pack()

label_ws = tk.Label(root,text= f'win_streak ={win_streak}')
label_ws.pack() # not change but i fix that

btn1 = tk.Button(root,text = 'paper',command= lambda: play('paper'))
btn1.pack()

btn2 = tk.Button(root,text = ' stone',command= lambda : play('stone'))
btn2.pack()

btn3 = tk.Button(root,text = 'scissors',command= lambda : play("scisors"))
btn3.pack()



root.mainloop()
conn.close()
