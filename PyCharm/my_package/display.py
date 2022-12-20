def display_acc(accounts):
    if accounts:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 2,
            '-' * 25,
            '-' * 25,
            '-' * 10
        )
        print(line)
        print(
            '| {:^2} | {:^25} | {:^25} | {:^10} |'.format(
                "№",
                "Sender bank account",
                "beneficiary account",
                "Amount",
            )
        )
        print(line)

        for ind, requisite in enumerate(accounts, 1):
            print(
                '| {:^2} | {:^25} | {:^25} | {:^10} |'.format(
                    ind,
                    requisite.get('s_b_a'),
                    requisite.get('b_a'),
                    requisite.get('t_a'),
                )
            )
            print(line)
    else:
        print("You have no bank accounts for now!")
