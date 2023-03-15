
# schleifen :/
def forachleife(exitChar):
    user_input = input("Eingabe: ")

    for aChar in user_input :
        print(aChar)
        if aChar == exitChar:
            break
    else:
        print("Der letzte macht die Tür zu!")

forachleife("@")