from tkinter import filedialog, StringVar
import customtkinter
from QRGenerator import generateQRs, readExcel

class QRApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.FolderSelected = False
        self.FileSelected = False

        self.title("QR Code Generator")
        self.geometry("700x480")
        self.resizable(False, False)       
        
        self.title = customtkinter.CTkLabel(self, text="QR Code Generator", font=("Arial", 24))
        self.title.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.button = customtkinter.CTkButton(self, text="Select file", command=self.selectFile)
        self.button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.fileNameVar = customtkinter.StringVar()
        self.l1 = customtkinter.CTkLabel(self, textvariable=self.fileNameVar)
        self.l1.grid(row=2, column=0, padx=20, pady=0, sticky="ew")
        self.fileNameVar.set("No file selected")

        self.button2 = customtkinter.CTkButton(self, text="Select folder to save QRs", command=self.selectFolder)
        self.button2.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        self.folderNameVar = customtkinter.StringVar()
        self.l2 = customtkinter.CTkLabel(self, textvariable=self.folderNameVar)
        self.l2.grid(row=4, column=0, padx=20, pady=0, sticky="ew")
        self.folderNameVar.set("No folder selected")


        self.button3 = customtkinter.CTkButton(self, text="Generate QR Codes", command=self.generateQRs)
        self.button3.grid(row=5, column=0, padx=20, pady=20, sticky="ew")
        self.message = customtkinter.StringVar()
        self.l3 = customtkinter.CTkLabel(self, textvariable=self.message)
        self.l3.grid(row=6, column=0, padx=20, pady=0, sticky="ew")
        self.message.set("Please select an Excel file and a folder to generate the QR Codes")

        self.button4 = customtkinter.CTkButton(self, text="Exit", command=self.destroy)
        self.button4.grid(row=7, column=0, padx=20, pady=50, sticky="ew")        
        self.grid_columnconfigure(0, weight=1)

    def button_callback(self):
        print("Button clicked")

    def selectFile(self):
        fileName = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")], initialdir=".")
        if fileName:
            self.fileNameVar.set(fileName)
            self.fileName = fileName
            self.FileSelected = True
        
    def selectFolder(self):
        folderName = filedialog.askdirectory()
        if folderName:
            self.folderNameVar.set(folderName)
            self.folderName = folderName
            self.FolderSelected = True

    def generateQRs(self):
        if self.FileSelected and self.FolderSelected:
            self.message.set("Generating QR Codes...")
            self.l3.configure(text_color="blue")
            excelData = readExcel(self.fileName)
            totalQRs = generateQRs(excelData, self.folderName)
            self.message.set(f"{totalQRs} QR Codes generated successfully!")
            self.l3.configure(text_color="green")
        
        else:
            self.message.set("Please select an Excel file and a folder to generate the QR Codes")
            self.l3.configure(text_color="red")


app = QRApp()
app.mainloop()