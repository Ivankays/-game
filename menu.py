from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets menu")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def del_esc(event):
    window.destroy()

window = Tk()
window.title('Hexxagon')
window.iconphoto(True, PhotoImage(file='picture/Group 6.png'))
window.bind("<Escape>", del_esc)

window_width = 720
window_height = 480

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

window.attributes('-topmost', True)
window.focus_force()

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=480,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    365.3076970693364,
    244.51054739952087,
    image=image_image_1
)

def open_game():
    window.destroy()
    subprocess.Popen(['python', 'select.py'])

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_game,
    relief="flat"
)
button_1.place(
    x=500.0,
    y=250.0,
    width=170.0,
    height=80.0
)

window.resizable(False, False)
window.mainloop()