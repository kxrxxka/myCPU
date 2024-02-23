import psutil
import random
from tkinter import *
from PIL import Image, ImageTk

def update_number():
     label2.config(text = "CPU load: " + str(psutil.cpu_percent()) + "%")

     label4.config(text = "Memory load: " + str(psutil.virtual_memory().percent) + "%")

     label6.config(text = "Disk usage:" + str(psutil.disk_usage("/").used // 1000000000) + 'GB / ' + str(psutil.disk_usage("/").total // 1000000000) + 'GB')

     window.after(1000, update_number)
    

window = Tk()


image_file = Image.open("icons8-cpu-50 (1).png")
image_file2 = Image.open("icons8-ram-60.png")
image_file3 = Image.open("icons8-c-drive-2-50.png")

cpu_image = ImageTk.PhotoImage(image_file)
ram_image = ImageTk.PhotoImage(image_file2)
space_image = ImageTk.PhotoImage(image_file3)


label1 = Label(window, image = cpu_image)
label1.grid(row = 0, column = 0)

label2 = Label(window, font = ("Comic Sans MS", 25), text = "CPU load: " + str(psutil.cpu_percent()) + "%")
label2.grid(row = 0, column = 1)

label3 = Label(window, image = ram_image)
label3.grid(row = 1, column = 0)

label4 = Label(window, font = ("Comic Sans MS", 25), text = "Memory load: " + str(psutil.virtual_memory().percent) + "%")
label4.grid(row = 1, column = 1)

label5 = Label(window, image = space_image)
label5.grid(row = 2, column = 0)

label6 = Label(window, font = ("Comic Sans MS", 25), text = "Disk usage:" + str(psutil.disk_usage("/").used // 1000000000) + 'GB / ' + str(psutil.disk_usage("/").total // 1000000000) + 'GB')
label6.grid(row = 2, column = 1)


window.after(1000, update_number)

mainloop()

