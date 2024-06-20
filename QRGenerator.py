from qrcode import QRCode
import pandas as pd

def generateQRs(excelData, saveFolder):
    totalQRGenerated = 0
    QRsNotGenerated = []
    for i in range(len(excelData)):
        if pd.isna(excelData.at[i, 'URL']):
            QRsNotGenerated.append(excelData.at[i, 'NAME'])
            continue
        qr = QRCode(version=1, box_size=10, border=5)
        data = excelData['URL'][i]
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f"{saveFolder}/{excelData['NAME'][i]}.png")
        totalQRGenerated += 1
    return totalQRGenerated


def readExcel(excelPath):
    excelData = pd.read_excel(excelPath)
    excelData = excelData.set_axis(['NAME', 'URL'], axis=1)
    return excelData