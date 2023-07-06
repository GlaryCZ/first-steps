from tkinter import *
import random

root = Tk()

N = 5
blocks = []
win_pos = []
for i in range(N**2):
    blocks.append(i+1)
blocks = blocks[:-1]
blocks.append(" ")
for i in range(N**2):
    win_pos.append(i+1)
win_pos = win_pos[:-1]
win_pos.append(" ")
print(blocks)
def draw(blocks):
    for i, block in enumerate(blocks):
        if block == " ":
            Label(root, text=block, height=5, width=10, bg="black", font="areal").grid(column=i % N, row=i // N)
        else:
            Label(root, text=block, height=5, width=10, bg="red", font="areal").grid(column=i % N, row=i // N)

draw(blocks)
def up(p):
    if not blocks.index(" ") < N:
        poped2i = blocks.index(" ")-N
        poped2 = blocks.pop(blocks.index(" ")-N)
        poped1i = blocks.index(" ")
        blocks.pop(blocks.index(" "))

        blocks.insert(poped1i, poped2)
        blocks.insert(poped2i, " ")
        

        print(blocks)
        draw(blocks)
        check_win(blocks)
def down(p):
    if not blocks.index(" ") > N**2-N-1:
        poped2i = blocks.index(" ")+N
        poped2 = blocks.pop(blocks.index(" ")+N)
        poped1i = blocks.index(" ")
        blocks.pop(blocks.index(" "))

        blocks.insert(poped1i, poped2)
        blocks.insert(poped2i, " ")
        

        print(blocks)
        draw(blocks)
        check_win(blocks)

def left(p):
    if not (blocks.index(" ")) % N == 0:
        poped2i = blocks.index(" ")-1
        poped2 = blocks.pop(blocks.index(" ")-1)
        poped1i = blocks.index(" ")
        blocks.pop(blocks.index(" "))
        blocks.insert(poped2i, poped2)
        blocks.insert(poped1i, " ")
        print(blocks)
        draw(blocks)
        check_win(blocks)

def right(p):
    if not (blocks.index(" ")+1) % N == 0:
        poped2i = blocks.index(" ")+1
        poped2 = blocks.pop(blocks.index(" ")+1)
        poped1i = blocks.index(" ")
        blocks.pop(blocks.index(" "))

        blocks.insert(poped1i, poped2)
        print(poped2i)
        blocks.insert(poped2i, " ")
        

        print(blocks)
        draw(blocks)
        check_win(blocks)


def check_win(c):
    print("penis")
    print(blocks)
    print(win_pos)
    if blocks == win_pos:
        print("######################################")
        print("win")

def shuffle(x):
    for i in range(x):
        c = random.randint(0, 3)
        if c == 0:
            right(False)
        elif c == 1:
            left(False)
        elif c == 2:
            up(False)
        else:
            down(False)
shuffle(100)

root.bind("<w>", up)
root.bind("<s>", down)
root.bind("<a>", left)
root.bind("<d>", right)

root.mainloop()