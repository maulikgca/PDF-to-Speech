from PyPDF2 import PdfReader
import PyPDF2 as pdf
import pyttsx3
from tkinter import *
from tkinter import filedialog as fd

AskPath = Tk()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

AskPath.withdraw()
file_path = fd.askopenfilename(
    title="SELECT PDF",
    filetypes=(("PDF files", "*.pdf"),)
    )
AskPath.destroy()
AskPath.mainloop()
reader = PdfReader(file_path)

while True:
    engine.say("Enter the page number you want me to read")
    engine.runAndWait()
    page = reader.pages[(int(input("Enter the Page number you want me to read: ")))-1]
    text = page.extract_text()
    print(text)
    engine.say(text)
    engine.runAndWait()

    engine.say("Do you want me to repeat?")
    engine.runAndWait()
    x = input("Do you want me to repeat?(Y/N): ")

    while True:
        if x == "Y":
            engine.say("Enter the page number you want me to repeat")
            engine.runAndWait()
            page = reader.pages[(int(input("Enter the Page number you want me to repeat: ")))-1]
            text = page.extract_text()
            print(text)
            engine.say(text)
            engine.runAndWait()
            
            engine.say("Do you want me to read again?")
            engine.runAndWait()
            x = input("Do you want me to read again? (Y/N): ")
            
        elif x == "N":
            engine.say("Ok... No Problem. Thank You for using me")
            engine.runAndWait()
            break
    break
            