from PyPDF2 import PdfFileMerger, PdfFileReader
import os
from tkinter import filedialog , messagebox
from tkinter import *

all_files = []
filenames = []
filesNames = []
root = Tk()
root.withdraw()

while(True):
    Directory = filedialog.askdirectory(title ="Selecione a Pasta Que Contêm Os Arquivos (*.pdf)")
    if(messagebox.askokcancel(title="Pasta Que Contêm Os Arquivos (*.pdf)", message=Directory)):
        break


for dirpath, dirnames, filenames in os.walk(Directory):
    for filename in [f for f in filenames if (f.endswith(".pdf") or f.endswith(".PDF")) ]:
        all_files.append(os.path.join(filename))

for i in all_files : 
    if (i.endswith("-1.pdf")):
        filesNames.append(i.replace("-1.pdf",""))
# Loop nos nomes dos arquivos
while(True):
    DirectorySaved = filedialog.askdirectory(title ="Selecione a Pasta Para salvar os Arquivos (*.pdf)")
    if(messagebox.askokcancel(title="Pasta Para salvar os Arquivos (*.pdf)", message=DirectorySaved)):
        break
    
if(messagebox.askquestion (title="", message="Carregar de : " + Directory +"\n" + "Salvar Em : " + DirectorySaved,icon = 'warning') == "yes"):
    for pdfName in filesNames:
        mergedObject = PdfFileMerger() # Call the PdfFileMerger

        try:
            # Loop nos arquivo-$(number)

            for fileNumber in range(1, 7):
                mergedObject.append(PdfFileReader(Directory +'\\'+ pdfName +'-' + str(fileNumber)+ '.pdf', 'rb'))
        except:
            print(pdfName + " - Pag's - " + str(fileNumber-1))
        finally:
        
            mergedObject.write(DirectorySaved +"\\" + pdfName + ".pdf")
            # Limpando a referencia do objeto
            mergedObject = None
            
