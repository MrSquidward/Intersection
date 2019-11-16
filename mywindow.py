import tkinter as tk
import math as m
from tkcolorpicker import askcolor


def findNearestPoint(Pt, ComparedPt1, ComparedPt2):
    distancePt1 = m.sqrt(((Pt[0] - ComparedPt1[0]) ** 2) + ((Pt[1] - ComparedPt1[1]) ** 2))
    distancePt2 = m.sqrt(((Pt[0] - ComparedPt2[0]) ** 2) + ((Pt[1] - ComparedPt2[1]) ** 2))

    if distancePt1 <= distancePt2:
        return ComparedPt1
    else:
        return ComparedPt2


class Points:
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

        margin = 25
        scaledX = margin + sX * (y - minY)
        scaledY = margin + canMaxY - (sY * (x - minX))

        return scaledX, scaledY

    def addPointsLabels(self, P1, P2, P3, P4, Pp):
        ALabel = tk.Label(self.canvas, text='A', bg='white')
        BLabel = tk.Label(self.canvas, text='B', bg='white')
        CLabel = tk.Label(self.canvas, text='C', bg='white')
        DLabel = tk.Label(self.canvas, text='D', bg='white')

        self.canvas.create_window(P1[0]+15, P1[1]+15, window=ALabel, tags='AL')
        self.canvas.create_window(P2[0]+15, P2[1]+15, window=BLabel, tags='BL')
        self.canvas.create_window(P3[0]+15, P3[1]+15, window=CLabel, tags='CL')
        self.canvas.create_window(P4[0]+15, P4[1]+15, window=DLabel, tags='DL')

        self.hidePointsLabels()

    def hidePointsLabels(self):
        self.canvas.itemconfig('AL', state='hidden')
        self.canvas.itemconfig('BL', state='hidden')
        self.canvas.itemconfig('CL', state='hidden')
        self.canvas.itemconfig('DL', state='hidden')

    def drawLines(self, canvas):
        sPa = self.scalePoints(self.xa, self.ya)
        sPb = self.scalePoints(self.xb, self.yb)
        sPc = self.scalePoints(self.xc, self.yc)
        sPd = self.scalePoints(self.xd, self.yd)
        sPp = self.scalePoints(self.px, self.py)

        self.canvas = canvas
        self.canvas.create_line(sPa[0], sPa[1], sPb[0], sPb[1], width=2, tags='line1')
        self.canvas.create_line(sPc[0], sPc[1], sPd[0], sPd[1], width=2, tags='line2')

        self.addPointsLabels(sPa, sPb, sPc, sPd, sPp)

        if not (0 <= self.t1 <= 1):
            nearestPt = findNearestPoint(sPp, sPa, sPb)
            self.canvas.create_line(sPp[0], sPp[1], nearestPt[0], nearestPt[1], dash=(6, 4), tags='lined1')

        if not (0 <= self.t2 <= 1):
            nearestPt = findNearestPoint(sPp, sPc, sPd)
            self.canvas.create_line(sPp[0], sPp[1], nearestPt[0], nearestPt[1], dash=(6, 4), tags='lined2')

        rad = 5  # radius
        canvas.create_oval(sPp[0] - rad, sPp[1] - rad, sPp[0] + rad, sPp[1] + rad, fill='red')
        canvas.create_oval(sPa[0] - rad, sPa[1] - rad, sPa[0] + rad, sPa[1] + rad, fill='black', tags='PointA')
        canvas.create_oval(sPb[0] - rad, sPb[1] - rad, sPb[0] + rad, sPb[1] + rad, fill='black', tags='PointB')
        canvas.create_oval(sPc[0] - rad, sPc[1] - rad, sPc[0] + rad, sPc[1] + rad, fill='black', tags='PointC')
        canvas.create_oval(sPd[0] - rad, sPd[1] - rad, sPd[0] + rad, sPd[1] + rad, fill='black', tags='PointD')

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

        nominator = (dXac * dYcd) - (dYac * dXcd)
        denominator = (dXab * dYcd) - (dYab * dXcd)

        if denominator == 0:
            return 1

        self.t1 = nominator / denominator
        self.t2 = ((dXac * dYab) - (dYac * dXab)) / ((dXab * dYcd) - (dYab * dXcd))

        self.px = self.xa + (self.t1 * dXab)
        self.py = self.ya + (self.t1 * dYab)

        self.px = round(self.px, 3)
        self.py = round(self.py, 3)

        return 0


class Window:
    def __init__(self):
        self.Pts = Points()
        self.root = tk.Tk()
        self.root.title('Computing intersection of line segments')

        self.MarginFrame = tk.Frame(self.root, height=500, width=200)
        self.MarginFrame.pack(side=tk.RIGHT)

        self.DrawFrame = tk.Frame(self.root, height=500, width=500)
        self.DrawFrame.pack(side=tk.RIGHT)

        self.canvas = tk.Canvas(self.DrawFrame, bg='white', height=400, width=400)
        self.canvas.pack()


class MarginFrame:
    dashLinesDisplayStatus = True
    pointsLabelsDisplayStatus = False

    def __init__(self, root, can, MF):
        self.root = root
        self.canvas = can
        self.MarginFrame = MF

        self.colorList = tk.Listbox(self.MarginFrame, font=40)

    def callbackFirstChangeColorBtn(self):
        color = askcolor()
        color_name = color[1]

        if color_name:
            self.canvas.itemconfig('line1', fill=color_name)
            self.canvas.itemconfig('lined1', fill=color_name)
            self.canvas.itemconfig('PointA', fill=color_name)
            self.canvas.itemconfig('PointB', fill=color_name)

    def callbackSecondChangeColorBtn(self):
        color = askcolor()
        color_name = color[1]

        if color_name:
            self.canvas.itemconfig('line2', fill=color_name)
            self.canvas.itemconfig('lined2', fill=color_name)
            self.canvas.itemconfig('PointC', fill=color_name)
            self.canvas.itemconfig('PointD', fill=color_name)

    def callbackHideDashLinesBtn(self):
        if self.dashLinesDisplayStatus:
            self.canvas.itemconfig('lined1', state='hidden')
            self.canvas.itemconfig('lined2', state='hidden')
            self.dashLinesDisplayStatus = False
        else:
            self.canvas.itemconfig('lined1', state='normal')
            self.canvas.itemconfig('lined2', state='normal')
            self.dashLinesDisplayStatus = True

    def callbackShowPointsLabelsBtn(self):
        if self.pointsLabelsDisplayStatus:
            self.canvas.itemconfig('AL', state='hidden')
            self.canvas.itemconfig('BL', state='hidden')
            self.canvas.itemconfig('CL', state='hidden')
            self.canvas.itemconfig('DL', state='hidden')
            self.pointsLabelsDisplayStatus = False
        else:
            self.canvas.itemconfig('AL', state='normal')
            self.canvas.itemconfig('BL', state='normal')
            self.canvas.itemconfig('CL', state='normal')
            self.canvas.itemconfig('DL', state='normal')
            self.pointsLabelsDisplayStatus = True

    def addFirstChangeColorButton(self):
        changeColorButton = tk.Button(self.MarginFrame, font=40,
                                      text='Change color \n of first line',
                                      command=self.callbackFirstChangeColorBtn)

        changeColorButton.place(relx=0.1, rely=0.1, width=170)

    def addSecondChangeColorButton(self):
        changeColorButton = tk.Button(self.MarginFrame, font=40,
                                      text='Change color \n of second line',
                                      command=self.callbackSecondChangeColorBtn)

        changeColorButton.place(relx=0.1, rely=0.3, width=170)

    def addHideDashLines(self):
        hideDashLinesButton = tk.Button(self.MarginFrame, font=40, text='Hide/Show Dash \n Lines',
                                        command=self.callbackHideDashLinesBtn)

        hideDashLinesButton.place(relx=0.1, rely=0.5, width=170)

    def addShowPointsLabels(self):
        showPointsLabelsButton = tk.Button(self.MarginFrame, font=40, text='Show/Hide Points \n Lables',
                                        command=self.callbackShowPointsLabelsBtn)

        showPointsLabelsButton.place(relx=0.1, rely=0.7, width=170)


class InputFrame:
    def __init__(self, root, can, PtsObj):
        self.root = root
        self.canvas = can
        self.Pts = PtsObj

        self.Input = tk.Frame(self.root, height=500, width=500)
        self.Input.pack(side=tk.LEFT)

        self.xaEntry = tk.Entry(self.Input, font=40)
        self.yaEntry = tk.Entry(self.Input, font=40)
        self.xbEntry = tk.Entry(self.Input, font=40)
        self.ybEntry = tk.Entry(self.Input, font=40)
        self.xcEntry = tk.Entry(self.Input, font=40)
        self.ycEntry = tk.Entry(self.Input, font=40)
        self.xdEntry = tk.Entry(self.Input, font=40)
        self.ydEntry = tk.Entry(self.Input, font=40)

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
        introLb = tk.Label(self.Input, font=40,
                           text='Enter coordinates of four points: ')
        introLb.place(relx=0.01, rely=0.01)

    def addInputsFields(self):
        self.xaEntry.place(relx=0.1, rely=0.1, relwidth=0.3)
        self.yaEntry.place(relx=0.6, rely=0.1, relwidth=0.3)
        self.xbEntry.place(relx=0.1, rely=0.2, relwidth=0.3)
        self.ybEntry.place(relx=0.6, rely=0.2, relwidth=0.3)
        self.xcEntry.place(relx=0.1, rely=0.3, relwidth=0.3)
        self.ycEntry.place(relx=0.6, rely=0.3, relwidth=0.3)
        self.xdEntry.place(relx=0.1, rely=0.4, relwidth=0.3)
        self.ydEntry.place(relx=0.6, rely=0.4, relwidth=0.3)

    def addInputsLabels(self):
        xaLabel = tk.Label(self.Input, font=40, text='Xa:')
        yaLabel = tk.Label(self.Input, font=40, text='Ya:')
        xbLabel = tk.Label(self.Input, font=40, text='Xb:')
        ybLabel = tk.Label(self.Input, font=40, text='Yb:')
        xcLabel = tk.Label(self.Input, font=40, text='Xc:')
        ycLabel = tk.Label(self.Input, font=40, text='Yc:')
        xdLabel = tk.Label(self.Input, font=40, text='Xd:')
        ydLabel = tk.Label(self.Input, font=40, text='Yd:')

        xaLabel.place(relx=0.01, rely=0.1)
        yaLabel.place(relx=0.5, rely=0.1)
        xbLabel.place(relx=0.01, rely=0.2)
        ybLabel.place(relx=0.5, rely=0.2)
        xcLabel.place(relx=0.01, rely=0.3)
        ycLabel.place(relx=0.5, rely=0.3)
        xdLabel.place(relx=0.01, rely=0.4)
        ydLabel.place(relx=0.5, rely=0.4)

    def addErrorLabel(self):
        self.errorInfoLabelText.set('Lines are parallel \n or inputs are incorrect!!')
        self.errorInfoLabel = tk.Label(self.Input, font=40,
                                       textvariable=self.errorInfoLabelText)
        self.errorInfoLabel.place(relx=0.2, rely=0.6)

    def addResultLabel(self):
        self.resultLabelText.set('Point of intersection: ')
        self.pxLabelText.set('Xp:   ' + str(self.Pts.px))
        self.pyLabelText.set('Yp:   ' + str(self.Pts.py))

        resultLabel = tk.Label(self.Input, font=40, textvariable=self.resultLabelText)
        pxLabel = tk.Label(self.Input, font=40, textvariable=self.pxLabelText)
        pyLabel = tk.Label(self.Input, font=40, textvariable=self.pyLabelText)

        resultLabel.place(relx=0.01, rely=0.6)
        pxLabel.place(relx=0.01, rely=0.7)
        pyLabel.place(relx=0.5, rely=0.7)

    def clearInputsFields(self):
        self.xaEntry.delete(0, 'end')
        self.yaEntry.delete(0, 'end')
        self.xbEntry.delete(0, 'end')
        self.ybEntry.delete(0, 'end')
        self.xcEntry.delete(0, 'end')
        self.ycEntry.delete(0, 'end')
        self.xdEntry.delete(0, 'end')
        self.ydEntry.delete(0, 'end')

    def clearLabelsText(self):
        self.pxLabelText.set(' ')
        self.pyLabelText.set(' ')
        self.resultLabelText.set(' ')
        self.crossPointLocation.set(' ')
        self.errorInfoLabelText.set(' ')

    def callbackComputeBtn(self, xa, ya, xb, yb, xc, yc, xd, yd):
        self.canvas.delete('all')
        self.clearLabelsText()

        checkError = self.Pts.findCrossingPoint(xa, ya, xb, yb, xc, yc, xd, yd)

        if checkError:
            self.addErrorLabel()
            return

        self.Pts.drawLines(self.canvas)
        self.addResultLabel()

        if (0 <= self.Pts.t1 <= 1) and (0 <= self.Pts.t2 <= 1):
            self.crossPointLocation.set('Line segments are crossing each other!')
        else:
            self.crossPointLocation.set('Intersection is at extension of line segments')

        crossInfoLabel = tk.Label(self.Input, font=40, textvariable=self.crossPointLocation)
        crossInfoLabel.place(relx=0.01, rely=0.8)

        self.resultLabelText.set('Point of intersection: ')

    def callbackLoadBtn(self):
            txtFile = open('points.txt')
            pts = []

            for line in txtFile:
                pts.append(float(line))

            self.xaEntry.insert(0, pts[0])
            self.yaEntry.insert(0, pts[1])
            self.xbEntry.insert(0, pts[2])
            self.ybEntry.insert(0, pts[3])
            self.xcEntry.insert(0, pts[4])
            self.ycEntry.insert(0, pts[5])
            self.xdEntry.insert(0, pts[6])
            self.ydEntry.insert(0, pts[7])

    def callbackResetBtn(self):
        self.clearInputsFields()
        self.canvas.delete('all')
        self.clearLabelsText()

    def addComputeButton(self):
        computeButton = tk.Button(self.Input, font=40,
                                  text='Compute intersection',
                                  command=lambda: self.callbackComputeBtn(
                                      self.xaEntry.get(), self.yaEntry.get(),
                                      self.xbEntry.get(), self.ybEntry.get(),
                                      self.xcEntry.get(), self.ycEntry.get(),
                                      self.xdEntry.get(), self.ydEntry.get())
                                  )

        computeButton.place(relx=0.25, rely=0.5, width=220)

    def addLoadButton(self):
        loadButton = tk.Button(self.Input, font=40, text='Load',
                                command=self.callbackLoadBtn)

        loadButton.place(relx=0.2, rely=0.9, width=100)

    def addResetButton(self):
        resetButton = tk.Button(self.Input, font=40, text='Reset',
                                command=self.callbackResetBtn)

        resetButton.place(relx=0.5, rely=0.9, width=100)