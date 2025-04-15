import tkinter as tk


class CGLCell(tk.Label):
    def __init__(self, master, coord):
        tk.Label.__init__(self, master, height=2, width=1, font=("Courier New", 14), borderwidth=5, relief=tk.GROOVE)
        self.grid(row=int(coord[0]), column=int(coord[1]))
        self.state = False
        self.coord = coord
        self.master = master
        self['bg'] = 'black'
        self.checkSurrounding()
        self.bind("<Button-1>", self.toggle)

    def giveState(self):
        return self.state

    def toggle(self, event):
        self.state = not self.state
        if self['bg'] == 'black':
            self['bg'] = 'white'
        else:
            self['bg'] = 'black'
        print(self.giveState())

    def checkSurrounding(self):
        master = self.master
        # print(master.cellGrid)
        # print(self.master.cellGrid[0].coord)
        pass


class CGLFrame(tk.Frame):
    def __init__(self, master, height, width):
        tk.Frame.__init__(self, master)
        self.grid()
        # z = CGLCell(self,(0,0))
        self.cellGrid = []
        for x in range(height):
            for y in range(width):
                self.cellGrid.append(CGLCell(self, (x, y)))
                # print(self.cellGrid)


root = tk.Tk()
root.title("Conway's Game of Life")
# MSG = MSGrid(root,10,10,10)
CGL = CGLFrame(root, 50,50)
CGL.mainloop()
#
# print("Test")
# #!/usr/bin/env python
#
# """Proof of concept gfxdraw example"""
#
# import pygame, sys
# from pygame.locals import *
#
#
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((400, 300))
#     done = False
#     red = (255, 0, 0)
#     green = (0, 255, 0)
#     blue = (0, 0, 255)
#     white = (255, 255, 255)
#     while not done:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
#         pygame.draw.rect(screen, red, pygame.Rect(100, 30, 60, 60))
#         pygame.draw.polygon(screen, blue, ((25, 75), (76, 125), (275, 200), (350, 25), (60, 280)))
#         pygame.draw.circle(screen, white, (180, 180), 60)
#         pygame.draw.line(screen, red, (10, 200), (300, 10), 4)
#         pygame.draw.ellipse(screen, green, (250, 200, 130, 80))
#         pygame.display.update()
#
#
#
# if __name__ == "__main__":
#     main()
