def sum_check(requisites, account):
    full_summa = 0
    for sender_req in requisites:

        if int(sender_req.get("s_b_a")) == int(account):
            full_summa += float(sender_req.get("t_a"))

    if full_summa == 0:
        print("This bank account does not exist")
    else:
        print(full_summa)
