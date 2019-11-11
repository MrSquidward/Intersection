import tkinter as tk

        
class points:
    px, py = 0.0, 0.0
    t1, t2 = 0.0, 0.0
    xa, ya, xb, yb, xc, yc, xd, yd = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

    def scalePoints(self, x, y):
        canMaxX, canMaxY = 350, 350
        maxX = max(self.xa, self.xb, self.xc, self.xd, self.px)
        maxY = max(self.ya, self.yb, self.yc, self.yd, self.py)
        minX = min(self.xa, self.xb, self.xc, self.xd, self.px)
        minY = min(self.ya, self.yb, self.yc, self.yd, self.py)

        sX = canMaxX / (maxY - minY)
        sY = canMaxY / (maxX - minX)

        scaledX = 25 +  sX * (y - minY)
        scaledY = 25 +  canMaxY - (sY * (x - minX))
        
        return (scaledX, scaledY)


    def drawLines(self, canvas):
        sPa = self.scalePoints(self.xa, self.ya)
        sPb = self.scalePoints(self.xb, self.yb)
        sPc = self.scalePoints(self.xc, self.yc)
        sPd = self.scalePoints(self.xd, self.yd)
        sPp = self.scalePoints(self.px, self.py)
        
        canvas.create_line(sPa[0], sPa[1], sPb[0], sPb[1])
        canvas.create_line(sPc[0], sPc[1], sPd[0], sPd[1])
        
        canvas.create_line(sPp[0], sPp[1], sPb[0], sPb[1], dash=(6, 4))
        canvas.create_line(sPp[0], sPp[1], sPd[0], sPd[1], dash=(6, 4))
        
        canvas.create_oval(sPp[0]-5, sPp[1]-5, sPp[0]+5, sPp[1]+5, fill="red")
        canvas.create_oval(sPa[0]-5, sPa[1]-5, sPa[0]+5, sPa[1]+5, fill="black")
        canvas.create_oval(sPb[0]-5, sPb[1]-5, sPb[0]+5, sPb[1]+5, fill="black")
        canvas.create_oval(sPc[0]-5, sPc[1]-5, sPc[0]+5, sPc[1]+5, fill="black")
        canvas.create_oval(sPd[0]-5, sPd[1]-5, sPd[0]+5, sPd[1]+5, fill="black")

    
    def findCrossingPoint(self, xa, ya, xb, yb, xc, yc, xd, yd):
        try:
            self.xa = float(xa)
            self.ya = float(ya)
            self.xb = float(xb)
            self.yb = float(yb)
            self.xc = float(xc)
            self.yc = float(yc)
            self.xd = float(xd)
            self.yd = float(yd)
        except:
            return 1

        dXab = self.xb - self.xa
        dYab = self.yb - self.ya
        dXac = self.xc - self.xa
        dYcd = self.yd - self.yc
        dYac = self.yc - self.ya
        dXcd = self.xd - self.xc

        licz = (dXac * dYcd) - (dYac * dXcd)
        mian = (dXab * dYcd) - (dYab * dXcd)
        
        if mian == 0:
            return 1

        self.t1 = licz/mian
        self.t2 = ((dXac * dYab) - (dYac * dXab)) / ((dXab * dYcd) - (dYab * dXcd))

        self.px = self.xa + (self.t1*dXab)
        self.py = self.ya + (self.t1*dYab)

        self.px = round(self.px, 3)
        self.py = round(self.py, 3)

        return 0



class window:
    def __init__(self):
        self.Pts = points()
        self.root = tk.Tk()
        self.root.title('Computing intersection of line segments')
        
        self.InputFrame = tk.Frame(self.root, height = 500, width = 500)
        self.InputFrame.pack(side=tk.LEFT)
        self.SpaceFrame = tk.Frame(self.root, height = 500, width = 50)
        self.SpaceFrame.pack(side=tk.RIGHT)
        self.DrawFrame = tk.Frame(self.root, height = 500, width = 500)
        self.DrawFrame.pack(side=tk.RIGHT)
        self.canvas = tk.Canvas(self.DrawFrame, bg="white", height = 400, width = 400)
        self.canvas.pack()
        
        self.xaEntry = tk.Entry(self.InputFrame, font = 40)
        self.yaEntry = tk.Entry(self.InputFrame, font = 40)
        self.xbEntry = tk.Entry(self.InputFrame, font = 40)
        self.ybEntry = tk.Entry(self.InputFrame, font = 40)
        self.xcEntry = tk.Entry(self.InputFrame, font = 40)
        self.ycEntry = tk.Entry(self.InputFrame, font = 40)
        self.xdEntry = tk.Entry(self.InputFrame, font = 40)
        self.ydEntry = tk.Entry(self.InputFrame, font = 40)

        self.errorInfoLabelText = tk.StringVar()
        self.errorInfoLabelText.set(' ')

        self.pxLabelText = tk.StringVar()
        self.pxLabelText.set(' ')

        self.pyLabelText = tk.StringVar()
        self.pyLabelText.set(' ')

        self.resultLabelText = tk.StringVar()
        self.resultLabelText.set(' ')

        self.crossPointLocation = tk.StringVar()
        self.crossPointLocation.set(' ')
    

        
    def addEncourageLabel(self):
        introLb = tk.Label(self.InputFrame, font = 40,
                   text = "Enter coordinates of four points: ")
        introLb.place(relx = 0.01, rely = 0.01)


    def addInputsFields(self):
        self.xaEntry.place(relx = 0.1, rely = 0.1, relwidth = 0.3)
        self.yaEntry.place(relx = 0.6, rely = 0.1, relwidth = 0.3)
        self.xbEntry.place(relx = 0.1, rely = 0.2, relwidth = 0.3)
        self.ybEntry.place(relx = 0.6, rely = 0.2, relwidth = 0.3)
        self.xcEntry.place(relx = 0.1, rely = 0.3, relwidth = 0.3)
        self.ycEntry.place(relx = 0.6, rely = 0.3, relwidth = 0.3)
        self.xdEntry.place(relx = 0.1, rely = 0.4, relwidth = 0.3)
        self.ydEntry.place(relx = 0.6, rely = 0.4, relwidth = 0.3)

    def clearInputsFields(self):
        self.xaEntry.delete(0, "end")
        self.yaEntry.delete(0, "end")
        self.xbEntry.delete(0, "end")
        self.ybEntry.delete(0, "end")
        self.xcEntry.delete(0, "end")
        self.ycEntry.delete(0, "end")
        self.xdEntry.delete(0, "end")
        self.ydEntry.delete(0, "end")

    def addInputsLabels(self):
        xaLabel = tk.Label(self.InputFrame, font = 40, text = 'Xa:')
        yaLabel = tk.Label(self.InputFrame, font = 40, text = 'Ya:')
        xbLabel = tk.Label(self.InputFrame, font = 40, text = 'Xb:')
        ybLabel = tk.Label(self.InputFrame, font = 40, text = 'Yb:')
        xcLabel = tk.Label(self.InputFrame, font = 40, text = 'Xc:')
        ycLabel = tk.Label(self.InputFrame, font = 40, text = 'Yc:')
        xdLabel = tk.Label(self.InputFrame, font = 40, text = 'Xd:')
        ydLabel = tk.Label(self.InputFrame, font = 40, text = 'Yd:')
        
        xaLabel.place(relx = 0.01, rely = 0.1)
        yaLabel.place(relx = 0.5, rely = 0.1)
        xbLabel.place(relx = 0.01, rely = 0.2)
        ybLabel.place(relx = 0.5, rely = 0.2)
        xcLabel.place(relx = 0.01, rely = 0.3)
        ycLabel.place(relx = 0.5, rely = 0.3)
        xdLabel.place(relx = 0.01, rely = 0.4)
        ydLabel.place(relx = 0.5, rely = 0.4)

        
    def addErrorLabel(self):
        self.errorInfoLabelText.set('Lines are parallel \n or inputs are incorrect!!')
        self.errorInfoLabel = tk.Label(self.InputFrame, font = 40,
                                       textvariable = self.errorInfoLabelText)
        self.errorInfoLabel.place(relx = 0.2, rely = 0.6)


    def addResultLabel(self):
        self.resultLabelText.set('Point of intersection: ')
        self.pxLabelText.set('Xp:   ' + str(self.Pts.px))
        self.pyLabelText.set('Yp:   ' + str(self.Pts.py))
        
        resultLabel = tk.Label(self.InputFrame, font = 40, textvariable = self.resultLabelText)
        pxLabel = tk.Label(self.InputFrame, font = 40, textvariable = self.pxLabelText)
        pyLabel = tk.Label(self.InputFrame, font = 40, textvariable = self.pyLabelText)
        
        resultLabel.place(relx = 0.01, rely = 0.6)
        pxLabel.place(relx = 0.01, rely = 0.7)
        pyLabel.place(relx = 0.5, rely = 0.7)

    def callbackResetBtn(self):
        self.clearInputsFields()
        self.canvas.delete("all")
        
        self.pxLabelText.set(' ')
        self.pyLabelText.set(' ')
        self.resultLabelText.set(' ')
        self.crossPointLocation.set(' ')
        self.errorInfoLabelText.set(' ')

    def addResetButton(self):
        resetButton = tk.Button(self.InputFrame, font = 40, text = "Reset",
                                command = self.callbackResetBtn)

        resetButton.place(relx = 0.4, rely = 0.9, width = 100)


    def callbackComputeBtn(self, xa, ya, xb, yb, xc, yc, xd, yd):
        checkError = self.Pts.findCrossingPoint(xa, ya, xb, yb, xc, yc, xd, yd)
        
        if checkError:
            self.addErrorLabel()
            return
        
        self.Pts.drawLines(self.canvas)
        self.addResultLabel()
        
        if (self.Pts.t1 >= 0 and self.Pts.t1 <= 1) and (self.Pts.t2 >= 0 and self.Pts.t2 <= 1):
            self.crossPointLocation.set('Line segments are crossing each other!')
        else:
            self.crossPointLocation.set('Intersection is at extension of line segments')

        crossInfoLabel = tk.Label(self.InputFrame, font = 40, textvariable = self.crossPointLocation)
        crossInfoLabel.place(relx = 0.01, rely = 0.8)

        self.resultLabelText.set('Point of intersection: ')


    def addComputeButton(self):
        computeButton = tk.Button(self.InputFrame, font = 40,
                                  text="Compute intersection",
                                  command = lambda:self.callbackComputeBtn(
                                      self.xaEntry.get(), self.yaEntry.get(),
                                      self.xbEntry.get(), self.ybEntry.get(),
                                      self.xcEntry.get(), self.ycEntry.get(),
                                      self.xdEntry.get(), self.ydEntry.get())
                                  )

        computeButton.place(relx = 0.3, rely = 0.5, relwidth = 0.4)

    
    
