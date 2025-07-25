import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk


root=tk.Tk()
root.title("Image Resizer")

def open_image():
    file_path=filedialog.askopenfilename(filetypes=[("Image Files","*jpg *jpeg *png")])
    
    if file_path:
        image=Image.open(file_path)
        canvas.image=ImageTk.PhotoImage(image)
        canvas.create_image(0,0,anchor=tk.NW,image=canvas.image)
        save_button.configure(state=tk.NORMAL)
        resize_button.configure(state=tk.NORMAL)
        root.image=image
def resize_image():
    try:
        width=int(width_entry.get())
        height=int(height_entry.get())
        image=root.image.resize((width,height))
        canvas.image=ImageTk.PhotoImage(image)
        canvas.create_image(0,0,anchor=tk.NW,image=canvas.image)
                  
    except(ValueError,AttributeError,OSError):
        status_label.configure(text="Error:Invailed dimention or no image ")
def save_image():
    file_path=filedialog.asksaveasfilename(defaultextension=".jpg",filetypes=[("JPEG","*jpg"),("PNG","*.png")])
    if file_path:
        try:
            image=root.image.resize((int(width_entry.get()),int(height_entry.get())))
            image.save(file_path)
            status_label.configure(text="Image saved successfully")
        except(ValueError,AttributeError,OSError):
            status_label.configure(text="Error:failed to save image")
   

width_label=tk.Label(root,text="width:")
width_label.pack()
width_entry=tk.Entry(root)
width_entry.pack()

height_label=tk.Label(root,text="Height:")
height_label.pack()
height_entry=tk.Entry(root)
height_entry.pack()


open_button=tk.Button(root,text="Open Image",command=open_image)
open_button.pack()

resize_button=tk.Button(root,text="Resize Image",command=resize_image,state=tk.DISABLED)
resize_button.pack()

canvas=tk.Canvas(root,width=400,height=400)
canvas.pack()

save_button=tk.Button(root,text="Save Image",command=save_image,state=tk.DISABLED)
save_button.pack()
status_label=tk.Label(root,text="")
status_label.pack()
root.mainloop()