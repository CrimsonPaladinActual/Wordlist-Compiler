import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def combine_password_lists(directory, output_file):
    passwords = set()
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
    
    total_files = len(files)
    for index, file in enumerate(files):
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                passwords.add(line.strip())
        progress_var.set((index + 1) / total_files * 100)
        root.update_idletasks()

    with open(output_file, 'w', encoding='utf-8') as f:
        for password in passwords:
            f.write(password + '\n')
    return len(passwords)

def browse_directory():
    directory = filedialog.askdirectory(title="Select Source Folder")
    if directory:
        source_folder_var.set(directory)

def browse_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        output_file_var.set(file_path)

def combine():
    source_folder = source_folder_var.get()
    output_file = output_file_var.get()
    
    if not source_folder or not output_file:
        messagebox.showwarning("Warning", "Please specify both source folder and output file.")
        return

    num_passwords = combine_password_lists(source_folder, output_file)
    progress_var.set(100)
    messagebox.showinfo("Success", f"Combined {num_passwords} unique passwords into {output_file}")
    progress_var.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password List Combiner")

    source_folder_var = tk.StringVar()
    output_file_var = tk.StringVar()
    progress_var = tk.DoubleVar()

    tk.Label(root, text="Source Folder:").pack(padx=20, pady=5, anchor="w")
    tk.Entry(root, textvariable=source_folder_var, width=50).pack(padx=20, pady=5, anchor="w")
    tk.Button(root, text="Browse...", command=browse_directory).pack(padx=20, pady=5, anchor="w")

    tk.Label(root, text="Output File:").pack(padx=20, pady=5, anchor="w")
    tk.Entry(root, textvariable=output_file_var, width=50).pack(padx=20, pady=5, anchor="w")
    tk.Button(root, text="Browse...", command=browse_output_file).pack(padx=20, pady=5, anchor="w")

    tk.Button(root, text="Combine Password Lists", command=combine).pack(padx=20, pady=20)
    
    progress_bar = ttk.Progressbar(root, variable=progress_var, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(padx=20, pady=5)

    root.mainloop()
