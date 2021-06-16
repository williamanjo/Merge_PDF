from PyPDF2 import PdfFileMerger, PdfFileReader
import os

# Pegando o nome dos arquivos 
arquivo = open("list.txt","r",encoding='utf-8')
name_file = arquivo.read()
arquivo.close()
filenames = name_file.splitlines()
arquivo.close()
# Loop nos nomes dos arquivos
for pdfName in filenames:
    mergedObject = PdfFileMerger() # Call the PdfFileMerger
    print(pdfName)

    try:
        # Loop nos arquivo-$(number)

        for fileNumber in range(1, 7):
            mergedObject.append(PdfFileReader('C:\\Users\\william.silva\\Downloads\\Res\\'+ pdfName +'-' + str(fileNumber)+ '.pdf', 'rb'))
    except:
        print(fileNumber)
    finally:
        # Gerando o arquivo Merged
        mergedObject.write("C:\\Users\\william.silva\\Downloads\\Res-merged\\" + pdfName + ".pdf")
        # Limpando a referencia do objeto
        mergedObject = None
