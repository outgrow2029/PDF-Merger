import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from pypdf import PdfWriter

def merge_pdfs(input_files, output_path):
    try:
        merger = PdfWriter()
        for pdf in input_files:
            merger.append(pdf)
        
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success!", f"Merged {len(input_files)} PDFs successfully!\n\nSaved to: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def handle_drop(event):
    # tkinterdnd2 returns a string of file paths. We split them into a list.
    files = root.tk.splitlist(event.data)
    
    # Filter to make sure we only try to merge PDFs
    pdf_files = [f for f in files if f.lower().endswith('.pdf')]
    
    if len(pdf_files) < 2:
        messagebox.showwarning("Hold up", "Please drop at least TWO PDF files to merge.")
        return

    # Prompt the user for WHERE to save and WHAT to name it
    output_path = filedialog.asksaveasfilename(
        title="Save Merged PDF As...",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    # If the user didn't hit 'Cancel' on the save menu, proceed with merging
    if output_path:
        merge_pdfs(pdf_files, output_path)

# --- App Setup ---
# We use TkinterDnD.Tk() instead of standard tk.Tk() to enable drag/drop
root = TkinterDnD.Tk()
root.title("Quick PDF Merger")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Create a big drop zone label
drop_zone = tk.Label(
    root, 
    text="Drop PDF Files Here\n📄⬇️", 
    font=("Helvetica", 16, "bold"), 
    bg="#e0e0e0", 
    relief="groove",
    borderwidth=4
)
drop_zone.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Register the label to accept dropped files
drop_zone.drop_target_register(DND_FILES)
drop_zone.dnd_bind('<<Drop>>', handle_drop)

# Start the app
root.mainloop()