from error_handler import input_error


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact exists!"
    else:
        contacts[name] = phone
        return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact changed."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")


@input_error
def show_all(args, contacts):
    if not contacts:
        return "No contacts available."
    return str(contacts)
