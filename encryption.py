import sys

def vigenereEncrypt(text, key): #taken from https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4 to implement the vigenere algorithms
  keyLen = len(key)
  keyInt = [ord(i) for i in key] #we store the ascii values for each character of the key and text 
  textInt = [ord(i) for i in text]

  encryptedRes = ''
  for i in range(len(textInt)):
    value = (textInt[i] + keyInt[i%keyLen]) % 26
    encryptedRes += chr(value + 65) #calculate the shifts using the key and 65 is because the ascii for 'a' is 65
  return encryptedRes

def vigenereDecrypt(text, key):
  keyLen = len(key)
  keyInt = [ord(i) for i in key]
  textInt = [ord(i) for i in text]

  decryptedRes = ''
  for i in range(len(textInt)):
    value = (textInt[i] - keyInt[i % keyLen]) % 26
    decryptedRes += chr(value + 65)
  return decryptedRes

def main():
  currentKey = None

  while True:
    driverInput = input() #pull in stdin from pipe / driver
    #the format of input should be "{action} parameter if any"
    parser = driverInput.split(maxsplit=1)
    action = parser[0].upper()
    if action == "QUIT":
      print("QUIT Encryption program stopped")
      break
    
    if len(parser) < 2:
      print("ERROR INVALID COMMAND FORMAT") #putting this here in case some other command without a action and message pops up somehow...
      sys.stdout.flush()
      continue

    parameter = parser[1] 
    if action == "PASSKEY":
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
