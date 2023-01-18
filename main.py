import tkinter as tk
from tkinter import ttk, messagebox
from random import randint
import pyperclip, string

ambigous = ('"', "`", "'", '(', ')', '*', ',', '.', '/', "\\", ':', ';', '~', '<', '>', '[', ']', '{', '|', '}')
similar = ('e', 'g', 'i', 'I', 'l', 'L', 'o', 'O', '0', '1')
pw_generated = ''

# Generate random password from chosen symbols
def generate_password():
    global pw_generated
    # Create a tuple from chosen symbols
    chosen_ch = []
    if pw_symbols.get():
        chosen_ch += string.punctuation
    if pw_numbers.get():
        chosen_ch += string.digits
    if pw_lch.get():
        chosen_ch += string.ascii_lowercase
    if pw_uch.get():
        chosen_ch += string.ascii_uppercase
    if pw_simch.get():
        chosen_ch = list(set(chosen_ch) - set(similar))
    if pw_ambch.get():
        chosen_ch = list(set(chosen_ch) - set(ambigous))
    
    pw_generated = ''
    try:
        for i in range(pw_length.get()):
            pw_generated += chosen_ch[randint(0,len(chosen_ch)-1)]
        lbl_pw_generated.configure(text=pw_generated)
    except ValueError:
        messagebox.showwarning(title='test', message="Password can't be created")

def copy():
    pyperclip.copy(pw_generated)

root = tk.Tk()
root.title('Password Generator')
root.geometry('386x342')
#root.resizable(False, False)

lbl_pw_generated = tk.Label(root, text='Your new password', width=23, font='Arial 18 bold')
lbl_pw_generated.grid(row=0, column=0, pady=30)

img_btn_generate = tk.PhotoImage(file = r'generate.png')
tk.Button(root,
    image=img_btn_generate,
    command=generate_password,
    bd=0).grid(row=0, column=1)
img_btn_copy = tk.PhotoImage(file = r'copy.png')
tk.Button(root, image=img_btn_copy, command=copy).grid(row=0, column=2)
ttk.Separator(root, orient='horizontal').grid(row=1, column=0, columnspan=3, sticky='ew')

#main_frame = tk.Frame(root)
#main_frame.grid(row=1, column=0, columnspan=3)

tk.Label(root, text='Password length').grid(row=2, column=0, sticky='w')
pw_length = tk.IntVar()
scale_pw_length = tk.Scale(root, variable=pw_length, from_=4, to=20, length=120, orient='horizontal')
scale_pw_length.grid(row=2, column=1, columnspan=2, padx=(0, 5))
ttk.Separator(root, orient='horizontal').grid(row=3, column=0, columnspan=3, sticky='ew', pady=5)

# Include symbols option
pw_symbols = tk.BooleanVar()
pw_symbols.set(True)
tk.Label(root, text='Include symbols (e.g. @#$%!)').grid(row=4, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, variable = pw_symbols).grid(row=4, column=2, sticky='e')
ttk.Separator(root, orient='horizontal').grid(row=5, column=0, columnspan=3, sticky='ew', pady=5)

# Include numbers option
pw_numbers = tk.BooleanVar()
pw_numbers.set(True)
tk.Label(root, text='Include numbers (12345)').grid(row=6, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, variable = pw_numbers).grid(row=6, column=2, sticky='e')
ttk.Separator(root, orient='horizontal').grid(row=7, column=0, columnspan=3, sticky='ew', pady=5)

# Include lowercase characters option
pw_lch = tk.BooleanVar()
pw_lch.set(True)
tk.Label(root, text='Include lowercase characters (abcde)').grid(row=8, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, variable = pw_lch).grid(row=8, column=2, sticky='e')
ttk.Separator(root, orient='horizontal').grid(row=9, column=0, columnspan=3, sticky='ew', pady=5)

# Include uppercase characters option
pw_uch = tk.BooleanVar()
pw_uch.set(True)
tk.Label(root, text='Include uppercase characters (ABCDE)').grid(row=10, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, variable = pw_uch).grid(row=10, column=2, sticky='e')
ttk.Separator(root, orient='horizontal').grid(row=11, column=0, columnspan=3, sticky='ew', pady=5)

# Exclude similar characters option
pw_simch = tk.BooleanVar()
pw_simch.set(False)
tk.Label(root, text='Exclude similar characters (e.g. i l 1 0 o)').grid(row=12, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, variable = pw_simch).grid(row=12, column=2, sticky='e')
ttk.Separator(root, orient='horizontal').grid(row=13, column=0, columnspan=3, sticky='ew', pady=5)

# Exclude ambiguous characters option
pw_ambch = tk.BooleanVar()
pw_ambch.set(False)
tk.Label(root, text='Exclude ambiguous characters (e.g. { [ , ; < )').grid(row=14, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, variable = pw_ambch).grid(row=14, column=2, sticky='e')

root.mainloop()