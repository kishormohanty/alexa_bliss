from tkinter import *
from PIL import ImageTk,Image
root = Tk()
canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D://factory ms//image.png"))
canvas.create_image(20, 20, anchor=NW, image=img)
root.mainloop()