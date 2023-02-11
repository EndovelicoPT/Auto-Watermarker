from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# Create window
window = Tk()
window.title("Watermarker")
window.config(padx=50, pady=10)

# Pack window with logo and labels
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="camera.png")
logo = Label(image=logo_img)
logo.grid(row=1)
title = Label(text="Custom Watermark")
title.grid(row=2)
custom_watermark = Entry(window, justify='center')
custom_watermark.grid(row=3)


def uploadImg():
    global image
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select an Image", filetype=(("jpeg files", "*.jpg"), ("PNG  files", "*.png")))
    image = Image.open(filename)
    w, h = image.size
    x, y = int(w / 2), int(h / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x
    font = ImageFont.truetype("arial.ttf", int(font_size/20))
    draw = ImageDraw.Draw(image)

    # Add watermark
    draw.text((0, 0), custom_watermark.get(), fill=(0, 0, 0), font=font)
    image.show()


def savefile():
    files = [('JPG Files', '*.jpg'),
             ('PNG Files', '*.png')]
    filename = filedialog.asksaveasfile(
        filetypes=files, defaultextension=files)
    image.save(filename)


btn_upload_img = Button(text="Upload Image", bg="white", command=uploadImg)
btn_upload_img.grid(row=4, column=0)
btn_save = Button(text="Save", bg="white", command=savefile)
btn_save.grid(row=5, column=0)


window.mainloop()
