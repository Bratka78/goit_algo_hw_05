def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments."
    return inner

@input_error
def add_contact(args, contacts):
        if args[0] in contacts:
            add_answer= input("Such contact name exists, overwrite yes/no?").strip().lower()
            if add_answer == "yes":
                name, phone = args
                contacts[name] = phone
                return "Contact overwritten"
            else:
                return "Contact not recorded"
        name, phone = args
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args,contacts):
        name, phone = args
        contacts[name] = phone
        return "Contact updated."
    
@input_error
def show_phone(args, contacts):
        name = args[0]
        return contacts[name]

@input_error
def show_all(contacts):
    line = []
    for name, phone in sorted(contacts.items()):
        line.append(f"{name}: {phone}")
    return "\n".join(line)