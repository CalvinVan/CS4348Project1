import sys
import datetime
def getTime():
  return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def writeMessage(action, message, file):
  timeStamp = getTime()
  file.write(f"{timeStamp} [{action}] {message}\n")
  file.flush()

def main():

  if len(sys.argv) != 2: #error handle for if logger file was not passed into the program
    print("Run: python driver.py <logFileName>")
    sys.exit(1) #return error code

  logFile = sys.argv[1]
  
  with open(logFile, 'a') as f: #Open up the log file as append since we could be using a file that was previously written in
    writeMessage("START", "Logging Started.", f) #write start of logging into logger

    while True:
      logMessage = input().strip()  #get the message from standard input 

      #handle Quit Input
      if logMessage.lower() == "quit":
        writeMessage("QUIT", "Program Quitted.", f)
        return #break out of the loop to end the program
      else:
      #handle every other action / input
      #messages are broken into 2 parts [ACTION] [MESSAGE]
        parseArr = logMessage.split(maxsplit=1) #here we can have message be its own entry with any number of spaces / split into 2 parts
        action = parseArr[0]
        if len(parseArr) == 2:
          message = parseArr[1] #maybe there is possible logic to put here if an action does not result in a message
        writeMessage(action, message, f)
    

if __name__ == "__main__":
    main()