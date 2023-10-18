import os

def clear_screen():
    # Check the OS and use the appropriate clear screen command
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def main():
    while True:
        clear_screen()
        print("Recommendations menu: ")
        print("1. Literature")
        print("2. Cinema")
        print("3. Music")
        print("4. Video games")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            clear_screen()
            print("Recommended readings:")
            print("+ Waiting for Tito and other football stories (Eduardo Sacheri)")
            print("+ Ender's Game (Orson Scott Card)")
            print("+ The dream of heroes (Adolfo Bioy Casares)")
            input("Press Enter to continue...")
        elif choice == '2':
            clear_screen()
            print("Recommended movies:")
            print("+ Matrix (1999)")
            print("+ The last samurai (2003)")
            print("+ Cars (2006)")
            input("Press Enter to continue...")
        elif choice == '3':
            clear_screen()
            print("Recommended discs:")
            print("+ Torn to pieces (La Renga, 1996)")
            print("+ Buffalo (The Mississippi, 2008)")
            print("+ Gaia (Wizard of Oz, 2003)")
            input("Press Enter to continue...")
        elif choice == '4':
            clear_screen()
            print("Recommended classic video games:")
            print("+ Day of the Tentacle (LucasArts, 1993)")
            print("+ Terminal Velocity (Terminal Reality/3D Realms, 1995)")
            print("+ Death Rally (Remedy/Apogee, 1996)")
            input("Press Enter to continue...")
        elif choice == '5':
            clear_screen()
            print("Goodbye!")
            break
        else:
            clear_screen()
            print("Option does not validate.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
