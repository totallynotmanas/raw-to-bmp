import raw_to_bmp as RTB
import tkinter as tk

def convert_raw_to_bmp():
    input_file = entry_input.get()
    output_file = entry_output.get()
    width = int(entry_width.get())
    height = int(entry_height.get())

    RTB.raw_to_bmp(input_file, output_file, width, height)

root = tk.Tk()
root.title("RAW to BMP Converter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_input = tk.Label(frame, text="Input RAW file:")
label_input.grid(row=0, column=0)
entry_input = tk.Entry(frame)
entry_input.grid(row=0, column=1)

label_output = tk.Label(frame, text="Output BMP file:")
label_output.grid(row=1, column=0)
entry_output = tk.Entry(frame)
entry_output.grid(row=1, column=1)

label_width = tk.Label(frame, text="Width:")
label_width.grid(row=2, column=0)
entry_width = tk.Entry(frame)
entry_width.grid(row=2, column=1)

label_height = tk.Label(frame, text="Height:")
label_height.grid(row=3, column=0)
entry_height = tk.Entry(frame)
entry_height.grid(row=3, column=1)

button_convert = tk.Button(frame, text="Convert", command=convert_raw_to_bmp)
button_convert.grid(row=4, columnspan=2)

root.mainloop()