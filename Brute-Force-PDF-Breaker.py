# password breaker - will break into any encrypted PDF document that has a password that is one english word.

"""
Using the file-reading skills from the Chapter 8, we can create a list of word strings by reading the provided file (dictionary). We start by looping 
over each word in the list, and passing it to the decrypt() method. If this method returns an integer of 0, the password was wrong and the program 
shall continue to the next password.If decrypt() returns 1, then the program shall break out of the loop and print the hacked password, throughout this
process we maked sure to try both the Uppercase and lowercase forms.
"""

import PyPDF2
import os
import time as t

""" 
    By using the path methods provided by the os library we can make the program universal as anyone can run it in their corresponded machine without
any hussle with the directories.

    The PDFroots is an empty initialised list that stores all our found pdfs in the provided folder,so it can be accessed later on by the programme 
from the user inputed choice.
"""

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "PUT YOUR PDF HERE !!")
PDFroots = []

"""[Decrypt_pdf] Arguments(An encrypted PDF file, A list of potiential passwords)
    
    The function start by checking if the pdf is encrypted, by returning True it processeds to go through the inside code otherwise if it gives
False it prints a message to the user informing him that the pdf is accessable without the need of a password.
    
    This is where all the magic happens as the loop will begin by iterating over each word in the passed list while printing a message at the beginning 
so the user knows the program is still running since it can take a while for the program to complete, depending on your word,if decrypt returns a 1 in
eiher cases then it's a success braking out of the loop.
    
    The time taken to find the password is given wit hthe help of methods in the time module, giving the user an idea of how easy a password can be
cracked using the right tools.
"""


def Decrypt_pdf(encrypted_pdf, list_of_words):
    if encrypted_pdf.isEncrypted:
        t1 = t.time()
        for word in list_of_words:
            print('Trying to break in with ' + word + '...')
            t2 = t.time()
            if encrypted_pdf.decrypt(word) == 1:
                print('-'*100, '\nCongratulations! The password was uppercased "' +
                      word + '" found in ', t.strftime("%H h: %M m: %S s", t.gmtime(t2-t1)), '!\n', '-'*100)
                break
            elif encrypted_pdf.decrypt(word.lower()) == 1:
                print('-'*100, '\nCongratulations! The password was lowercased "' +
                      word.lower() + '" found in ', t.strftime("%H h: %M m: %S s", t.gmtime(t2-t1)), '!\n', '-'*100)
                break
        else:
            print('-'*100, '\nCould not determine the password\n', '-'*100)
    else:
        print(
            '-'*100, '\nthe file is not ENCRYPTED and can be accessed witout a password !!\n', '-'*100)

    """[interface] Arguments(none)
    This is what the user sees, as the foundPDF is a boolen which used as a flag to check if there's any PDF in the folder.
upon not finding any it informs the user that the folder is empty.
    The function returns a boolen given by the foundPDF state which is checked later on in the main function.
    """


def interface():
    foundPDF = False
    pdf_index = 0
    print('-'*100, '\nThis programme will try to decrypt your encrypted pdf files in the provided folder.\n',
          '-'*100, '\nName', '\t'*10, 'Encrypted\n', '-'*100)
    # this loop is able to filter any unwanted files as it catches only files ending with .pdf and appending them to the PDF
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".pdf") == 1:
                    # we always need to test our pdf files before passing them as some can be corrupted.
                    testpdf = open(root+'//'+file, 'rb')
                    test_pdf_reader = PyPDF2.PdfFileReader(testpdf)
                    foundPDF = True
                    print(f'[{pdf_index}] --> '+file+'\r' + '\t' *
                          10 + str(test_pdf_reader.isEncrypted))
                    # appending the full path of each pdf found to the list so it can be used later.
                    PDFroots.append(root+'//'+file)
                    pdf_index += 1
                    testpdf.close()
    except Exception as exc:
        print(
            '-'*100, "\nsomething went wrong with the Pdf, Try checking the pdfs in the folder are correct !\n", '-'*100)

    if foundPDF == False:
        print('-'*100, "\nno file found under the extension of PDF, try adding some pdf files !\n", '-'*100)
        return False
    else:
        print('-'*100, '\nchoose a Pdf to decrypt by providing the index : ...')
        return True


"""[main]
    Now to our main function, it's a composition of all the defined function above.
"""

if __name__ == '__main__':
    # Opening the text file and using read and split for each word
    text = open(os.path.join(my_path, "dictionary.txt"))
    text = text.read()
    text = text.split('\n')
    # nextmove will grab the user input for exiting the programme.
    nextmove = ''

    while(nextmove.lower() != 'q'):
        # checking the interface output, to see if it can processed to the next part of the code or just break out of it.
        if interface() == True:
            while(True):
                # this part of the code take care of any miss input by the user when entering the choosed pdf number
                try:
                    n = int(input(""))
                except ValueError as e:
                    print(
                        '-'*100, "\nWrong index,try choosing from the listed numbers !\n", '-'*100)
                    # continue here serve a reset going back to the start of the while loop
                    continue
                if n < 0 or n >= len(PDFroots):
                    print(
                        '-'*100, "\nWrong index,out of list bound !\n", '-'*100)
                    continue
                # we open the choosen pdf using the open function with rb as an argument, then the user chosen pdf is assigned
                # to a variable called pdf.
                pdf = open(PDFroots[n], 'rb')
                # pdf.FileReader offers functions that help in reading & viewing the pdf file. It offers various functions using which you can filter
                # the pdf on the basis of the page number, content, page mode, etc.
                pdf_reader = PyPDF2.PdfFileReader(pdf)
                break
            # calling the Decrypt_pdf function to start cracking the password while passing the pdf_reader and text list as arguments
            Decrypt_pdf(pdf_reader, text)
            # grabing the user input for what to do next
            nextmove = input(
                '-'*100 + '\nType Q and press enter to exit ... ')
            # closing the opened pdf
            pdf.close()
        # except catches any problems that prevents us from opening the pdf.

        else:
            # we break out of the programme main while loop  as the interface() function returned False meaning the folder is empty
            break
    else:
        print('-'*100, '\nThank you for using the Brute-force-PDF-Breaker!\n', '-'*100)
