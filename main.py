import mywindow as mywnd

wnd = mywnd.Window()
IFrame = mywnd.InputFrame(wnd.root, wnd.canvas, wnd.Pts)
MFrame = mywnd.MarginFrame(wnd.root, wnd.canvas, wnd.MarginFrame)

IFrame.addEncourageLabel()
IFrame.addInputsFields()
IFrame.addInputsLabels()
IFrame.addComputeButton()
IFrame.addResetButton()
IFrame.addLoadButton()

MFrame.addFirstChangeColorButton()
MFrame.addSecondChangeColorButton()
MFrame.addHideDashLinesButton()
MFrame.addShowPointsLabelsButton()
MFrame.addExitButton()

wnd.root.mainloop()
