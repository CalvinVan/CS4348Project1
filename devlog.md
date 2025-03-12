# Project 1 Devlog Calvin Van CTV210001 CS4348.003

## March 11th 7:00PM
Begin reading project requirements and gaining an idea of the steps and functionalities
needed to accomplish them

### Project Requirement Notes
There are 3 components needed for the project
1. Logger
2. Encryption Program
3. Driver Program

The plan is to use the Subprocess module as I am most familiar with Python recently.

### Logger Impressions
The logger has 1 main function
1. It should be able to write log messages into a log file. As for what it writes, it will use the following format  "YYYY-MM-DD HH:MM" "["ACTION"] MESSAGE
So the logger writes in 3 things: The date and time of the action, the action category, and
the message associated with the action. As for what file it will write in, it will write
in a log file given to it. As for how it will write its messages, it will accept them
through standard input until it receives QUIT

### Encryption Program Impressions
The encryption program should accept commands via standard input. As for how input is 
formatted. It is {command} {arguments for command}. Output will be printed if the command
type is "response type"

Breakdown of command types:
1. PASS / PASSKEY: Set the argument as the current key being used for encryption/decryption
2. ENCRYPT: Encrypt the argument using the key and output the encrypted Argument using the key.
3. DECRYPT: Decrypt the argument using the system's key and output the decrypted argument using the key
4. QUIT: Exit the program

Response types
RESULT {Message after running an action that is valid}
Example of RESULT msgs for functions:
1. PASSKEY: Passkey set to PASSKEY ARG
2. ENCRYPT: Encrypted string
3. Decrypt: Decrypted String
4. Quit: Program Quitted

ERROR {Message explaining error}

Example of errors for functions 
1. PASSKEY: When the argument is not a valid string (contains non-alphabetical characters)
2. ENCRYPT: When there is no passkey set up. 
3. DECRYPT: When there is no passkey set up


### Driver Program Impression
The driver receives ***Input: LOG FILE**. Upon starting the driver program, it should
start two new processes: 1. The logger (which is expecting a log file) 2. The encryption program.

Pipes should be used to essentially connect the user's input into the driver program and logger send them to the encryption program which will then produce output that is then sent back into the driver program which then sends the action into the logger to log the result. Furthermore, it should also log the action taken.

Data flow
Standard Input -> Driver Program (It should store the standard input in a variable probably to then be combined with the encryption output?) -> (Scratch that, it should send into the logger the input that was asked and the time it was sent) -> Encryption Program receives the standard input and then executes the command -> send output message to Driver Program -> send message into logger.

Driver Functionality
1. Start the new processes of executing logger and encryption program (possibly using a pipe)
2. Once the setup is finished, print a menu of commands and prompt the user for commands and quitting out the loop once it sees the the user wants to quit.

Driver Commands:
1. password: provide the user with the option of using a string in the history or entering a new string. If new string is used, prompt for a string to be used for a password which it can then set as the current passkey in the encryption program (PASS FUNCTION). If history is used, then provide user with menu where a number can be used to select a string stored in the history. ***PASSWORD ENTERED IS NOT STORED IN HISTORY ONLY ENCRYPTED AND DECRYPTED RESULTS***
Example:
>User: password
>System: "Use history (h) or enter new string (n) (Enter h or n)"
>User: h
> System: *Call function to show history
> User: 2 (validation needed for this line and the one above)
> System -> Logger: Pass in when the command was sent
> System -> Encryption: Passes in PASSKEY {string} into Encryption
> Encryption -> System: Output 
> System ->Logger: Output

> if User: n
> System: "Enter a string"
> User: "string"
> System->Logger: Passes in action
> System->Encryption: Passes in PASSKEY {string}
> Encryption -> System: Output message
> System -> Logger: Output

2. encrypt: Provide the user with the option of using a string in the history or entering a new string. If new string is used, prompt user for a string, record said string in history, and send encrypt command to encryption program. If history used, select from history screen.
Results are printed to output and also saved in the history

Example:
> User: encrypt
> System: "Use history (h) or enter new string (n) (Enter h or n)"
> User: h
> System: *Call function to show history"
> User: 2 (validation needed for this line and the one above) (have some prompt allowing user to exit out of the history)
> System: Update History
> System -> Logger: Pass in when the command was sent
> System -> Encryption: Passes in Encrypt {string} into Encryption
> Encryption -> System: Output onto system
> System ->Logger: Output message to record in logger
> System: Record output into history

> if User: n
> System: "Enter a string to encrypt"
> User: "string input"
> System: Record string into history
> System -> Logger: Log encrypt command
> System -> Encryption: Pass in Encrypt string
> Encryption -> System: Output onto system
> System -> Logger: Output Message to record in logger
> System: Record output into history

3. Decrypt: Provide user with option of using string in history or entinering a new string. It's the same as Encrypt basically

4. History: Output numbered list of encrypted and decrypted string and string arguments with 1 being the most recent and so on.

>User: history
> System -> Logger: User called history
> System: Display history

5. quit
>User: quit
> System->logger: "quit"
> System->encryption: "quit"
> System: Break out of loop and end program.




