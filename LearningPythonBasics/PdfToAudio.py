import PyPDF2
import pyttsx3

# PDF File
path = open('pdfToOpen.pdf', 'rb')

# creating a pdf file reader object
pdfReader = PyPDF2.PdfFileReader(path)

# get an engine instance for the speech synthesis
speak = pyttsx3.init()


for pages in range(pdfReader.numPages):
    text = pdfReader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()


speak.stop()

# was provided from: clcoding.com
