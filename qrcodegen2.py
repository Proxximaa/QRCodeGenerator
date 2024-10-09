import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk
import subprocess
from io import BytesIO


qr = None


max_capacities = [
    25, 47, 77, 114, 154, 192, 224, 279, 335, 395,
    468, 535, 619, 667, 758, 883, 1024, 1108, 1252,
    1408, 1548, 1725, 1882, 2048, 2240, 2620, 2953,
    3384, 4043, 4800, 5520, 6240, 7089, 7958, 8838,
    9719, 10600, 11583, 12566, 13551, 14630, 15811,
    17095, 18581, 20068, 21657
]


def generate_qr():
    global qr
    data = data_entry.get()
    version = int(version_dropdown.get())

    if not data:
        messagebox.showerror("Input Error", "Please enter some data!")
        return


    max_capacity = max_capacities[version - 1]


    if len(data) > max_capacity:
        version += 1
        if version > 40:
            messagebox.showerror("Version Error", "Data is too large for QR Code version 40!")
            return
        version_dropdown.set(version)
        messagebox.showinfo("Version Changed", f"Switched to QR Code version {version} due to data size.")


    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)


    img = qr.make_image(fill='black', back_color='white')
    update_image(img)


def update_image(img):
    global img_tk
    img = img.resize((current_size, current_size))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk


def increase_size():
    global current_size
    current_size += 20
    update_image(qr.make_image(fill='black', back_color='white'))

def decrease_size():
    global current_size
    if current_size > 20:
        current_size -= 20
        update_image(qr.make_image(fill='black', back_color='white'))


def copy_qr_to_clipboard():
    if qr is None:
        messagebox.showerror("Error", "Please generate a QR code first!")
        return

    img = qr.make_image(fill='black', back_color='white')


    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)


    try:
        subprocess.run(["xclip", "-selection", "clipboard", "-t", "image/png"], input=img_byte_arr.read(), text=False, check=True)
        messagebox.showinfo("Success", "QR Code copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy QR code to clipboard: {e}")


root = tk.Tk()
root.title("QR Code Generator")


current_size = 300


tk.Label(root, text="Enter Data:").grid(row=0, column=0, padx=10, pady=10)
data_entry = tk.Entry(root, width=40)
data_entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(root, text="Select Version:").grid(row=1, column=0, padx=10, pady=10)
version_dropdown = ttk.Combobox(root, values=[str(i) for i in range(1, 41)])
version_dropdown.grid(row=1, column=1, padx=10, pady=10)
version_dropdown.current(0)


generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)


copy_button = tk.Button(root, text="Copy QR Code", command=copy_qr_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)


qr_label = tk.Label(root)
qr_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


size_frame = tk.Frame(root)
size_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
increase_button = tk.Button(size_frame, text="+", command=increase_size)
increase_button.pack(side=tk.LEFT)
decrease_button = tk.Button(size_frame, text="-", command=decrease_size)
decrease_button.pack(side=tk.LEFT)


root.mainloop()
