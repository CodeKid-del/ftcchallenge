import tkinter as tk


class CGLCell(tk.Label):
    def __init__(self, master, coord):
        tk.Label.__init__(self, master, height=2, width=1, font=("Courier New", 14), borderwidth=5, relief=tk.GROOVE)
        self.grid(row=int(coord[0]), column=int(coord[1]))
        self.state = False
        self.coord = coord
        self.master = master
        self['bg'] = 'black'
        self.isUpdating = True
        # self.checkSurrounding()
        self.bind("<Button-1>", self.toggle)
        self.after(1000,self.update)
        # while True:
        #     self.update()


    def giveState(self):
        return self.state

    def giveCoords(self):
        return self.coord

    def isupdating(self):
        return self.isUpdating

    def stopUpdating(self):
        self.isUpdating = False

    def startUpdating(self):
        self.isUpdating = True
        self.update()

    def toggle(self, event):
        self.state = not self.state
        if self['bg'] == 'black':
            self['bg'] = 'white'
        else:
            self['bg'] = 'black'
        # print(self.giveState())
        # print(self.checkSurrounding())

    def die(self):
        self.state = False
        self['bg'] = 'black'
        # print(self.giveState())

    def live(self):
        self.state=True
        self['bg'] = 'white'


    def checkSurrounding(self):
        '''calls the frame to check how many cells around it are alive'''
        return self.master.checkSurroundingCoord(coord=self.giveCoords())

    def update(self):
        surroundingAliveCells = self.checkSurrounding()
        if self.giveState():
            if surroundingAliveCells < 2:
                self.die()
            if surroundingAliveCells > 3:
                self.die()
        else:
            if surroundingAliveCells == 3:
                self.live()
        if self.isupdating():
            self.after(1000,self.update)


class CGLFrame(tk.Frame):
    def __init__(self, master, rows, cols):
        tk.Frame.__init__(self, master)
        self.grid()
        # z = CGLCell(self,(0,0))
        self.rows = rows
        self.cols = cols
        # print(rows,cols)
        self.cellGrid = []
        for r in range(rows):
            tempList = []
            for c in range(cols):
                tempList.append([])
            self.cellGrid.append(tempList)
        # print(self.cellGrid)
        for x in range(rows):
            for y in range(cols):
                # print(x,y)
                self.cellGrid[x][y] = CGLCell(self, (x, y))
                self.cellGrid[x][y].grid(row=x,column=y)

        self.isUpdating = True

        self.bind('<space>',self.toggleUpdating)

        self.toggleUpdating('hi')


    def checkSurroundingCoord(self,coord):
        aliveCounter = 0
        for r in range(coord[0]-1,coord[0]+2):
            for c in range(coord[1] - 1, coord[1] + 2):

                # print(r,c,self.cellGrid[r][c].giveState())
                # print(coord)
                # print(len(self.cellGrid))
                if r >= self.rows:
                    r = r%self.rows
                if c >= self.cols:
                    c = c%self.cols
                if self.cellGrid[r][c].giveState():
                    aliveCounter +=1
        if self.cellGrid[coord[0]][coord[1]].giveState():
            aliveCounter -= 1
        return aliveCounter

    def toggleUpdating(self,event):
        self.isUpdating = not self.isUpdating
        # self.cellGrid[0][0].toggle(' ')
        # print(self.isUpdating)
        for r in range(self.rows):
            for c in range(self.cols):
                if self.isUpdating:
                    self.cellGrid[r][c].startUpdating()
                else:
                    self.cellGrid[r][c].stopUpdating()

root = tk.Tk()
root.title("Conway's Game of Life")
# MSG = MSGrid(root,10,10,10)
CGL = CGLFrame(root, 25,25)
root.bind('<space>',CGL.toggleUpdating)
CGL.mainloop()
