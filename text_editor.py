import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# open file function
def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    
    window.title(f"Open File: {filepath}")

# save file function
def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)

    window.title(f"Open File: {filepath}")

# main function
def main():

    # configuring the window
    window = tk.Tk()
    window.title("text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    # configuring the widgets
    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)

    # configuring the buttons
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))

    # adding buttons & frame to the grid
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    # adding keyboard shortcuts for saving & opening files
    window.bind("<Command-s>", lambda x: save_file(window, text_edit))
    window.bind("<Command-o>", lambda y: open_file(window, text_edit))


    window.mainloop()

main()