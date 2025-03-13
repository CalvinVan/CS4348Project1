import sys

def vigenereEncrypt(text, key):
  return 0

def vigenereDecrypt(text, key):
  return 0

def main():
  currentKey = None

  while True:
    driverInput = input() #pull in stdin from pipe / driver
    #the format of input should be "{action} parameter if any"
    parser = driverInput.split(maxsplit=1)
    action = parser[0].upper()
    parameter = parser[1]

    if action == "QUIT":
      print("QUIT Encryption program stopped")
      break
    elif action == "PASSKEY":
      if not parameter.isalpha():
        print("ERROR Password must contain only letters")
      else:
        currentKey = parameter
        print(f"RESULT Key set successfully to {parameter}")
    elif action == "ENCRYPT":
      if currentKey == None:
        print("ERROR No passkey set")

      elif not parameter.isalpha():
        print("ERROR Input must contain only letters")
      else:
        encrypted = vigenereEncrypt(parameter, currentKey)
        print(f"RESULT {encrypted}")
    
    elif action == "DECRYPT":
        if currentKey == None:
          print("ERROR No passkey set")
        elif not parameter.isalpha():
          print("ERROR Input must contain only letters")
        else:
          decrypted = vigenereDecrypt(parameter, currentKey)
          print(f"RESULT {decrypted}")
    else:
      print(f"ERROR Unknown Action Entered: {action}")

    sys.stdout.flush() #Send out the output after printing to stdout

if __name__ == "__main__":
    main()
