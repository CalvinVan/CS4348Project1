import sys
from subprocess import Popen, PIPE

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

  