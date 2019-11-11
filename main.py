import tkinter as tk
import mywindow as mywnd


wnd = mywnd.window()
wnd.addEncourageLabel()
wnd.addInputsFields()
wnd.addInputsLabels()
wnd.addComputeButton()
wnd.addResetButton()

wnd.root.mainloop()
