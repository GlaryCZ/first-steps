from tkinter import *

root = Tk()
N = 5
blocks = []

for i in range(N**2):
    blocks.append(i+1)
blocks = blocks[:-1]
blocks.append(" ")
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
def down(p):
    if not blocks.index(" ") > N**2-N-1:
        print("penis")
        # TODO

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

def right(p):
    if not (blocks.index(" ")+1) % N == 0:
        poped2i = blocks.index(" ")+1
        poped2 = blocks.pop(blocks.index(" ")+1)
        poped1i = blocks.index(" ")
        blocks.pop(blocks.index(" "))

        blocks.insert(poped1i, poped2)
        blocks.insert(poped2i, " ")
        

        print(blocks)
        draw(blocks)


root.bind("<w>", up)
root.bind("<s>", down)
root.bind("<a>", left)
root.bind("<d>", right)

root.mainloop()