import tkinter as tk
from tkinter import filedialog

def file_select(title="Select a file"):
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename(
        title=title,
        filetypes=[("Ktape file", "*.ktape.ckd"), ("All files", "*.*")]
    )
    root.destroy()
    return file if file else None

