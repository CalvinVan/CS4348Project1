import sys
from subprocess import Popen, PIPE

   
def password(loggerProcess, encryptionProcess, history):
   loggerProcess.stdin.write("PASSWORD_SELECTED User selected set password option\n")
   loggerProcess.stdin.flush()
   while True:
      print("Use history (h) or enter new string (n) to set as password (Enter h or n or cancel)")
      print("Select: ", end="")
      userInput = input().strip().lower()
      if userInput == "cancel":
         loggerProcess.stdin.write("CANCEL User cancelled action")
         loggerProcess.stdin.flush()
         return
      elif (userInput != "h" and userInput != "n"):
         print("Invalid Input")
      else:
         break

   while True:
      if userInput == "h":
         if len(history) == 0:
            print("There are no words in history to select from")
            while True:
               print("Would you like to enter a new string? Enter (yes or no)")
               userInput = input().strip().lower()
               if userInput == "yes":
                  userInput = "n"
                  break
               elif userInput == "no":
                  loggerProcess.stdin.write("PASSWORD_EXIT User exit out of entering a password\n")
                  loggerProcess.stdin.flush()
                  return #break out of function
               else:
                  print("Invalid input")
         else:
            displayHistory(history)
            print("Enter the number for the word you would like to set as password (If you would like to enter a new line, enter n): ")
            passwordNum = input().strip().lower()

            if passwordNum.isdigit():
               index = int(passwordNum)
               if 1 <= index <= len(history):
                  index = -index
                  word = history[index]
                  loggerProcess.stdin.write("HISTORY_PASSWORD User chose to use word in history to set as password\n")     
                  loggerProcess.stdin.flush()
                  
                  encryptionProcess.stdin.write(f"PASSKEY {word}\n")
                  encryptionProcess.stdin.flush()
                  
                  #pull output from encryption process and store it
                  output = encryptionProcess.stdout.readline().strip()
                  #requirements state to print the output from driver
                  print(output)

                  #write the output to logger
                  loggerProcess.stdin.write(output)
                  loggerProcess.stdin.flush()
                  return       
                  
               else:
                  loggerProcess.stdin.write("ERROR User chose a number out of range for history\n")     
                  loggerProcess.stdin.flush()
                  print("Number not in range")
                  userInput ="h"

            else:
               if userInput != "n":
                  print("Invalid Input")
                  userInput ="h"
               else:
                  userInput = "n"
            

      if userInput == "n":
         while True:
            print("Enter new string that you would like to set as a password:")
            word = input().strip().lower()
           
            loggerProcess.stdin.write("NEW_PASSWORD User chose to enter a new word to set as password\n")
            loggerProcess.stdin.flush() 

            encryptionProcess.stdin.write(f"PASSKEY {word}\n")
            encryptionProcess.stdin.flush()
            
            
            output = encryptionProcess.stdout.readline().strip()
            
            print(output)


            loggerProcess.stdin.write(output)
            loggerProcess.stdin.flush()
            return
    
            

def displayHistory(history):
  print("\nHISTORY OF WORDS")
  if len(history) > 0:
    n = 1
    for i in range(len(history)-1, -1, -1): #the last element should be the latest one added
       print(f"{[n]}. {history[i]}")
       n += 1
  else:
     print("There are no words stored in history.\n")



def encrypt(loggerProcess, encryptionProcess, history):
   loggerProcess.stdin.write("ENCRYPT_SELECTED User selected encrypt option\n")
   loggerProcess.stdin.flush()
   while True:
      print("Use history (h) or enter new string (n) to encrypt (Enter h or n or cancel)")
      print("Select: ", end="")
      userInput = input().strip().lower()
      if userInput == "cancel":
         loggerProcess.stdin.write("CANCEL User cancelled action")
         loggerProcess.stdin.flush()
         return
      elif (userInput != "h" and userInput != "n"):
         print("Invalid Input")
      else:
         break
   
   while True:
      if userInput == "h":
         if len(history) == 0:
            print("There are no words in history to select from")
            while True:
               print("Would you like to enter a new string? Enter (yes or no)")
               userInput = input().strip().lower()
               if userInput == "yes":
                  userInput = "n"
                  break
               elif userInput == "no":
                  loggerProcess.stdin.write("ENCRYPT_EXIT User exit out of entering an encryption\n")
                  loggerProcess.stdin.flush()
                  return
               else:
                  print("Invalid input")
         else:
            displayHistory(history)
            print("Enter a number for the word you would like to encrypt (If you would like to enter a new line, enter n): ")
            encryptNum = input().strip().lower()

            if encryptNum.isdigit():
               index = int(encryptNum)
               if 1 <= index <= len(history):
                  index *= -index
                  word = history[index]
                  loggerProcess.stdin.write("HISTORY_ENCRYPT User chose to encrypt word in history\n")
                  loggerProcess.stdin.flush()
                  #put encryption functions
                  #store ouptut of encryption process
                  # put logger output write
                  return
               else:
                  print("Number not in range")
                  userInput = "h"
            else:
               if userInput != "n":
                  print("Invalid  Input")
               else:
                  userInput = "n"
      if userInput == "n":
         print("Enter new string that you would like to encrypt:")
         print("Select: ", end="")
         word = input().strip().lower()
        
         history.append(word)
         loggerProcess.stdin.write("NEW_ENCRYPTION User chose to enter new string to encrypt\n")
         loggerProcess.stdin.flush()

         encryptionProcess.stdin.write("ENCRYPT {}")

         #put appropriate functions
         return


def decrypt(loggerProcess, encryptionProcess, history):
   loggerProcess.stdin.write("DECRYPT_SELECTED User selected decrypt option\n")
   loggerProcess.stdin.flush()
   while True:
      print("Use history (h) or enter new string (n) to decrypt (Enter h or n or cancel) ")
      print("Select: ", end="")
      userInput = input().strip().lower()
      if userInput == "cancel":
         loggerProcess.stdin.write("CANCEL User cancelled action")
         loggerProcess.stdin.flush()
         return
      elif (userInput != "h" and userInput != "n"):
         print("Invalid Input")
      else:
         break
   
   while True:
      if userInput == "h":
         if len(history) == 0:
            print("There are no words in history to select from")
            while True:
               print("Would you like to enter a new string? Enter (yes or no)")
               userInput = input().strip().lower()
               if userInput == "yes":
                  userInput = "n"
                  break
               elif userInput == "no":
                  loggerProcess.stdin.write("DECRYPT_EXIT User exit out of entering a decryption\n")
                  loggerProcess.stdin.flush()
                  return
               else:
                  print("Invalid input")
         else:
            displayHistory(history)
            print("Enter a number for the word you would like to decrypt (If you would like to enter a new line, enter n): ")
            decryptNum = input().strip().lower()

            if decryptNum.isdigit():
               index = int(decryptNum)
               if 1 <= index <= len(history):
                  index *= -index
                  word = history[index]
                  loggerProcess.stdin.write("HISTORY_DECRYPT User chose to encrypt word in history\n")
                  loggerProcess.stdin.flush()
                  #put encryption functions
                  #store ouptut of encryption process
                  # put logger output write
                  return
               else:
                  print("Number not in range")
                  userInput = "h"
            else:
               if userInput != "n":
                  print("Invalid  Input")
               else:
                  userInput = "n"
      if userInput == "n":
         print("Enter new string that you would like to encrypt:")
         word = input().strip().lower()
         if word.isalpha():
            history.append(word)
            loggerProcess.stdin.write("NEW_DECRYPT User chose to enter new string to decrypt\n")
            loggerProcess.stdin.flush()
            #put appropriate functions
            return
         else:
            print("Invalid String. Should only contain characters.")
         



def main():
  ##Error handling for log file if it is not put in with the arguments when running python [arguments]
  if len(sys.argv) != 2:
    print("Run: python driver.py <logFileName>")
    sys.exit(1) #return error code
  
  #fetch the log file name to pass into logger process
  logFile = sys.argv[1]

  #initalize a new history for the run using an array 
  history = [] #I think I will treat it as a stack to append the new words 

  #run the process "python logger.py <logFIleName>"
  #Setup a loggerProcess.stdin to send in input from the driver
  #I could possibly explore connect stdin to the output of the encryption process but will not worry about that for now 
  loggerProcess = Popen(['python', 'logger.py', logFile], stdin = PIPE, text = True )

  #run process "python encrypytion.py"
  #Setup stdin and stdout pipes to get info
  encryptionProcess = Popen(['python', 'encryption.py'], stdin = PIPE, stdout = PIPE, text = True)

  ###############  UI SETUP      #############

  while True:
    
    print("\nWELCOME TO ENCRYPTION PROGRAM: TYPE AN ACTION\n")
    print("1. password")
    print("2. encrypt")
    print("3. decrypt")
    print("4. history")
    print("5. quit\n")
    print("Action: ", end="")
    userInput = input().strip().lower() #remove the trailing and leading whitespace with strip
    
    if userInput == "password": #handle set password
       password(loggerProcess, encryptionProcess, history)
    elif userInput == "encrypt": #handle encryption
       encrypt(loggerProcess, encryptionProcess, history)

    elif userInput == "decrypt": #handle decryption
       decrypt(loggerProcess, encryptionProcess, history)

    elif userInput == "history": #handle history
       displayHistory(history)
       loggerProcess.stdin.write("HISTORY_SELECTED User selected history function\n")
       loggerProcess.stdin.flush()

    elif userInput == "quit": #handle quit action
       loggerProcess.stdin.write("QUIT\n")
       loggerProcess.stdin.flush()
       break
    else:
       print("Invalid command entered.")

    
       
  loggerProcess.terminate() #terminate the processes
  encryptionProcess.terminate()
  print("Broke out of loop")

    


if __name__ == "__main__":
    main()