from command_parser import parse_input
from asistant_handler import add_contact, show_all, change_contact, show_phone


def main():
    print('Hello')
    print('How can I help you?')
    contacts = {}
    while (True):

        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        match command:
            case "close":
                print("Good bye!")
                break
            case "exit":
                print("Good bye!")
                break
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(args, contacts))
            case _:
                print("Invalid command!")


if __name__ == "__main__":
    main()
