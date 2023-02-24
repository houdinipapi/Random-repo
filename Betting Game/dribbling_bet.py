from tkinter import *
import time
import random

winner = False

rashford_x = 0
rashford_y = 5

garnacho_x = 0
garnacho_y = 80

def start_game():
    global rashford_x
    global garnacho_x
    global winner

    while winner == False:
        time.sleep(0.05)
        random_move_rashford = random.randint(0, 20)
        random_move_garnacho = random.randint(0, 20)

        #Update the x position of both horses
        rashford_x += random_move_rashford
        garnacho_x += random_move_garnacho

        move_players(random_move_rashford, random_move_garnacho)
        main_screen.update()
        winner = check_winner()

    if winner == "Tie":
        Label(main_screen, text=winner, font=('calibri', 20), fg="brown").place(x=200, y=450)
    else:
        Label(main_screen, text=winner + " Wins!!", font=('calibri', 20), bg="brown").place(x=200, y=450)


def move_players(rashford_random_move, garnacho_random_move):
    canvas.move(rashford, rashford_random_move, 0)
    canvas.move(garnacho, garnacho_random_move, 0)

def check_winner():
    if rashford_x >= 550 and garnacho_x >= 550:
        return "Tie"
    if rashford_x >= 550:
        return "Rashford"
    if garnacho_x >= 550:
        return "Garnacho"
    return False

#Creating the main screen
main_screen = Tk()
main_screen.title('Dribbling Battle')
main_screen.geometry('600x500')
main_screen.config(background='light green')

#Creating a canvas
canvas = Canvas(main_screen, width=600, height=200, bg="green")
canvas.pack(pady=20)

#Import the images
rashford_dribbling_img = PhotoImage(file="./images/rashford_dribbling.png")
garnacho_dribbling_img = PhotoImage(file="./images/garnacho_dribbling.png")

#Resizing the images
rashford_dribbling_img = rashford_dribbling_img.zoom(15)
rashford_dribbling_img = rashford_dribbling_img.subsample(220)
garnacho_dribbling_img = garnacho_dribbling_img.zoom(15)
garnacho_dribbling_img = garnacho_dribbling_img.subsample(300)

#Adding the images to the canvas
rashford = canvas.create_image(rashford_x, rashford_y, anchor = NW, image = rashford_dribbling_img)
garnacho = canvas.create_image(garnacho_x, garnacho_y, anchor = NW, image = garnacho_dribbling_img)

#Adding text to the screen (Labels)
l1 = Label(main_screen, text='Select your player', font=('calibri', 20), bg="green")
l1.place(x = 230, y = 280)

l2 = Label(main_screen, text = 'CLICK PLAY WHEN READY!!',font=('calibri, 20'), bg="green")
l2.place(x = 150, y = 330)

b1 = Button(main_screen, text = 'PLAY!', height=2, width=15, bg='light blue', font=('calibri', 15), command=start_game)
b1.place(x=250, y=390)

main_screen.mainloop()