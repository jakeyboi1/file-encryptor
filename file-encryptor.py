# Importing The encryption library used
from cryptography.fernet import Fernet


# Determining Wether the user wants to encrypt Or Decrypt a file
print("To encrypt a file type 'encrypt' and press enter. To decrypt a file type 'decrypt' and press enter.")
type = input()


if type == 'encrypt':
    #### Encryption Area ######

    #Asking For File location
    print('Input the directory of a file you wish to encrypt')
    fileDir = input()

    # Fernet Key Generation
    key = Fernet.generate_key()
    f = Fernet(key)

    #Encrypting the files contents
    filesContent = open(fileDir, 'rb').read()
    encryptedContent = f.encrypt(filesContent)

    # Replacing the file with the encrypted content
    open(fileDir, 'wb').write(encryptedContent)


    # Printing Success and to store key safely
    print('File encrypted Success Here is your key! Store this safely. Press enter to close this program')
    print(key)

    input()
elif type == 'decrypt':


    ##### Decryption Area #####

    # Gets the location of the file to decrypt
    print('Input the directory of the file you wish to decrypt(Note this script can only decrypt files it encrypted!)')
    decryptFileDir = input()

    # Gets the encryption key for this file
    print('Input the encryption key for this file')
    encryptionKey = input()
    e = Fernet(encryptionKey) #Loads key into fernet (this is needed)

    # Decrypts the file
    encryptedFilesContent = open(decryptFileDir, 'rb').read()
    decryptedContent = e.decrypt(encryptedFilesContent)
    open(decryptFileDir, 'wb').write(decryptedContent)

    #Printing success
    print("Your file has been decrypted! Press enter to close this program")
    input()