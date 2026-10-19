import os
from random import randint

password = []

def gen_password(length): #Function for generating passwords
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-=_+`~/.,?><\"';'"
    try:
        for _ in range(length):
            cur_char = randint(0, len(chars)-1)
            password.append(chars[cur_char])
        return "".join(password)
    except ValueError:
        print("Try using an integer for length")


while True: # Starts main loop

    userinput = input(">> ")

    if userinput.lower() == "gennew": # Generating a new password
        length_input = input("Enter length>> ")
        name = input("Enter name for password>> ")
        yn = input(f"Save password to {name}.txt? y/n >>")

        # ^^ Asks info about password about to generate ^^

        if yn.lower() == "y" or yn.lower() == "yes":

            try:
                print("Attempting to save file")
                with open(f"passwords/{name}.txt", "w") as p:
                    p.write(f"{name}: {gen_password(int(length_input))}")

                # Attempting to, well, save file via Open()

                if os.path.exists(f"passwords/{name}.txt") == True: # Check if the file just made exists, just in case
                    print("File made succesfully.")
                else:
                    print("File not created.")

            # VV Exceptions VV
            except ValueError:
                print("Please type a valid integer for the length. E.G, 6, 9, 7. NOT floats such as 5.5, 7.8, or 6.7")
                os.remove(f"passwords/{name}.txt")

            except PermissionError:
                print("Not enough permissions to make file.")
                os.remove(f"passwords/{name}.txt")

            except FileExistsError:
                print("File with that name already exists.")
                os.remove(f"passwords/{name}.txt")

        elif yn.lower() == "n" or yn.lower == "no": # If user says no, does nothing
            print("File not saved")

    ## VV If the user wants to delete a file
    elif userinput.lower() == "delpass":

        file = input("Which file would you like to delete? Make sure to add a .txt to the end >> ")

        try: # Tries to remove file, with basic exceptions
            os.remove(f"passwords/{file}.txt")
        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("You don't have enough permissions to delete this file.")


    elif userinput.lower() == "manpass":
        man_password = input("Enter password >> ")
        man_name = input("Enter password name >> ")

        try:
            with open(f"passwords/{man_name}.txt", "w") as mp:
                mp.write(f"{man_name}: {man_password}")
            if os.path.exists(f"passwords/{man_name}.txt"):
                print("File created")
            else:
                print("File not created")
        except FileExistsError:
            print("File with that name already exists")

        except PermissionError:
            print("Not enough permissions")

    # ^^^ Same as gennew, but with different values.

            if os.path.exists(f"password/{man_name}.txt"):
                print("File created.")
            else:
                print("File not created.")

    elif userinput.lower() == "viewpass":
        print(os.listdir("passwords")) # Self explanatory

    elif userinput.lower() == "exit":
        break # Self explanatory v2

    elif userinput.lower() == "help": # Self explanatory v, uh, 4? I lost count.
        print("COMMANDS: gennew: Follow the prompts to make a new password -- delpass: Deletes a password. Follow the prompts to do so -- viewpass: Views all the files in the directory \"password/\" directory -- [ExamplePasswordFile.txt] Views that file (Case-sensetive) -- manpass: Manually adds a password if the user doesn't wanna generate one randomly -- exit: Exits")

    else: # If a user inputs something else, checks if its a password file name before returning an error.
        if os.path.exists(f"passwords/{userinput}"):
            with open(f"passwords/{userinput}", "r") as p:
                print(p.readline())
        else:
            print("Unkown command or password file. Try 'help'.")
