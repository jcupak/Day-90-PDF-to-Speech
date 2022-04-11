############################################################################
# 100 Days of Code - The Complete Python Pro Bootcamp for 2021             #
# PDF to Speech                                                            #
# Reads and speaks text from PDF file when given file name and page number #
# Requires installation of pyPDF2 to read PDF and pyttsx3 to speak         #
# Course Instructor: Angela Yu                                             #
# Coded by: John Cupak cupakj@acm.org                                      #
# History: 2022-04-11 Completed with source citations                      #
############################################################################

import PyPDF2
import pyttsx3


def get_pdf_information(filename):
    """Returns PDF file metadata

    The function reads the filename, formats and prints the metadata, and returns the file information.

    The function is based on the section "How to Extract Document Information From a PDF in Python"
    from April 19, 2019 article by Mike Driscoll "How to Work With a PDF in Python",
    at https://realpython.com/pdf-python/

    Parameters
    ----------
    filename: str
        The path to the file to read
    """
    #

    with open(filename, 'rb') as file:

        pdf = PyPDF2.PdfFileReader(file)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

        info = f"""
        Author:   {information.author}
        Creator:  {information.creator}
        Producer: {information.producer}
        Subject:  {information.subject}
        Title:    {information.title}
        Pages:    {number_of_pages}
        """

        print(info)
        return information


def speak_pdf(filename, page_number=0):
    """
    Convert PDF File Text to Audio Speech using Python

    Based on https://www.geeksforgeeks.org/convert-pdf-file-text-to-audio-speech-using-python/

    :param filename: str
        The path of the file to read
    :param page_number: int, optional
        The page number of the file to speak (default is 0)
    """


    file = open(filename, 'rb')
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(page_number)
    text = page.extractText()

    # read the text
    speak = pyttsx3.init()
    speak.setProperty('rate', 160)  # Set speech rate a little slower
    voices = speak.getProperty('voices')
    speak.setProperty('voice', voices[0].id)  # Change to male voice
    speak.say(text)
    speak.runAndWait()

    speak.stop()


if __name__ == '__main__':

    pdfFile = 'files/minutes.pdf'

    get_pdf_information(pdfFile)
    speak_pdf(pdfFile)
