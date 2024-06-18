import os
from os.path import isfile, join
from qrcode import QRCode
import pandas as pd
from dotenv import load_dotenv

def generateQRs(excelData):
    for i in range(len(excelData)):
        qr = QRCode(version=1, box_size=10, border=5)
        data = excelData["URL"][i]
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        savePath = os.environ["SAVE_PATH"]
        img.save(f"{savePath}/{excelData['NAME'][i]}.png")

def readExcel(excelPath):
    excelData = pd.read_excel(excelPath)
    return excelData

def main():
    load_dotenv()
    excelPath = os.environ["EXCEL_PATH"] # Path to the excel file
    excelData = readExcel(excelPath)
    print(excelData)
    generateQRs(excelData)