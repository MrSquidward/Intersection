import mywindow as mywnd

wnd = mywnd.window()
wnd.addEncourageLabel()
wnd.addInputsFields()
wnd.addInputsLabels()
wnd.addComputeButton()
wnd.addResetButton()
wnd.addFirstChangeColorButton()
wnd.addSecondChangeColorButton()
wnd.addHideDashLines()

wnd.root.mainloop()
