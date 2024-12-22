
import os
import tkinter as tk
from tkinter import ACTIVE, DISABLED, NORMAL, filedialog, messagebox, simpledialog
import re
from functions import caesar_code,decrypte_caesar_code
import subprocess

plain_text = ''
cipherText = ''
chiffre_btn = None
key_button = None
decrypt_button = None

def open_file():
    global key_button
    global chiffre_btn
    
    file_path = filedialog.askopenfilename()
    text = ''
    if os.path.getsize(file_path) == 0:
        messagebox.showwarning("Alert", "The file is empty!\nPlease try again.")
        return
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            # Check if the file contains numbers
            text = text.upper()
            print(text)
            global plain_text
            plain_text = text
            key_button.config(state=ACTIVE)
            

def open_filee():
    global decrypt_button 

    file_path = filedialog.askopenfilename()
    text = ''
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            # Check if the file contains numbers
            text = text.upper()
            print(text)
            global cipherText
            cipherText = text
            decrypt_button.config(state=ACTIVE)
                


def enter_key():
    global key_button
    global chiffre_btn

    # Prompt for the first number
    number1 = simpledialog.askinteger("Enter a Number", "Please enter the first number (1-25):")
    if number1 is None:  # User canceled the dialog
        return
    
    print(number1)

    # Check if the first number is valid
    if number1 < 0 or number1 > 25:
        messagebox.showwarning("Alert", "The first key should be between 1 and 25\nPlease try again.")
        chiffre_btn.config(state=DISABLED)
        return

    # Prompt for the second number
    number2 = simpledialog.askinteger("Enter a Number", "Please enter the second number (1-25):")
    if number2 is None:  # User canceled the dialog
        return

    print(number2)

    # Check if the second number is valid
    if number2 < 0 or number2 > 25:
        messagebox.showwarning("Alert", "The second key should be between 1 and 25\nPlease try again.")
        chiffre_btn.config(state=DISABLED)
        return

    # If both numbers are valid, store them and enable the button
    global key1
    global key2
    key1 = number1
    key2 = number2
    chiffre_btn.config(state=ACTIVE)

def encrypt_text():
    global plain_text
    plain_text = caesar_code(plain_text, key1,key2)
    print(plain_text)
    new_file_path = "encrypted_file.txt"
    with open(new_file_path, 'w') as file:
        # Write content to the file
        file.write(plain_text)
        subprocess.Popen(['notepad.exe', new_file_path])

def decrypt_text():
    global cipherText
    cipherText = decrypte_caesar_code(cipherText)
    new_file_path = "decrypted_file.txt"
    with open(new_file_path, 'w') as file:
        # Write content to the file
        file.write(cipherText)
        subprocess.Popen(['notepad.exe', new_file_path])




def page1():
    page1_window = tk.Toplevel(root)
    page1_window.geometry("800x800")  # Set the size of the window
    page1_window.title("Encrypt")
    page1_window.grab_set()

    global key_button
    global chiffre_btn

    select_button = tk.Button(page1_window, text="Select File", command=open_file, height=5, width=20, cursor="hand2")
    select_button.pack(padx=50, pady=50)

    key_button = tk.Button(page1_window, text="Enter the key", command=enter_key, state=DISABLED, height=5, width=20, cursor="hand2")
    key_button.pack(padx=50, pady=50)

    chiffre_btn = tk.Button(page1_window, text="Encrypt", command=encrypt_text, state=DISABLED, height=5, width=20, cursor="hand2")
    chiffre_btn.pack(padx=50, pady=50)

def page2():
    page2_window = tk.Toplevel(root)
    page2_window.geometry("800x800")  
    page2_window.title("Decipher")
    page2_window.grab_set()

    global decrypt_button

    select_button = tk.Button(page2_window, text="Select File", command=open_filee, height=5, width=20, cursor="hand2")
    select_button.pack(padx=50, pady=50)

    decrypt_button = tk.Button(page2_window, text="Decipher", command=decrypt_text, state=DISABLED, height=5, width=20, cursor="hand2")
    decrypt_button.pack(padx=50, pady=50)

root = tk.Tk()
root.geometry("600x600") 

encrypt_btn = tk.Button(root, text="Encrypt", command=page1, state=NORMAL, height=5, width=20, cursor="hand2")
encrypt_btn.pack(padx=50, pady=50, side="left")
decrypt_btn = tk.Button(root, text="Decrypt", command=page2, state=NORMAL, height=5, width=20, cursor="hand2")
decrypt_btn.pack(padx=50, pady=50, side="left")

root.mainloop()

#Author Tarek Triki