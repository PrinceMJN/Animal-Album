from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Animal Album")
#root.geometry("400x400")
root.iconbitmap('favicon.ico')

img1 = ImageTk.PhotoImage(Image.open("s_image/cheetah.jpg"))
img2 = ImageTk.PhotoImage(Image.open("s_image/lion.jpg"))
img3 = ImageTk.PhotoImage(Image.open("s_image/tiger.jpg"))

img_list = [img1, img2, img3]

status = Label(root, text="Image 1 0f " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=W)
my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(img_id):
    global my_label
    global next_bt
    global back_bt
    my_label.grid_forget()
    my_label = Label(image=img_list[img_id-1])
    my_label.grid(row=0, column=0, columnspan=3)
    next_bt = Button(root, text=">>", command=lambda: forward(img_id+1))
    back_bt = Button(root, text="<<", command=lambda: backward(img_id-1))

    if img_id == 3:
        next_bt = Button(root, text=">>", state=DISABLED)
    status = Label(root, text="Image " + str(img_id) +" 0f " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


    next_bt.grid(row=1, column=2)
    back_bt.grid(row=1, column=0)


def backward(img_id):
    global my_label
    global next_bt
    global back_bt
    my_label.grid_forget()
    my_label = Label(image=img_list[img_id - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    next_bt = Button(root, text=">>", command=lambda: forward(img_id + 1))
    back_bt = Button(root, text="<<", command=lambda: backward(img_id - 1))

    if img_id == 1:
        back_bt = Button(root, text="<<", state=DISABLED)

    next_bt.grid(row=1, column=2)
    back_bt.grid(row=1, column=0)
    status = Label(root, text="Image " + str(img_id) + " 0f " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

back_bt = Button(root, text="<<", state=DISABLED)
exit_bt = Button(root, text="Exit Program", command=root.quit)
next_bt = Button(root, text=">>", command=lambda: forward(2))

back_bt.grid(row=1, column=0)
exit_bt.grid(row=1, column=1)
next_bt.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
