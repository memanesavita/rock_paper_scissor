

from tkinter import *
from random import randint, random
from tkinter import ttk
root=Tk()
root.title("my first window")

label=Label(root,font=("Arial",20),text="Game of Rock Paper Scissor",bg="yellow",fg="black")
label.pack()
root.geometry("800x900+300+150")
root.resizable(0,0)

rock=PhotoImage(file="stones.png")
paper=PhotoImage(file="index.png")
scissors=PhotoImage(file="paper.png")


image_list=[rock,paper,scissors]
pick_number =randint(0,2)

image_label=Label(root,image=image_list[pick_number])
image_label.pack(pady=20)


# # create spin funstion
def spin():
    pick_number=randint(0,2)
    image_label.config(image=image_list[pick_number])
    def win():
        print("you win")
    def lose():
        print("you lose")
    while True:
        player_choice=input("what you pick?(rock, paper,scissor:")
        player_choice.strip()
        random_move=randint(0,2)
        moves=["rock","paper","scissor"]
        computer_choice=moves[random_move]
        print(computer_choice)
        player_choice_value=randint[0,2]
        if player_choice== computer_choice:
            print()
        elif player_choice=="rock" or computer_choice=="scissors":
            win()
        elif player_choice=="paper " or computer_choice=="scissors":
            lose()
        elif player_choice=="scissors" or computer_choice=="paper":
            win()
        elif player_choice=="paper" or computer_choice=="rock":
            lose()
        elif player_choice=="rock" or computer_choice=="paper":
            win()
        again=input("do you want play again? (y or n").strip()
        if again=="n":
            break
        if player_choice_value==0:#rock
            if pick_number==0:
                win_lose_label.config(text="It's a Tie!,spin again...")
            elif pick_number==1:
                win_lose_label.config(text="paper cover rock!you lose...")
            elif pick_number==2:
                win_lose_label.config(text="rock smashes scissor!you win!!!")
            if player_choice_value==1:#paper
                if pick_number==1:
                    win_lose_label.config(text="It's a Tie!,spin again...")
            elif pick_number==0:
                win_lose_label.config(text="paper cover rock!you win!!!")
            elif pick_number==2:
                win_lose_label.config(text="scissor cut paper!you lose...")
            if player_choice_value==2:#scissor
                if pick_number==2:
                    win_lose_label.config(text="It's a Tie!,spin again...")
            elif pick_number==0:
                win_lose_label.config(text="rock smashes scissor!you lose...")
            elif pick_number==1:
                win_lose_label.config(text="rock smashes scissor!you win")
        
player_choice=ttk.Combobox(root,values=("rock","paper","scissors"))
player_choice.current(0)
player_choice.pack(pady=20)




computer_choice=ttk.Combobox(root,values=("rock","paper","scissors"))
computer_choice.current(1)
computer_choice.pack(pady=20)



# create spin button

spin_button=Button(root,text="spin!",command=spin)
spin_button.pack(pady=10)


exit_button=Button(root,text="exit!",command=exit)
exit_button.pack(pady=10)

# label for showing if you win or lose
win_lose_label=Label(root,text="",font=("Helvetica",18))
win_lose_label.pack(pady=50)

root.mainloop()
























