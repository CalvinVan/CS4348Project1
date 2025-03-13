# CS4348Project1
 
The following project utilizes three programs/scripts. A driver, logger, and encryption program back-end

The main file is the driver.py and to run the program in command line you run "python driver.py <name of log file>" EX: python driver.py logFile.txt

As for the functionality of the driver, it serves as the main file / front-end that starts the subprocesses that will run the logger and encryption files and communicates user input to them via pipes. The main purpose of it is to allow the user to set keys and encrypt and decrypt messages via the vigenere technique.

As for how to use the program, the user is presented with a menu and 5 options: password, encrypt, decrypt, history, and quit. As for how the user can select them, the user can type the action itself or type in a number in respect to the command. EX: 1 for password, 2 for encrypt and so on.

As for the functionalities,

Password: (Should be the first command that is run as you need to set a key to begin encrypting or decrypting) Sets the key that the vigenere algorithm will use to shift letters for any encryptions and decryptions. Key can be new ones or those that are in history.

**NOTE ABOUT HISTORY** Words are sorted from newest to oldest with the newest being at number 1. When it comes to selecting a string from history, user can just type in the number.

Encrypt: User will be presented with the option to encrypt a new string or use from from history. The function will then output the encrypted string on the console and store that encrypted string (alongside the pre-encrypted string) into history

Decrypt: User will be presented with the option to decrypt a string or use from history. The function will output the decrypted string on the console and store both the decrypted string and uncrypted string in history.

History: Displays the history of words done so far in the program's run.

Quit: Quits the encryption process, logger process, and the driver process


Logger:
The logger has a function to calculate the time at which a message is written to record when an action was taken. As for how it does it, it receives input from the driver via pipe / stdin and will break the input into 2 parts (unless the message is quit then it will quit the program): action and message. It will then record the action and message in the format: "{timestamp} [action] message"

Encryption Program:
Serves as the backend for the driver. It holds the functions to handle encryptions, decryptions, and setting up and recording the passkey to determine the shifts for the encryptions and decryptions. Also contains string validation logic to return errors in the instance a user returns a string that is not valid for setting as a password or being en/de-crypted.
