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
         loggerProcess.stdin.write("CANCEL User cancelled action\n")
         loggerProcess.stdin.flush()
         return
      elif (userInput != "h" and userInput != "n"):
         loggerProcess.stdin.write("ERROR User gave invalid input\n")     
         loggerProcess.stdin.flush()
         print("Invalid Input")
      else:
         break

   while True:
      if userInput == "h":
         loggerProcess.stdin.write("SELECT_HISTORY_PASSWORD User chose to use a word from history to set as password\n")     
         loggerProcess.stdin.flush()
         if len(history) == 0:
            print("There are no words in history to select from")
            while True:
               print("Would you like to enter a new string? Enter (yes or no)")
               print("Input Yes/No: ", end="")
               userInput = input().strip().lower()
               if userInput == "yes":
                  userInput = "n"
                  break
               elif userInput == "no":
                  loggerProcess.stdin.write("PASSWORD_EXIT User exit out of history for entering a password\n")
                  loggerProcess.stdin.flush()
                  return #break out of function
               else:
                  loggerProcess.stdin.write("ERROR User gave invalid input\n")     
                  loggerProcess.stdin.flush()
                  print("Invalid input")
         else:
            displayHistory(history)
            print("Enter the number for the word you would like to set as password (If you would like to enter a new line, enter n): ")
            print("Input Number: ", end="")
            passwordNum = input().strip().lower()
            if passwordNum.isdigit():
               index = int(passwordNum)
               if 1 <= index <= len(history):
                  index = -index
                  word = history[index]
                  
                  loggerProcess.stdin.write(f"SET_HISTORY_PASSWORD User chose to use {word} in history to set as password\n")     
                  loggerProcess.stdin.flush()
                  encryptionProcess.stdin.write(f"PASSKEY {word}\n")
                  encryptionProcess.stdin.flush()
                  
                  #pull output from encryption process and store it
                  output = encryptionProcess.stdout.readline().strip()
                  #requirements state to print the output from driver
                  print(output)

                  #write the output to logger
                  loggerProcess.stdin.write(f"{output}\n")
                  loggerProcess.stdin.flush()
                  return       
                  
               else:
                  loggerProcess.stdin.write("ERROR User chose a number out of range for history\n")     
                  loggerProcess.stdin.flush()
                  print("Number not in range")
                  userInput ="h"

            else:
               if userInput != "n":
                  loggerProcess.stdin.write("ERROR User gave invalid input\n")     
                  loggerProcess.stdin.flush()
                  print("Invalid Input")
                  userInput ="h"
            
      if userInput == "n":
         loggerProcess.stdin.write("SELECT_NEW_PASSWORD User chose to enter a new word to set as password\n")
         loggerProcess.stdin.flush() 
         print("Enter new string that you would like to set as a password")
         print("Input Password: ", end="")
         word = input().strip().upper()

         loggerProcess.stdin.write(f"SET_NEW_PASSWORD User chose to set {word} as password\n")
         loggerProcess.stdin.flush() 
         
         encryptionProcess.stdin.write(f"PASSKEY {word}\n")
         encryptionProcess.stdin.flush()
         
         output = encryptionProcess.stdout.readline().strip()         
         print(output)

         loggerProcess.stdin.write(f"{output}\n")
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
         loggerProcess.stdin.write("CANCEL User cancelled action\n")
         loggerProcess.stdin.flush()
         return
      elif (userInput != "h" and userInput != "n"):
         loggerProcess.stdin.write("ERROR User gave invalid input\n")     
         loggerProcess.stdin.flush()
         print("Invalid Input")
      else:
         break
   
   while True:
      if userInput == "h":
         loggerProcess.stdin.write("SELECT_HISTORY_ENCRYPTION User chose to use a word from history to encrypt\n")     
         loggerProcess.stdin.flush()
         if len(history) == 0:
            print("There are no words in history to select from")
            while True:
               print("Would you like to enter a new string? Enter (yes or no)")
               print("Input Yes/No: ", end="")
               userInput = input().strip().lower()
               if userInput == "yes":
                  userInput = "n"
                  break
               elif userInput == "no":
                  loggerProcess.stdin.write("ENCRYPT_EXIT User exit out of history for entering an encryption\n")
                  loggerProcess.stdin.flush()
                  return
               else:
                  loggerProcess.stdin.write("ERROR User gave invalid input\n")     
                  loggerProcess.stdin.flush()
                  print("Invalid input")
         else:
            displayHistory(history)
            print("Enter a number for the word you would like to encrypt (If you would like to enter a new line, enter n): ")
            print("Input Number: ", end="")
            encryptNum = input().strip().lower()

            if encryptNum.isdigit():
               index = int(encryptNum)
               if 1 <= index <= len(history):
                  index = -index
                  word = history[index]
                  loggerProcess.stdin.write(f"HISTORY_ENCRYPT User chose to encrypt {word} in history\n")
                  loggerProcess.stdin.flush()

                  encryptionProcess.stdin.write(f"ENCRYPT {word}\n")
                  encryptionProcess.stdin.flush()

                  output = encryptionProcess.stdout.readline().strip()
                  print(output)
                  parser = output.split()
                  code = parser[0].upper()

                  if code != "ERROR":
                     history.append(word)
                     history.append(parser[-1]) 

                  loggerProcess.stdin.write(f"{output}\n")
                  loggerProcess.stdin.flush()
                  return
               
               else:
                  loggerProcess.stdin.write("ERROR User chose a number out of range for history\n")     
                  loggerProcess.stdin.flush()
                  print("Number not in range")
                  userInput = "h"
            else:
               if userInput != "n":
                  loggerProcess.stdin.write("ERROR User gave invalid input\n")     
                  loggerProcess.stdin.flush()
                  print("Invalid Input")
               else:
                  userInput = "n"
      if userInput == "n":
         loggerProcess.stdin.write("SELECT_NEW_ENCRYPTION User chose to enter a new word to encrypt\n")
         loggerProcess.stdin.flush() 
         print("Enter new string that you would like to encrypt")
         print("Input Encryption String: ", end="")
         word = input().strip().upper()
        
         
         loggerProcess.stdin.write(f"SEND_NEW_ENCRYPTION User chose to encrypt {word}\n")
         loggerProcess.stdin.flush()

         encryptionProcess.stdin.write(f"ENCRYPT {word}\n")
         encryptionProcess.stdin.flush()
         

         output = encryptionProcess.stdout.readline().strip()
         print(output)
         parser = output.split()
         code = parser[0].upper()

         
         #need logic here to make sure only valid words and results are added to the history
         if code != "ERROR":
            history.append(word)
            history.append(parser[1])

         loggerProcess.stdin.write(f"{output}\n")
         loggerProcess.stdin.flush()
         return


def decrypt(loggerProcess, encryptionProcess, history):
   loggerProcess.stdin.write("DECRYPT_SELECTED User selected decrypt option\n")
   loggerProcess.stdin.flush()
   while True:
      print("Use history (h) or enter new string (n) to decrypt (Enter h or n or cancel) ")
      print("Select: ", end="")
      userInput = input().strip().lower()
      if userInput == "cancel":
         loggerProcess.stdin.write("CANCEL User cancelled decryption\n")
         loggerProcess.stdin.flush()
         return
      elif (userInput != "h" and userInput != "n"):
         loggerProcess.stdin.write("ERROR User gave invalid input\n")     
         loggerProcess.stdin.flush()
         print("Invalid Input")
      else:
         break
   
   while True:
      if userInput == "h":
         loggerProcess.stdin.write("SELECT_HISTORY_DECRYPTION User chose to use a word from history to decrypt\n")     
         loggerProcess.stdin.flush()
         if len(history) == 0:
            print("There are no words in history to select from")
            while True:
               print("Would you like to enter a new string? Enter (yes or no)")
               print("Input Yes/No: ")
               userInput = input().strip().lower()
               if userInput == "yes":
                  userInput = "n"
                  break
               elif userInput == "no":
                  loggerProcess.stdin.write("DECRYPT_EXIT User exit out of history for entering a decryption\n")
                  loggerProcess.stdin.flush()
                  return
               else:
                  loggerProcess.stdin.write("ERROR User gave invalid input\n")     
                  loggerProcess.stdin.flush()
                  print("Invalid input")
         else:
            displayHistory(history)
            print("Enter a number for the word you would like to decrypt (If you would like to enter a new line, enter n): ")
            print("Input Number: ", end="")
            decryptNum = input().strip().lower()

            if decryptNum.isdigit():
               index = int(decryptNum)
               if 1 <= index <= len(history):
                  print(len(history))
                  index = -index
                  word = history[index]
                  loggerProcess.stdin.write(f"HISTORY_DECRYPT User chose to decrypt {word} in history\n")
                  loggerProcess.stdin.flush()

                  encryptionProcess.stdin.write(f"DECRYPT {word}\n")
                  encryptionProcess.stdin.flush()

                  output = encryptionProcess.stdout.readline().strip()
                  print(output)

                  parser = output.split()
                  code = parser[0].upper()
                  
                  
                  if code != "ERROR":
                     history.append(word)
                     history.append(parser[1]) 

                  loggerProcess.stdin.write(f"{output}\n")
                  loggerProcess.stdin.flush()
                  return
               else:
                  loggerProcess.stdin.write("ERROR User chose a number out of range for history\n")     
                  loggerProcess.stdin.flush()
                  print("Number not in range")
                  userInput = "h"
            else:
               if userInput != "n":
                  loggerProcess.stdin.write("ERROR User gave invalid input\n")     
                  loggerProcess.stdin.flush()
                  print("Invalid Input")
               else:
                  userInput = "n"

      if userInput == "n":
         print("Enter new string that you would like to decrypt")
         print("Input String: ", end="")
         word = input().strip().upper()
         
         
         loggerProcess.stdin.write("NEW_DECRYPT User chose to enter new string to decrypt\n")
         loggerProcess.stdin.flush()

         encryptionProcess.stdin.write(f"DECRYPT {word}\n")
         encryptionProcess.stdin.flush()

         output = encryptionProcess.stdout.readline().strip()
         print(output)
         parser = output.split()
         code = parser[0].upper()
         
         #need logic here to make sure only valid words and results are added to the history
         if code != "ERROR":
            history.append(word)
            history.append(parser[-1])

         loggerProcess.stdin.write(f"{output}\n")
         loggerProcess.stdin.flush()
         
         return
      
         



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

      if (userInput == "password" or userInput == "1"): #handle set password
         password(loggerProcess, encryptionProcess, history)
      elif (userInput == "encrypt" or userInput == "2"): #handle encryption
         encrypt(loggerProcess, encryptionProcess, history)

      elif (userInput == "decrypt" or userInput == "3"): #handle decryption
         decrypt(loggerProcess, encryptionProcess, history)

      elif (userInput == "history" or userInput == '4'): #handle history
         displayHistory(history)
         loggerProcess.stdin.write("HISTORY_SELECTED User selected history function\n")
         loggerProcess.stdin.flush()

      elif (userInput == "quit" or userInput == "5"): #handle quit action
         encryptionProcess.stdin.write("QUIT\n")
         encryptionProcess.stdin.flush()
         output = encryptionProcess.stdout.readline().strip()
         print(output)
         loggerProcess.stdin.write("QUIT\n")
         loggerProcess.stdin.flush()
         break
      else:
         loggerProcess.stdin.write("ERROR User gave invalid command\n")     
         loggerProcess.stdin.flush()
         print("Invalid command entered.")


   encryptionProcess.terminate()
   loggerProcess.terminate()
      


    


if __name__ == "__main__":
    main()