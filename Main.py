import QRCodeGenerator as QR
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    app = QR.QRCodeGenerator(root)
    root.mainloop()