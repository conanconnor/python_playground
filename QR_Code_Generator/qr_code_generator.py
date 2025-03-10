import tkinter as tk
from tkinter import colorchooser
import qrcode
from PIL import Image, ImageTk

def generate_qr(): 
    website_link = url_entry.get().strip()

    if not website_link:
        status_label.config(text="Error: Please enter a valid URL.", fg="red")
        return

    filename = filename_entry.get().strip() if filename_entry.get().strip() else 'generated_qrcode'
    file_format = format_var.get()
    box_size = int(box_size_entry.get()) if box_size_entry.get().strip() else 5 
    border = int(border_entry.get()) if border_entry.get().strip() else 5
    foreground_color = foreground_color_var.get() if foreground_color_var.get() else "#000000"
    background_color = background_color_var.get() if background_color_var.get() else "#FFFFFF"

    qr = qrcode.QRCode(version=1, box_size=box_size, border=border)
    qr.add_data(website_link)
    qr.make()

    img = qr.make_image(fill_color=foreground_color, back_color=background_color)
    img_tk = ImageTk.PhotoImage(img)

    label.config(image=img_tk)
    label.image = img_tk

    if save_var.get() == 1:
        try:
            if file_format == "JPG":
                img = img.convert("RGB")
                img.save(f"{filename}.jpg", "JPEG")
                status_label.config(text=f"QR code saved as '{filename}.jpg'", fg="green")
            else:
                img.save(f"{filename}.png")
                status_label.config(text=f"QR code saved as '{filename}.png'", fg="green")
        except Exception as e:
            status_label.config(text=f"Error saving QR code: {e}", fg="red")
    else:
        status_label.config(text="QR code generated (not saved)", fg="darkgray")

def choose_foreground_color():
    color_code = colorchooser.askcolor(title="Choose Foreground Color")[1]
    if color_code:
        foreground_color_var.set(color_code)

def choose_background_color():
    color_code = colorchooser.askcolor(title="Choose Background Color")[1]
    if color_code:
        background_color_var.set(color_code)

# UI
root = tk.Tk()
root.title('QR Code Generator')

url_label = tk.Label(root, text="Enter a URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)

filename_label = tk.Label(root, text="Enter filename (without extension):")
filename_label.pack(pady=5)
filename_entry = tk.Entry(root, width=40)
filename_entry.pack(pady=5)

box_size_label = tk.Label(root, text="Enter Box Size (default 5, optional):")
box_size_label.pack(pady=5)
box_size_entry = tk.Entry(root, width=10)
box_size_entry.insert(0, "5") 
box_size_entry.pack(pady=5)

border_label = tk.Label(root, text="Enter Border Size (default 5, optional):")
border_label.pack(pady=5)
border_entry = tk.Entry(root, width=10)
border_entry.insert(0, "5")
border_entry.pack(pady=5)

foreground_color_var = tk.StringVar()
foreground_color_button = tk.Button(root, text="Choose Foreground Color (default black)", command=choose_foreground_color)
foreground_color_button.pack(pady=5)
background_color_var = tk.StringVar()
background_color_button = tk.Button(root, text="Choose Background Color (default white)", command=choose_background_color)
background_color_button.pack(pady=5)

save_var = tk.IntVar()
save_checkbox = tk.Checkbutton(root, text="Save QR code?", variable=save_var)
save_checkbox.pack(pady=5)

format_label = tk.Label(root, text="Select file format (default PNG):")
format_label.pack(pady=5)
format_var = tk.StringVar()
format_var.set("PNG")
format_dropdown = tk.OptionMenu(root, format_var, "PNG", "JPG")
format_dropdown.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

label = tk.Label(root)
label.pack(pady=20)

status_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), fg="darkgray")
status_label.pack(pady=5)

root.mainloop()