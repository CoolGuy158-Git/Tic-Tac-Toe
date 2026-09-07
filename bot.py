import random

def predict_move(button_pos, bot_chat):
    """
    This function is used to predict the next BEST move of the player.
    It then finds where the best spot to place an X is to prevent that player moves.
    How?
    It starts by creating an imaginary board.
    Then it places an O on every empty spot on the board.
    Basically that could be the player's next move.
    Then it thinks.
    'If the player moves here, will it win the next move?' (It uses the same thing that func bot uses to determine if that's winning)
    If so, it places an X to that.
    Say you have.
      1 2 3
    A [][][O]
    B [][][]
    C [][][]
    The bot knows that if player places on B3 it is one move away from winning,
    so it places it on C3
    so final board will look like
      1 2 3
    A [][][O]
    B [][][]
    C [][][X]
    """
    imaginary_board = button_pos.replace("[", "").replace("]", "").replace("\n", ",").replace(" ", "").split(",")
    print("\n*---Predictor Log---*")
    print("OG Board")
    print(imaginary_board)
    rounds = 0
    for i, space in enumerate(imaginary_board):
        if space == "":
            rounds += 1
            imaginary_board[i] = "O"
            print(f"Possible move #{rounds}")
            print(imaginary_board)
            wins = [
                (0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)
            ]
            for a,b,c in wins:
                if imaginary_board[a] == "O" and imaginary_board[b] == "O" and imaginary_board[c] == "":
                    print("Best move for player 1 is C")
                    bot_chat.confident()
                    print("\n*-------E-N-D-------*")
                    return c
                elif imaginary_board[a] == "O" and imaginary_board[c] == "O" and imaginary_board[b] == "":
                    print("Best move for player 1 is B")
                    bot_chat.confident()
                    print("\n*-------E-N-D-------*")
                    return b
                elif imaginary_board[b] == "O" and imaginary_board[c] == "O" and imaginary_board[a] == "":
                    print("Best move for player 1 is A")
                    bot_chat.confident()
                    print("\n*-------E-N-D-------*")
                    return a
            imaginary_board[i] = ""
    print("No best move for player 1")
    print("\n*-------E-N-D-------*")
    return None

def predict_your_move(button_pos, bot_chat):
    """
    This function is used to predict the next BEST move of the YOURSELF.
    It finds the best spot to place an X to make sure that the next move is winning.
    How?
    It starts by creating an imaginary board.
    Then it places an X on every empty spot on the board.
    Basically that could be the player's next move.
    Then it thinks.
    'If I move here, will I win the next move?' (It uses the same thing that func bot uses to determine if that's winning)
    If so, it places an X to that.
    Say you have.
      1 2 3
    A [][][X]
    B [][][]
    C [][][]
    The bot knows that if it places on B3 it is one move away from winning,
    so it places it on C3
    so final board will look like
      1 2 3
    A [][][X]
    B [][][]
    C [][][X]
    """
    imaginary_board = button_pos.replace("[", "").replace("]", "").replace("\n", ",").replace(" ", "").split(",")
    print("\n*---Predictor Log---*")
    print("OG Board")
    print(imaginary_board)
    rounds = 0
    for i, space in enumerate(imaginary_board):
        if space == "":
            rounds += 1
            imaginary_board[i] = "X"
            print(f"Possible move #{rounds}")
            print(imaginary_board)
            wins = [
                (0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)
            ]
            for a,b,c in wins:
                if imaginary_board[a] == "X" and imaginary_board[b] == "X" and imaginary_board[c] == "":
                    print("Best move for player 2 is C")
                    bot_chat.best()
                    print("\n*-------E-N-D-------*")
                    return c
                elif imaginary_board[a] == "X" and imaginary_board[c] == "X" and imaginary_board[b] == "":
                    print("Best move for player 2 is B")
                    bot_chat.best()
                    print("\n*-------E-N-D-------*")
                    return b
                elif imaginary_board[b] == "X" and imaginary_board[c] == "X" and imaginary_board[a] == "":
                    print("Best move for player 2 is A")
                    bot_chat.best()
                    print("\n*-------E-N-D-------*")
                    return a
            imaginary_board[i] = ""
    print("No best move for player 2")
    print("\n*-------E-N-D-------*")
    return None
def bot(buttons, player_1_turn, diff, button_pos, bot_chat):
    """
    This function is used to make a bot decision.
    In hard mode:
        It starts by seeing if there's a winning move, is so take it.
        Then it sees if there's a winning move for the player, if so block it.
        Then it runs the predict_move func.
        Then (This is also done in EASY mode)
        If center is available take it.
        If not randomly pick any empty spot on the board.
    """
    if all(button["text"] != "" for button in buttons):
        return
    if not player_1_turn:
        if diff == "hard":
            wins = [
                (0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)
            ]
            # If you're about to win TAKE IT!
            for a,b,c in wins:
                if buttons[a]["text"] == "X" and buttons[b]["text"] == "X" and buttons[c]["text"] == "":
                    buttons[c].invoke()
                    return
                elif buttons[a]["text"] == "X" and buttons[c]["text"] == "X" and buttons[b]["text"] == "":
                    buttons[b].invoke()
                    return
                elif buttons[b]["text"] == "X" and buttons[c]["text"] == "X" and buttons[a]["text"] == "":
                    buttons[a].invoke()
                    return
            # If player 1 is about to win TAKE ITS SPOT!
            for a,b,c in wins:
                if buttons[a]["text"] == "O" and buttons[b]["text"] == "O" and buttons[c]["text"] == "":
                    buttons[c].invoke()
                    bot_chat.blocked()
                    return
                elif buttons[a]["text"] == "O" and buttons[c]["text"] == "O" and buttons[b]["text"] == "":
                    buttons[b].invoke()
                    bot_chat.blocked()
                    return
                elif buttons[b]["text"] == "O" and buttons[c]["text"] == "O" and buttons[a]["text"] == "":
                    buttons[a].invoke()
                    bot_chat.blocked()
                    return
            your_predicted = predict_your_move(button_pos, bot_chat)

            if your_predicted is not None:
                buttons[your_predicted].invoke()
                return

            predicted = predict_move(button_pos, bot_chat)

            if predicted is not None:
                buttons[predicted].invoke()
                return
        while True:
            for button in buttons:
                # Else just pick center if N/A, randomly take any square
                if buttons[4]["text"] == "":
                    buttons[4].invoke()
                    return
                if button["text"] == "":
                    if random.choice([True, False]):
                        button.invoke()
                        return
                    else:
                        continue
