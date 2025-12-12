import os
from cryptography.fernet import Fernet as crypt
allowed_usr = "FOR1059410"


def Mainmenu():
    print("---MAIN-MENU---\n\n\nChoose one of the following Options:\n\t1 - decrypt\n\t2 - encrypt\n\t6 - create new key")
    ans = input("Enter a number to proceed\n>>>")

    if ans == "1":
        DECRYPT()
    elif ans == "2":
        ENCRYPT()
    elif ans == "6":
        new_key(True)
        print("[INFO]New keyfile created.")
    else:
        print("[ERROR]Invalid Input")
        Mainmenu()


def ENCRYPT():
    print("---ENCRYPT---\n[INFO]looking for key in current directory...")
    global Key

    if "keyfile.key" in Current_Directory:
        ans = input("Choose one of the following options:\n\t1 - create a new keyfile\n\t2 - create a key and display it\n\t3 - use the keyfile in the current directory\nEnter a number to proceed\n>>>")
    else:
        ans = input("Choose one of the following options:\n\t1 - create a new keyfile\n\t2 - create a key and display it\nEnter a number to proceed\n>>>")

    if ans == "1":
        print("[INFO]Creating new keyfile...")
        new_key(True)

    elif ans == "2":
        new_key(False)
        print("[INFO]The key that will be used for this encryption is:" + Key.decode())

    elif ans == "3":
        with open("keyfile.key", "rb") as keyfile:
            Key = keyfile.read()

    print("[INFO]Encrypting files...")
    for targetfile in Locker_directory_files:
        print("[INFO]Encrypting: " + targetfile)
        try:
            with open(targetfile, "rb") as current_targetfile:
                targetcontent = current_targetfile.read()

            targetcontent_encrypted = crypt(Key).encrypt(targetcontent)

            with open(targetfile, "wb") as current_targetfile:
                current_targetfile.write(targetcontent_encrypted)

        except PermissionError:
            print("[WARNING] No permission to encrypt: " + targetfile)
        except:
            print("[WARNING] Failed to encrypt: " + targetfile)

    print("[INFO]Done!")
    Mainmenu()


def DECRYPT():
    global Key
    print("---DECRYPT---")
    ans = input("Choose one of the following options:\n\t1 - enter the key\n\t2 - enter the path to the keyfile\n\t3 - use the keyfile in the current directory\nEnter a number to proceed\n>>>")

    if ans == "1":
        Key = input("Please enter the Key.\n>>>").encode()

    elif ans == "2":
        Keydir = input("Please enter the path to the key file.\n>>>")
        with open(Keydir, "rb") as keyfile:
            Key = keyfile.read()

    elif ans == "3":
        with open("keyfile.key", "rb") as keyfile:
            Key = keyfile.read()

    print("[INFO]Decrypting files...")
    for targetfile in Locker_directory_files:
        print("[INFO]Decrypting: " + targetfile)

        try:
            with open(targetfile, "rb") as current_targetfile:
                targetcontent = current_targetfile.read()

            targetcontent_decrypted = crypt(Key).decrypt(targetcontent)

            with open(targetfile, "wb") as current_targetfile:
                current_targetfile.write(targetcontent_decrypted)

        except PermissionError:
            print("[WARNING] No permission to decrypt: " + targetfile)
        except:
            print("[WARNING] Failed to decrypt: " + targetfile)

    print("[INFO]Done!")
    Mainmenu()


def new_key(save_as_keyfile):
    global Key
    Key = crypt.generate_key()

    if save_as_keyfile:
        with open("keyfile.key", "wb") as keyfile:
            keyfile.write(Key)


print("---WELCOME TO FORLOCKER---\n\n[INFO]Initializing...")
Current_Directory = []
Locker_Directory = []
Locker_directory_files = []
usr = None
Key = None

print("[INFO]Listing current directory...")
Current_Directory = os.listdir()

print("[INFO]Checking for Locker directory...")
if not "Locker" in Current_Directory:
    print("[INFO]Locker directory not found.\n[INFO]Creating Locker directory...")
    os.system('mkdir Locker')
else:
    print("[INFO]Locker directory found.")

print("[INFO]Listing Locker directory...")
for root, dirs, files in os.walk("./Locker"):
    for file in files:
        Locker_directory_files.append(os.path.join(root, file))

print("[INFO] files found:" + str(len(Locker_directory_files)))
usr = os.getlogin()
print("[INFO]identified: " + usr)

if not usr == allowed_usr:
    print("[ERROR]" + usr + " doesn't have the Admittions to run this Program")
    quit()
else:
    print("welcome")
    Mainmenu()
