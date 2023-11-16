from tkinter import *
import random
import pygame

pygame.init()

def next_turn(row, colomn):
    global player
    if not check_winner():
        play_click_sound()
    if buttons[row][colomn]['text'] == "" and not check_winner():
        if player == players[0]:
            buttons[row][colomn]['text'] = player

            if not check_winner():
                player = players[1]
                label.config(text=f"{player} turn")
            elif check_winner() is True:
                label.config(text=(players[0] + "  Wins!!!"))
            else:
                label.config(text=("Tie!!!"))
        else:
            buttons[row][colomn]['text'] = player
            if not check_winner():
                player = players[0]
                label.config(text=f"{player} turn")
            elif check_winner() is True:
                label.config(text=(players[1] + "  Wins!!!"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!!!"))


def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[2][0]["text"] == buttons[1][1]["text"] == buttons[0][2]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    return False


def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
                return True

    return False

def on_enter(event):
    if not check_winner() or check_winner() == "Tie":
        event.widget.config(bg="lightblue")

def on_leave(event):
    if not check_winner() or check_winner() == "Tie":
        event.widget.config(bg="#F0F0F0")
def play_click_sound():
    pygame.mixer.Sound("click_sound.wav").play()
def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player} turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Beautiful Tic Tac Toe")
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
y = int((screen_height / 2) - (WINDOW_HEIGHT / 2))

window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, x, y))
window.config(bg="lightgray")


players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
label = Label(text=f"{player} turn", font=("Helvetica", 24))
label.config(bg="lightgray", fg="darkblue")
label.pack(side="top")

reset_button = Button(window, text="New Game!!!", font=("Helvetica", 16), command=new_game, bg="blue", fg="white")
reset_button.config(bg="green", fg="white")
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()


button_style = {"font": ("Arial", 20), "width": 5, "height": 2, "relief": "ridge", "borderwidth": 2}
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",command=lambda row=row, column=column: next_turn(row, column),
                                      **button_style)
        buttons[row][column].grid(row=row, column=column, padx=5, pady=5)
        buttons[row][column].bind("<Enter>", on_enter)
        buttons[row][column].bind("<Leave>", on_leave)

window.mainloop()
