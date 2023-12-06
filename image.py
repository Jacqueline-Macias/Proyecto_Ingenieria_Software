from PIL import Image, ImageTk

def open_image(name,x,y):
    img = Image.open(name)
    new_img = img.resize((x,y))
    return ImageTk.PhotoImage(new_img)




