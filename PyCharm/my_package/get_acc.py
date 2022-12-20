def get_bank_acc():
    while True:
        s_b_a = input("Enter the sender's bank account: ")
        if len(s_b_a) != 20 or s_b_a.isdigit() is False:
            print("Incorrect bank account!")
        else:
            break

    while True:
        b_a = input("Enter the beneficiary's account: ")
        if len(b_a) != 20 or b_a.isdigit() is False:
            print("Incorrect bank account!")
        else:
            break

    t_a = input("Enter transfer amount in ₽: ")

    return {
        "s_b_a": s_b_a,
        "b_a": b_a,
        "t_a": t_a,
    }
