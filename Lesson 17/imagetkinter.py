# PIL (Python Imaging Library) provides image editing capabilities to the python interpreter
from tkinter import *
from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry as well
root = Tk()
root.title("image")
root.geometry("400x400")

# Now use Image.open to open and identify the given image file.
upload = Image.open("C:\\Users\\imran\\OneDrive\\Documents\\Python course\\Lesson 17\\Image.png")

# Convert this image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label
label = Label(root, image=image, height=500, width=500)
label.place(x=50, y=0)
label12 = Label(root, text="This is how you add image in Tkinter Window")
label12.place(x=40, y=360)

# Run the application
root.mainloop()