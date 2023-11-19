# Script for E-reader
import tkinter as tk
    #this isthe GUI
from tkinter import filedialog
    #this opens up the file dialog windows
from PIL import Image, ImageTk
    #used to work on images in various formats
import fitz  # PyMuPDF

class EReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Reader Application")

        self.canvas = tk.Canvas(root)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.load_button = tk.Button(root, text="Open E-Book", command=self.load_ebook)
        self.load_button.pack(side=tk.BOTTOM)

        self.current_page = 0
        self.doc = None

    def load_ebook(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.doc = fitz.open(file_path)
            self.show_page()

    def show_page(self):
        page = self.doc.load_page(self.current_page)
        image = page.get_pixmap().to_image()

        imgtk = ImageTk.PhotoImage(image=image)
        self.canvas.config(width=imgtk.width(), height=imgtk.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

        self.root.title(f"E-Reader Application - Page {self.current_page + 1}")

    def next_page(self):
        if self.doc and self.current_page < self.doc.page_count - 1:
            self.current_page += 1
            self.show_page()

    def prev_page(self):
        if self.doc and self.current_page > 0:
            self.current_page -= 1
            self.show_page()


if __name__ == "__main__":
    root = tk.Tk()
    app = EReaderApp(root)

    next_button = tk.Button(root, text="Next Page", command=app.next_page)
    next_button.pack(side=tk.RIGHT)

    prev_button = tk.Button(root, text="Previous Page", command=app.prev_page)
    prev_button.pack(side=tk.LEFT)

    root.geometry("800x600")
    root.mainloop()
