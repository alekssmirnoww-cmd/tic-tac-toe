import tkinter as tk
from tkinter import messagebox

tic = tk.Tk()
tic.title("tic-tac-toe")




click_count = 0

def click(btn):
    global click_count
    if btn["text"] != "":
        return
    click_count +=1
    if click_count % 2 !=0:
        player = "X"
    else:
        player = "O"
    btn.config(text=player)
    if checkwin():
        return
    if click_count == 9:
        messagebox.showinfo("Game Over", "TIE")
        reset_board()

def checkwin():
    for i in range(3):
        if buttons[i][0]["text"]==buttons[i][1]["text"]==buttons[i][2]["text"]!= "":
            announcewinner(buttons[i][0]["text"])
            return True
        if buttons[0][i]["text"]==buttons[1][i]["text"]==buttons[2][i]["text"]!= "":
            announcewinner(buttons[0][i]["text"])
            return True
    if buttons[0][0]["text"]==buttons[1][1]["text"]==buttons[2][2]["text"]!= "":
        announcewinner(buttons[0][0]["text"])
        return True
    if buttons[0][2]["text"]==buttons[1][1]["text"]==buttons[2][0]["text"]!= "":
        announcewinner(buttons[0][2]["text"])
        return True
    return False
def announcewinner(winner):
    messagebox.showinfo("Game Over", f"Player {winner} wins!")
    reset_board()

def reset_board():
    global click_count
    click_count=0
    for row in buttons:
        for btn in row:
            btn.config(text="")

buttons =[]
for r in range(3):
    row_list=[]
    for c in range(3):
        btn = tk.Button(tic, text="")
        btn.grid(row=r, column=c)
        btn.config(command=lambda b=btn :click(b))
        row_list.append(btn)
    buttons.append(row_list)


tic.mainloop()