# --- REFACTOR WITH A LOOP---

change = int(input())

values = {'dollar': 100, 'quarter': 25, 'dime': 10, 'nickel': 5, 'penny': 1}
count = {'dollar': 0, 'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}

if change <= 0:
    print('No change')

if change // values['dollar'] != 0:
    num_dollars = change // values['dollar']  # Number of whole dollars in change
    count['dollar'] = num_dollars  # Assign number of dollars to dictionary
    change -= (num_dollars * values['dollar'])  # Subtract dollar amount in cents from change

    if change // values['quarter'] != 0:
        num_quarters = change // values['quarter']  # Number of whole quarters in change
        count['quarter'] = num_quarters  # Assign number of quarters to dictionary
        change -= (num_quarters * values['quarter'])  # Subtract quarter amount in cents from change

        if change // values['dime'] != 0:
            num_dimes = change // values['dime']  # Number of whole dimes in change
            count['dime'] = num_dimes  # Assign number of dimes to dictionary
            change -= (num_dimes * values['dime'])  # Subtract dime amount in cents from change

            if change // values['nickel'] != 0:
                num_nickels = change // values['nickel']  # Number of whole dimes in change
                count['nickel'] = num_nickels  # Assign number of dimes to dictionary
                change -= (num_nickels * values['nickel'])  # Subtract dime amount in cents from change

                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
            else:
                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
        else:
            if change // values['nickel'] != 0:
                num_nickels = change // values['nickel']  # Number of whole dimes in change
                count['nickel'] = num_nickels  # Assign number of dimes to dictionary
                change -= (num_nickels * values['nickel'])  # Subtract dime amount in cents from change

                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
            else:
                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change

    else:
        if change // values['dime'] != 0:
            num_dimes = change // values['dime']  # Number of whole dimes in change
            count['dime'] = num_dimes  # Assign number of dimes to dictionary
            change -= (num_dimes * values['dime'])  # Subtract dime amount in cents from change

            if change // values['nickel'] != 0:
                num_nickels = change // values['nickel']  # Number of whole dimes in change
                count['nickel'] = num_nickels  # Assign number of dimes to dictionary
                change -= (num_nickels * values['nickel'])  # Subtract dime amount in cents from change

                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
            else:
                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
        else:
            if change // values['nickel'] != 0:
                num_nickels = change // values['nickel']  # Number of whole dimes in change
                count['nickel'] = num_nickels  # Assign number of dimes to dictionary
                change -= (num_nickels * values['nickel'])  # Subtract dime amount in cents from change

                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
            else:
                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change

else:
    if change // values['quarter'] != 0:
        num_quarters = change // values['quarter']  # Number of whole quarters in change
        count['quarter'] = num_quarters  # Assign number of quarters to dictionary
        change -= (num_quarters * values['quarter'])  # Subtract quarter amount in cents from change

        if change // values['dime'] != 0:
            num_dimes = change // values['dime']  # Number of whole dimes in change
            count['dime'] = num_dimes  # Assign number of dimes to dictionary
            change -= (num_dimes * values['dime'])  # Subtract dime amount in cents from change

            if change // values['nickel'] != 0:
                num_nickels = change // values['nickel']  # Number of whole dimes in change
                count['nickel'] = num_nickels  # Assign number of dimes to dictionary
                change -= (num_nickels * values['nickel'])  # Subtract dime amount in cents from change

                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
            else:
                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
        else:
            if change // values['nickel'] != 0:
                num_nickels = change // values['nickel']  # Number of whole dimes in change
                count['nickel'] = num_nickels  # Assign number of dimes to dictionary
                change -= (num_nickels * values['nickel'])  # Subtract dime amount in cents from change

                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
            else:
                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change

    else:
        if change // values['dime'] != 0:
            num_dimes = change // values['dime']  # Number of whole dimes in change
            count['dime'] = num_dimes  # Assign number of dimes to dictionary
            change -= (num_dimes * values['dime'])  # Subtract dime amount in cents from change

            if change // values['nickel'] != 0:
                num_nickels = change // values['nickel']  # Number of whole dimes in change
                count['nickel'] = num_nickels  # Assign number of dimes to dictionary
                change -= (num_nickels * values['nickel'])  # Subtract dime amount in cents from change

                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
            else:
                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
        else:
            if change // values['nickel'] != 0:
                num_nickels = change // values['nickel']  # Number of whole dimes in change
                count['nickel'] = num_nickels  # Assign number of dimes to dictionary
                change -= (num_nickels * values['nickel'])  # Subtract dime amount in cents from change

                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change
            else:
                if change // values['penny'] != 0:
                    num_pennies = change // values['penny']  # Number of whole pennies in change
                    count['penny'] = num_pennies  # Assign number of pennies to dictionary
                    change -= (num_pennies * values['penny'])  # Subtract penny amount in cents from change

dollars = f'{count["dollar"]} Dollars' if count["dollar"] > 1 else f'{count["dollar"]} Dollar'
quarters = f'{count["quarter"]} Quarters' if count["quarter"] > 1 else f'{count["quarter"]} Quarter'
dimes = f'{count["dime"]} Dimes' if count["dime"] > 1 else f'{count["dime"]} Dime'
nickels = f'{count["nickel"]} Nickels' if count["nickel"] > 1 else f'{count["nickel"]} Nickel'
pennies = f'{count["penny"]} Pennies' if count["penny"] > 1 else f'{count["penny"]} Penny'

if count["dollar"] > 0:
    print(f'{dollars}')

if count["quarter"] > 0:
    print(f'{quarters}')

if count["dime"] > 0:
    print(f'{dimes}')

if count["nickel"] > 0:
    print(f'{nickels}')

if count["penny"] > 0:
    print(f'{pennies}')