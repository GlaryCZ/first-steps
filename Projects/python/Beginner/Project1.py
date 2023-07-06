from tkinter import *
import math
import random

class Playground:
    def __init__(self, lol):
        self.lol = lol ** 2
        self.arr = list(range(1, self.lol + 1))

    def move_right(self, event):
        if event.keysym == 'd':
            black = self.arr.index(self.lol)  
            if black % math.isqrt(self.lol) != math.isqrt(self.lol) - 1:  
                self.arr[black], self.arr[black + 1] = self.arr[black + 1], self.arr[black]  
            w.delete("all")  
            self.Field()
            if  a1.Check():
                w.delete("all") 
                # w.create_text(200, 200, text="You have won!", fill="black", font=("Arial", 16))
                a1.Text()
    def move_left(self, event):
        if event.keysym == 'a':
            black = self.arr.index(self.lol)  
            if black % math.isqrt(self.lol) != 0:  
                self.arr[black], self.arr[black - 1] = self.arr[black - 1], self.arr[black]  
            w.delete("all")  
            self.Field() 
            if  a1.Check():
                w.delete("all")
                a1.Text()
                
    def move_up(self, event):
        if event.keysym == 'w':
            black = self.arr.index(self.lol)  
            if black // math.isqrt(self.lol) != 0:
                self.arr[black], self.arr[black - math.isqrt(self.lol)] = self.arr[black - math.isqrt(self.lol) ], self.arr[black]  # Swap the black square with the left neighbor
            w.delete("all")  
            self.Field() 
            if  a1.Check():
                w.delete("all")   
                a1.Text()
                
    def move_down(self, event):
        if event.keysym == 's':
            black = self.arr.index(self.lol)  
            if black // math.isqrt(self.lol) != math.isqrt(self.lol)-1:
                self.arr[black], self.arr[black + math.isqrt(self.lol)] = self.arr[black + math.isqrt(self.lol) ], self.arr[black]  # Swap the black square with the left neighbor
            w.delete("all")  
            self.Field()
            if  a1.Check():
                w.delete("all")
                a1.Text()
            
    def shuffle(self):
        rn = random.randint(1,4)
        black = self.arr.index(self.lol)
        if rn == 1: #down
           if black // math.isqrt(self.lol) != math.isqrt(self.lol)-1:
                self.arr[black], self.arr[black + math.isqrt(self.lol)] = self.arr[black + math.isqrt(self.lol) ], self.arr[black] 
            
                
        if rn == 2: #up
            black = self.arr.index(self.lol)  
            if black // math.isqrt(self.lol) != math.isqrt(self.lol):                              
                self.arr[black], self.arr[black - math.isqrt(self.lol)] = self.arr[black - math.isqrt(self.lol) ], self.arr[black]
          
        if rn == 3: #right
            black = self.arr.index(self.lol)  
            if black % math.isqrt(self.lol) != math.isqrt(self.lol) - 1:  
                self.arr[black], self.arr[black + 1] = self.arr[black + 1], self.arr[black]  
                
                
        if rn ==4: #left
            black = self.arr.index(self.lol)  
            if black % math.isqrt(self.lol) != 0: 
                self.arr[black], self.arr[black - 1] = self.arr[black - 1], self.arr[black]

    def Check(self):
        l = 0
        for i, num in enumerate(self.arr):
            if i == num -1:
                l += 1
                print(l)
            else:
                return False
            
        if l== len(self.arr):
            return True
        
    def Text(self):
        w.create_text(200, 200, text="You have won!", fill="red", font=("Arial", 40))
            
            
    def Field(self):
        gap = 10
        rectangle_width = 100
        for i, num in enumerate(self.arr):
            sq = math.isqrt(self.lol)
            x1 = i % sq * (rectangle_width + gap)
            y1 = i // sq * (rectangle_width + gap)
            x2 = x1 + rectangle_width
            y2 = y1 + rectangle_width

            if num != self.lol:
                w.create_rectangle(x1, y1, x2, y2, fill="blue", outline='black')
                text_x = (x1 + x2) / 2
                text_y = (y1 + y2) / 2
                w.create_text(text_x, text_y, text=str(num), fill='white', font=('Arial', 16))
            else:
                w.create_rectangle(x1, y1, x2, y2, fill="black", outline='blue')
                
                
                
                
game = True
root = Tk()
root.title("Puzzle")
w = Canvas(root, width=425, height=425)
a1 = Playground(4) 
for i in range(1000): 
    a1.shuffle()
w.pack()
root.bind('<KeyPress-a>', a1.move_left)
root.bind('<KeyPress-d>', a1.move_right)
root.bind('<KeyPress-w>', a1.move_up)
root.bind('<KeyPress-s>', a1.move_down)
a1.Field()
root.mainloop()
