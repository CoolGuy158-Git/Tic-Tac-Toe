import tkinter as tk
from tkinter import messagebox
from bot import bot
import winsound
import time
import threading
import bot_chat

def laugh():
    winsound.Beep(380, 600)
    time.sleep(0.08)
    for freq in [550, 700, 900, 1150, 1400]:
        winsound.Beep(freq, 80)
        time.sleep(0.04)
    time.sleep(0.15)
    winsound.Beep(300, 700)

chat_window = None
mode = "human"
blocked = confident = win = lose = draw = taunt = easy = start = None
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")
root.resizable(False, False)
root.configure(background="teal", cursor="circle", relief="sunken", borderwidth=8)

button_a1 = tk.Button(root, text="", background="black", foreground="green", font=("Arial", 30), activebackground="gray", relief="raised", borderwidth=8, command=lambda:pressed(button_a1))
button_a2 = tk.Button(root, text="", background="black", foreground="green", font=("Arial", 30),activebackground="gray", relief="raised", borderwidth=8, command=lambda:pressed(button_a2))
button_a3 = tk.Button(root, text="", background="black", foreground="green", font=("Arial", 30),activebackground="gray", relief="raised", borderwidth=8, command=lambda:pressed(button_a3))

button_b1 = tk.Button(root, text="", background="black", foreground="green", font=("Arial", 30),activebackground="gray", relief="raised", borderwidth=8, command=lambda:pressed(button_b1))
button_b2 = tk.Button(root, text="", background="black", foreground="green", font=("Arial", 30),activebackground="gray", relief="raised", borderwidth=8, command=lambda:pressed(button_b2))
button_b3 = tk.Button(root, text="", background="black", foreground="green", font=("Arial", 30),activebackground="gray", relief="raised", borderwidth=8, command=lambda:pressed(button_b3))

button_c1 = tk.Button(root, text="", background="black", foreground="green", font=("Arial", 30),activebackground="gray", relief="raised", borderwidth=8, command=lambda:pressed(button_c1))
button_c2 = tk.Button(root, text="", background="black", foreground="green", font=("Arial", 30),activebackground="gray", relief="raised", borderwidth=8, command=lambda:pressed(button_c2))
button_c3 = tk.Button(root, text="", background="black", foreground="green", font=("Arial", 30),activebackground="gray", relief="raised", borderwidth=8, command=lambda:pressed(button_c3))

buttons = [button_a1,button_a2,button_a3,button_b1,button_b2,button_b3,button_c1,button_c2,button_c3,]

for i, button in enumerate(buttons):
    row = i // 3
    col = i % 3

    button.place(x=23 + col * 82,y=23 + row * 82,width=80,height=80)

player_1_turn = True
def check_change_curse():
    if player_1_turn:
        root.configure(cursor="circle")
    else:
        root.configure(cursor="X_cursor")
    root.after(100, check_change_curse)
root.after(0, check_change_curse)
def check_win():
    ### Winning conditions
    # Player 1
    # Ik this is sooo long and ik there's a better way buttt what it does is
    # It checks if all like a1, a2, a3 or b1,b2, b3, or c1, c2, c3 are occupied or the vertical a1, b1, c1, etc. and the like \/ yea a1, b2, and c3 etc. and if any those rules are meet then win!
    if button_a1["text"] == "O" and button_a2["text"] == "O" and button_a3["text"] == "O" or button_b1[
        "text"] == "O" and button_b2["text"] == "O" and button_b3["text"] == "O" or button_c1["text"] == "O" and \
            button_c2["text"] == "O" and button_c3["text"] == "O" or button_a1["text"] == "O" and button_b1[
        "text"] == "O" and button_c1["text"] == "O" or button_a2["text"] == "O" and button_b2["text"] == "O" and \
            button_c2["text"] == "O" or button_a3["text"] == "O" and button_b3["text"] == "O" and button_c3[
        "text"] == "O" or button_a1["text"] == "O" and button_b2["text"] == "O" and button_c3["text"] == "O" or \
            button_a3["text"] == "O" and button_b2["text"] == "O" and button_c1["text"] == "O":
        messagebox.showinfo("Tic Tac Toe", "Player 1 has won!")
        print("Player 1 has won!")
        if mode == "bot":
            lose()
        clear()
    # Player 2
    # Same thing here
    elif button_a1["text"] == "X" and button_a2["text"] == "X" and button_a3["text"] == "X" or button_b1[
        "text"] == "X" and button_b2["text"] == "X" and button_b3["text"] == "X" or button_c1["text"] == "X" and \
            button_c2["text"] == "X" and button_c3["text"] == "X" or button_a1["text"] == "X" and button_b1[
        "text"] == "X" and button_c1["text"] == "X" or button_a2["text"] == "X" and button_b2["text"] == "X" and \
            button_c2["text"] == "X" or button_a3["text"] == "X" and button_b3["text"] == "X" and button_c3[
        "text"] == "X" or button_a1["text"] == "X" and button_b2["text"] == "X" and button_c3["text"] == "X" or \
            button_a3["text"] == "X" and button_b2["text"] == "X" and button_c1["text"] == "X":
        if mode == "bot":
            messagebox.showinfo("Tic Tac Toe", "Player 2 (CPU) has won!")
            threading.Thread(target=laugh).start()
            win()
        else:
            messagebox.showinfo("Tic Tac Toe", "Player 2 has won!")
        print("Player 2 has won!")
        clear()
    # Draw
    # If all the buttons are occupied but none of the other 2 conditions are meet yet then draw.
    elif all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        print("It's a draw!")
        if mode == "bot":
            draw()
        clear()
taunt_time = None
def pressed(button=None):
    global player_1_turn, taunt_time
    if taunt_time:
        root.after_cancel(taunt_time)
    taunt_time = root.after(5000, taunt)
    if None != button:
        if player_1_turn:
            button.configure(text="O")
            button.configure(state="disabled", disabledforeground="green")
            player_1_turn = False
            if mode == "bot":
                bot(buttons=buttons, player_1_turn=player_1_turn, diff=diff, button_pos=f"[{button_a1['text']}], [{button_a2['text']}], [{button_a3['text']}]\n[{button_b1['text']}], [{button_b2['text']}], [{button_b3['text']}]\n[{button_c1['text']}], [{button_c2['text']}], [{button_c3['text']}]\n", bot_chat=bot_chat)
                player_1_turn = True
        else:
            if mode == "human":
                button.configure(text="X")
                button.configure(state="disabled", disabledforeground="green")
                player_1_turn = True
            else:
                button.configure(text="X")
                button.configure(state="disabled", disabledforeground="green")
                player_1_turn = True
    check_win()
    print("[{button_a1['text']}], [{button_a2['text']}], [{button_a3['text']}]\n[{button_b1['text']}], [{button_b2['text']}], [{button_b3['text']}]\n[{button_c1['text']}], [{button_c2['text']}], [{button_c3['text']}]\n")

def clear():
    global score1, score2
    global player_1_turn
    for button in buttons:
        button.configure(text="")
        button.configure(state="normal")
    player_1_turn = True
    print("New Game!")
next_mode = "bot"
diff = "hard"
def switch_diff():
    global diff
    old_label = f"Difficulty: {diff} |"

    if diff == "hard":
        diff = "easy"
        easy()
    else:
        diff = "hard"
        start()
    menu.entryconfigure(old_label, label=f"Difficulty: {diff} |")
def switch_mode(): # You probably have no friends sooo BOT MODE!
    global next_mode, mode, chat_window, blocked, win, lose, draw, confident, taunt, easy, start
    if next_mode == "bot":
        next_mode = "player"
        mode = "bot"
        chat_window, blocked, win, lose, draw, confident, taunt, start, easy, best = bot_chat.chat(root)
        bot_chat.blocked = blocked
        bot_chat.confident = confident
        bot_chat.best = best
        start()
        menu.entryconfigure(menu.index(f"Difficulty: {diff} |"),state="normal")
        clear()
    elif next_mode == "player":
        next_mode = "bot"
        mode = "human"
        if chat_window:
            chat_window.destroy()
            chat_window = None
        menu.entryconfigure(menu.index(f"Difficulty: {diff} |"),state="disabled")
        clear()
    menu.entryconfigure(menu.index(f"Play with a {'bot' if next_mode == 'player' else 'player'} |"),label=f"Play with a {next_mode} |")
menu = tk.Menu(root)
root.config(menu=menu)
menu.add_command(label="Clear |", command=clear)
menu.add_command(label=f"Play with a {next_mode} |", command=switch_mode)
menu.add_command(label=f"Difficulty: {diff} |", command=switch_diff)
root.mainloop()