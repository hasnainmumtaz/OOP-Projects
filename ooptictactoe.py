

# library for the tic-tac-toe game
import tkinter as tk
import customtkinter as ctk
import os

player_one = True
game_status = True

class Box:
    def __init__(self, tttgame):
        self.status = True
        self.value = 0
        self.button = ctk.CTkButton(tttgame, text=" ",width=100,height=100,font=("Helvetica", 32),fg_color="grey",border_width= 5,border_color="black",corner_radius= 0,)
        self.button.configure(command=lambda: self.click())

    def click(self):
        global game_status
        global grid
        global player_one
        if game_status:
            if self.status:
                if player_one:
                    self.button.configure(text="X")
                    player_one = False
                    self.value = self.button.cget("text")
                    self.button.configure(fg_color="red4")
                else:
                    self.button.configure(text="O")
                    player_one = True
                    self.value = self.button.cget("text")
                    self.button.configure(fg_color="navy")

                self.status = False
                check_winner()
        else:
            #print("Game Over!")
            pass

def print_winner(x,y):
    global game_status
    game_status = False

    win_message = ctk.CTkLabel(ttt, text=f"{g_value(x,y)} is the Winner", font=("Helvetica", 32), fg_color="black", width=300, height=100)
    win_message.grid(row=1, column=0, columnspan=3)
    # print(f"{g_value(x,y)} is the Winner")
    # tk.messagebox.showinfo("Winner", f"{g_value(x,y)} is the Winner")

def g_value(x,y):
    return grid[x][y].value

def check_winner():
    global grid
    if g_value(0,0) == g_value(0,1) == g_value(0,2) != 0:
        print_winner(0,0)
    elif g_value(1,0) == g_value(1,1) == g_value(1,2) != 0:
        print_winner(1,0)
    elif g_value(2,0) == g_value(2,1) == g_value(2,2) != 0:
        print_winner(2,0)
    elif g_value(0,0) == g_value(1,0) == g_value(2,0) != 0:
        print_winner(0,0)
    elif g_value(0,1) == g_value(1,1) == g_value(2,1) != 0:
        print_winner(0,1)
    elif g_value(0,2) == g_value(1,2) == g_value(2,2) != 0:
        print_winner(0,2)
    elif g_value(0,0) == g_value(1,1) == g_value(2,2) != 0:
        print_winner(0,0)
    elif g_value(0,2) == g_value(1,1) == g_value(2,0) != 0:
        print_winner(0,2)
    else:
        #print("It's a tie!")
        pass

#define window_setup
def window_setup():
    window = ctk.CTk()
    window.title("Tic Tac Toe")
    window.geometry("300x350")
    window.resizable(False, False)

    return window

ttt = window_setup()

def populate_grid():
    grid = []
    for row in range(3):
        grid.append([])
        for col in range(3):
            box = Box(ttt)
            box.button.grid(row=row, column=col)
            grid[row].append(box)

    return grid

grid = populate_grid()  

def restart():
    ttt.destroy()
    os.system("python ooptictactoe.py")


restart_button = ctk.CTkButton(ttt, text="Restart",
                                 font=("Helvetica", 16),
                                    width=300,
                                    height=50,
                                  fg_color="black",
                                  border_width= 5,
                                  border_color="black",
                                  corner_radius= 0,
                                  hover_color="red",
                                    )
restart_button.configure(command=lambda: restart())
restart_button.grid(row=3, column=0, columnspan=3)



ttt.mainloop()