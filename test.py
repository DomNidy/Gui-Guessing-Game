from tkinter import *

#Creates window
root = Tk()

#Frames
topFrame = Frame(root)
bottomFrame = Frame(root)
topFrame.pack()
bottomFrame.pack(side=BOTTOM)

#Buttons
button_1 = Button(topFrame, text="Button 1", fg="red")
button_2 = Button(topFrame, text="Button 2", fg="blue")
button_3 = Button(topFrame, text="Button 3", fg="green")
button_4 = Button(bottomFrame, text="Button 4", fg="red")

button_1.pack(side=LEFT)
button_2.pack(side=RIGHT)
button_3.pack()
button_4.pack()

#Main loop
root.mainloop()