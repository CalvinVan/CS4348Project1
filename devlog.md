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
Standard Input -> Driver Program (It should store the standard input in a variable probably to then be combined with the encryption output?) -> Encryption Program receives the standard input and then executes the command -> send output message to Driver Program -> Combine Output message with the standard input in Driver Program -> send message into logger.



