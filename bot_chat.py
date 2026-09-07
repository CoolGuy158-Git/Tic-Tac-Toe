import tkinter as tk


def chat(root):
    app = tk.Toplevel(root)
    app.overrideredirect(True)
    app.title("Tic ta chat")
    app.resizable(False, False)
    app.geometry("400x190")
    app.config(background="teal", relief="sunken", borderwidth=8)

    def clicked_win(event):
        app.drag_x = event.x
        app.drag_y = event.y
    def drag_win(event):
        x = app.winfo_x() + event.x - app.drag_x
        y = app.winfo_y() + event.y - app.drag_y
        app.geometry(f"+{x}+{y}")
    app.bind("<Button-1>", clicked_win)
    app.bind("<B1-Motion>", drag_win)
    GUY = tk.Label(app, background="black", relief="raised", borderwidth=8, foreground="green", font=("Arial", 50), width=100)
    GUY.pack(pady=(10, 3), padx=10)

    GUY_chat = tk.Label(app, background="black", relief="raised", borderwidth=8, foreground="green", font=("Arial", 16), width=100, wraplength=350)
    GUY_chat.pack(pady=(0, 10), padx=10)
    GUY_chat.lift()
    def start():
        GUY.config(text="৻(  •̀ ᗜ •́  ৻)")
        GUY_chat.config(text="Hah-, SO YOU CHOOSE TO FIGHT ME?! YOU MORTAL!")

    def blocked():
        GUY.config(text="৻(  •̀ ᗜ •́  ৻)")
        GUY_chat.config(text="Haha, close. But I blocked you!")

    def win():
        GUY.config(text="( ˶ˆᗜˆ˵ )")
        GUY_chat.config(text="Yay, I WIN! BETTER LUCK NEXT TIME HUMAN!")

    def lose():
        GUY.config(text="(╥﹏╥)")
        GUY_chat.config(text="NOOOO... HOW DID I LOSE?! TO YOU???")

    def draw():
        GUY.config(text="( •́ ᴖ •̀ )")
        GUY_chat.config(text="A draw?! That's not very satisfying...")
    def confident():
        GUY.config(text="(¬‿¬)")
        GUY_chat.config(text="Hehe. I already know what you're gonna do.")
    def taunt():
        GUY.config(text="(≖ ͜ʖ≖)")
        GUY_chat.config(text="Is that really the best move you got?")
    def easy():
        GUY.config(text="(￣へ￣)")
        GUY_chat.config(text="FINEEEE- I'll take it easy on you!")
    def best():
        GUY.config(text="(¬‿¬ )")
        GUY_chat.config(text="If I place it here, THEN VICTORY IS GUARANTEED!")
    return app, blocked, win, lose, draw, confident, taunt, start, easy, best