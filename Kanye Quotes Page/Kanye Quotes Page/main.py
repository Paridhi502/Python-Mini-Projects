from tkinter import *
from PIL import Image, ImageTk
import requests
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(canvas_text, text=quote)
window = Tk()
window.title("Kanye Says..")
window.config(padx=50, pady=50)

# Load and resize the image
image_path = 'quote.png'
try:
    original_image = Image.open(image_path)
    resized_image = original_image.resize((300, 300), Image.Resampling.LANCZOS)
    background_image = ImageTk.PhotoImage(resized_image)

    canvas = Canvas(window, width=300, height=300)
    canvas_create = canvas.create_image(150, 150, image=background_image)

    canvas_text = canvas.create_text(150, 130, text=' ',width=150, font=("Arial", 10, "bold"))
    canvas.grid(row=0, column=0)

    kanye_img = PhotoImage(file="kanye.png")
    kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

except Exception as e:
    print(f"Failed to load image: {e}")


window.mainloop()
