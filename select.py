from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"rules\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def del_esc(event):
    window.destroy()
    
window = Tk()
window.title('Hexxagon')
window.iconphoto(True,  PhotoImage(file='picture/Group 6.png'))

window_width = 720
window_height = 480
window.geometry("720x480")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.bind("<Escape>", del_esc)

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

window.attributes('-topmost', True)
window.focus_force()

canvas = Canvas(
    window,
    bg = "#111111",
    height = 480,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_1 = canvas.create_image(
    365.3076970693364,
    244.51054739952087,
    image=image_image_1
)
image_image_1 = PhotoImage(
    file=relative_to_assets("select.png"))
image_1 = canvas.create_image(
    360,
    200,
    image=image_image_1
)

def lvl1():
    window.destroy()
    subprocess.Popen(['python', 'Hexxagon.py'])
button_image_1 = PhotoImage(
    file=relative_to_assets("lvl1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:(lvl1()),
    relief="flat"
)
button_1.place(
    x=200.0,
    y=300.0,
    width=119.0,
    height=33.0
)
def lvl2():
    window.destroy()
    subprocess.Popen(['python', 'Hexxagon copy.py'])
button_image_2 = PhotoImage(
    file=relative_to_assets("lvl2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:(lvl2()),
    relief="flat"
)
button_2.place(
    x=400.0,
    y=300.0,
    width=119.0,
    height=33.0
)

window.resizable(False, False)
window.mainloop()
