from tkinter import *
from tkinter import messagebox  
import random
import string
from PIL import Image, ImageTk
from pygame import mixer


ALPHABET = string.ascii_uppercase


def clicked():
    text = txt.get()
    indexes = ''
    for letter in text:
        if letter not in ALPHABET or len(text) != 6:
            messagebox.showerror('Ошибка', 'Неправильный формат ввода. Попробуйте ещё раз')
            return False
        letter_index = ALPHABET.index(letter)
        indexes += str((letter_index + 1) % 10)

    block1 = ''
    letters = [l for l in text]
    while len(block1) < 3:
        random_letter = random.choice(letters)
        letters.remove(random_letter)
        block1 += random_letter
    block2 = ''
    while len(block2) < 3:
        random_letter = random.choice(letters)
        letters.remove(random_letter)
        block2 += random_letter

    res = "Ваш ключ: {}".format(f'{block1}-{indexes}-{block2}')
    lbl.configure(text=res)
    txt.destroy()
    btn.destroy()


window = Tk()
window.title("Генератор ключей для The Sims4")
window.geometry('900x1100')


img =Image.open('unnamed.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(window, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)

lbl = Label(window, text="Введите слово из 6 букв латинскими прописными буквами: ", font=100, background='yellow')  
lbl.place(x=220, y=350)

txt = Entry(window, width=10)
txt.place(x=400, y=400)
txt.focus()

btn = Button(window, text="Сгенерировать ключ", bg="yellow", fg="black", command=clicked)
btn.place(x=370, y=450)


canvas=Canvas(window, width=60, height=100)
canvas.pack()
upY = 0
downY = 100
leftX = 0
rightX = 50
upX = downX = (rightX - leftX)//2
leftY = rightY = (downY - upY)//2
polygon_size = [upX, upY, rightX, rightY, downX, downY, leftX, leftY]
color = 'green'
polygon=canvas.create_polygon(polygon_size, fill=color)


def change():
    global color
    color = 'yellow' if color == 'green' else 'green'
    canvas.itemconfig(polygon, fill=color)
    window.after(500, change)
change()


mixer.init()
mixer.music.load('Sims.mp3')
mixer.music.play()

window.mainloop()