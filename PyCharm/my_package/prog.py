from my_package import help
from my_package import check
from my_package import display
from my_package import get_acc
from my_package import invalid


def main():
    """
    Main function
    """
    requisites = []
    while True:

        command = input("Enter Command: ").lower()
        if command == "exit":
            break

        elif command == "add":
            requisite = get_acc.get_bank_acc()
            requisites.append(requisite)

            if len(requisites) > 1:
                requisites.sort(key=lambda item: item.get("s_b_a", ""))

        elif command == "list":
            display.display_acc(requisites)

        elif command.startswith("select "):
            parts = command.split(" ", maxsplit=1)
            bank_acc = parts[1]
            check.sum_check(requisites, bank_acc)

        elif command == 'help':
            help.help_me()

        else:
            invalid.invalid_com()
