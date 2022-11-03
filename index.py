from tkinter import *

root = Tk()
root.geometry("300x250")
root.resizable(False, False)

frame1 = Frame(root, bg="White", width=100, height=100)
frame1.place(x=0, y=0)

firstblockRed = Frame(frame1, bg="#BB042B", width=90, height=90)
firstblockRed.place(x=0, y=0)

frame2 = Frame(root, bg="#001A5B", width=50, height=100)
frame2.place(x=100, y=0)



frame3 = Frame(root, bg="White", width=250, height=100)
frame3.place(x=150, y=0)

secondBlockRed = Frame(frame3, bg="#BB042B", width=240, height=90)
secondBlockRed.place(x=10, y=0)

frame4 = Frame(root, bg="#001A5B", height=50, width=300)
frame4.place(x=0, y=100)

frame5 = Frame(root, bg="White", width=100, height=100)
frame5.place(x=0, y=150)

thirdblockRed = Frame(frame5, bg="#BB042B", width=90, height=90)
thirdblockRed.place(x=0, y=10)

frame6 = Frame(root, bg="#001A5B", width=50, height=100)
frame6.place(x=100, y=150)



frame7 = Frame(root, bg="White", width=250, height=100)
frame7.place(x=150, y=150)

fourBlockRed = Frame(frame7, bg="#BB042B", width=240, height=90)
fourBlockRed.place(x=10, y=10)



root.mainloop()
