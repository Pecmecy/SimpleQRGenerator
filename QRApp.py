from tkinter import filedialog
import customtkinter
from QRGenerator import generateQRs, readExcel

class QRApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR Code Generator")
        self.geometry("1000x500")

        # self.button = customtkinter.CTkButton(self, text="Generate QR Codes", command=self.button_callback)
        self.button = customtkinter.CTkButton(self, text="Select file", command=self.selectFile)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.grid_columnconfigure(0, weight=1)

    def button_callback(self):
        print("Button clicked")

    def selectFile(self):
        fileName = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        print("Selected file: ")
        print(fileName)

app = QRApp()
app.mainloop()