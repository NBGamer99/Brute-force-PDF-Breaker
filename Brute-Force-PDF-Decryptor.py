# password breaker - will break into any encrypted PDF document that has
# a password that is one english word

"""
Using the file-reading skills from the Chapter 8, we can create a list of word strings
by reading the provided file (dictionary). We start by looping over each word in the list, and passing it to the decrypt()
method. If this method returns an integer of 0, the password was wrong and the program
shall continue to the next password. If decrypt() returns 1, then the program shall
break out of the loop and print the hacked password, throughout this process we maked sure
to try both the Uppercase and lowercase forms.
"""

import PyPDF2
import os
import time as t

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "PUT YOUR PDF HERE !!")
PDFroots = []


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


def interface():
    foundPDF = False
    pdf_index = 0
    print('-'*100, '\nThis programme will try to decrypt your encrypted pdf files in the provided folder.\n',
          '-'*100, '\nName', '\t'*10, 'Encrypted\n', '-'*100)

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf") == 1:
                testpdf = open(root+'//'+file, 'rb')
                test_pdf_reader = PyPDF2.PdfFileReader(testpdf)
                foundPDF = True
                print(f'[{pdf_index}] --> '+file+'\r' + '\t' *
                      10 + str(test_pdf_reader.isEncrypted))
                PDFroots.append(root+'//'+file)
                pdf_index += 1
                testpdf.close()

    if foundPDF == False:
        return False
    else:
        print('-'*100, '\nchoose a Pdf to decrypt by providing the index : ...')
        return True


if __name__ == '__main__':
    # Opening the text file and using read and split for each word
    text = open(os.path.join(my_path, "dictionary.txt"))
    text = text.read()
    text = text.split('\n')
    nextmove = ''
    # Open the encrypted document and create a reader and writer
    while(nextmove.lower() != 'q'):
        if interface() == False:
            print(
                '-'*100, "\nno file found under the extension of PDF, try adding some pdf files !\n", '-'*100)
            break
        else:
            try:
                while(True):
                    try:
                        n = int(input(""))
                    except ValueError as e:
                        print(
                            '-'*100, "\nWrong index,try choosing from the listed numbers !\n", '-'*100)
                        continue
                    if n < 0 or n >= len(PDFroots):
                        print(
                            '-'*100, "\nWrong index,out of list bound !\n", '-'*100)
                        continue
                    pdf = open(PDFroots[n], 'rb')
                    pdf_reader = PyPDF2.PdfFileReader(pdf)
                    break
                Decrypt_pdf(pdf_reader, text)
                nextmove = input(
                    '-'*100 + '\nType Q and press enter to exit ... ')
                pdf.close()
            except Exception as exc:
                print(
                    '-'*100, "\nsomething went wrong with the Pdf, Try checking the pdfs in the folder are correct !"+exc+'\n'+'-'*100)
    else:
        print('Thank you')

        # The loop will begin by iterating over each word in the text document
        # I print a message at the beginning so the user knows the program is still running
        # since it can take a while for the program to complete, depending on your word.
        # Once again, try and except. Same as previous programs
        # Inside the try is where we do our magic. As the problem states, if decrypt returns a 1
        # then it's a success. Just set an if statement for the word and word.lower == 1 that
        # # will break out if successful
