import raw_to_bmp as RTB
import tkinter as tk
from tkinter import ttk

def convert_raw_to_bmp():
    input_file = entry_input.get()
    output_file = entry_output.get()
    width = int(entry_width.get())
    height = int(entry_height.get())

    RTB.raw_to_bmp(input_file, output_file, width, height)

root = tk.Tk()
root.title("RAW to BMP Converter")

# Make window full screen
root.state('zoomed')  # For Windows full screen
# root.attributes('-fullscreen', True)  # Uncomment for true fullscreen (esc to exit)

# Dark mode colors
bg_color = '#23272e'
fg_color = '#f8f8f2'
entry_bg = '#282c34'
button_bg = '#44475a'
button_fg = '#f8f8f2'

root.configure(bg=bg_color)

style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background=bg_color)
style.configure('TLabel', background=bg_color, foreground=fg_color, font=('Segoe UI', 12))
style.configure('TButton', background=button_bg, foreground=button_fg, font=('Segoe UI', 12, 'bold'))
# Rounded corners for entries (ttk only, not classic tk.Entry)
style.element_create('RoundedEntry.border', 'from', 'clam')
style.layout('RoundedEntry.TEntry', [
    ('RoundedEntry.border', {'children': [
        ('Entry.padding', {'children': [
            ('Entry.textarea', {'sticky': 'nswe'})
        ], 'sticky': 'nswe'})
    ], 'sticky': 'nswe'})
])
style.configure('RoundedEntry.TEntry',
    fieldbackground=entry_bg, background=entry_bg, foreground=fg_color, borderwidth=2, relief='flat', padding=8, font=('Segoe UI', 12), bordercolor='#44475a')

# Center everything using a container frame
container = ttk.Frame(root, style='TFrame')
container.pack(expand=True)

# Title at the top
title_label = ttk.Label(container, text="RAW to BMP Converter", style='TLabel', font=('Segoe UI', 24, 'bold'))
title_label.pack(pady=(40, 30))

# Form frame centered
frame = ttk.Frame(container, padding=40, style='TFrame')
frame.pack(expand=True)

label_input = ttk.Label(frame, text="Input RAW file:", style='TLabel')
label_input.grid(row=0, column=0, sticky='e', pady=10, padx=10)
entry_input = ttk.Entry(frame, style='RoundedEntry.TEntry')
entry_input.grid(row=0, column=1, sticky='ew', pady=10, padx=10)

label_output = ttk.Label(frame, text="Output BMP file:", style='TLabel')
label_output.grid(row=1, column=0, sticky='e', pady=10, padx=10)
entry_output = ttk.Entry(frame, style='RoundedEntry.TEntry')
entry_output.grid(row=1, column=1, sticky='ew', pady=10, padx=10)

label_width = ttk.Label(frame, text="Width:", style='TLabel')
label_width.grid(row=2, column=0, sticky='e', pady=10, padx=10)
entry_width = ttk.Entry(frame, style='RoundedEntry.TEntry')
entry_width.grid(row=2, column=1, sticky='ew', pady=10, padx=10)

label_height = ttk.Label(frame, text="Height:", style='TLabel')
label_height.grid(row=3, column=0, sticky='e', pady=10, padx=10)
entry_height = ttk.Entry(frame, style='RoundedEntry.TEntry')
entry_height.grid(row=3, column=1, sticky='ew', pady=10, padx=10)

button_convert = ttk.Button(frame, text="Convert", command=convert_raw_to_bmp, style='TButton')
button_convert.grid(row=4, column=0, columnspan=2, pady=20)

# Make columns expand
frame.columnconfigure(1, weight=1)

root.mainloop()