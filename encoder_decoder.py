"""
Encoder Decoder program
Eecode messages with a-z charecters into a+shifter new letter
Decode reverse the encoding
"""
greating = """
      ###########################################
      Welcome to the Encoder/Decoder program !
      To start choose operation to performs:
      'encoder' to encrypt or 'decoder' to decrypt
      Then choose the shift amount
      To quit press 'No' or 'Yes' to continue. 
      ############################################
      """

def decoder(message,shifter):
    """Decoding the messages"""
    deco_message = ''
    b = 97 # 'a'
    m = 26 # 'z'
    for letter in message:
        delta = ord(letter[0])-shifter-m*((ord(letter[0])-
                                                shifter-b)//m)
        new_letter = chr(delta)
        deco_message += new_letter
    print(f'The decoded message is: {deco_message}')

def encoder(message,shifter):
    """Enciding the message"""
    enco_message = ''
    b = 97 # 'a'
    m = 26 # 'z'
    for letter in message:
        delta = ord(letter[0])+shifter-m*((ord(letter[0])+
                                                shifter-b)//m)
        new_letter = chr(delta)
        enco_message += new_letter
    print(f'The encoded message is: {enco_message}')
    
print(greating)
not_end = True
continue_game = True

while not_end:
    operation = input("Choose 'encode' to encrypt or 'decode' to decrypt: ")
    if operation.lower() == 'encode':
        message = input("enter messages to be decoded: ")
        shifter = int(input('Enter number of digits to shift: '))
        encoder(message,shifter)
    elif operation.lower() == 'decode':
        message = input("enter messages to be encoded: ")
        shifter = int(input('Enter number of digits to shift: '))
        decoder(message,shifter)
    elif operation.lower() == 'no':
        print('--- Good Bye ---')
        not_end = False
    else:
        print("You entered the wrong option !!!")
        print(greating)