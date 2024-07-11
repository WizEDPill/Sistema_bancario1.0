total = 0
counter = 0
while True:
    amount = int(input('Enter the amount to be deposited: '))
    total += amount

    contint = input('Do you want to continue depositing? y-yes n-no: ').strip().lower()
    if contint == 'n':
        sq = input('Do you want to see the statement? y-yes n-no: ').strip().lower()
        if sq == 'n':
            break
        if sq == 'y':
            print(f'Your statement balance is: ------- ${total} -------')
            withdraw_decision = input('Do you want to make a withdrawal? y-yes n-no: ').strip().lower()
            if withdraw_decision == 'n':
                break
            if withdraw_decision == 'y':
                withdrawal_amount = int(input('Enter the amount to withdraw: '))
                print('The limit is 3 withdrawals per day with a maximum of $500 per withdrawal.')
                total_withdrawn = withdrawal_amount
                if withdrawal_amount > total:
                    print(f'Your balance is ${withdrawal_amount - total} less than the amount in your account, so the withdrawal is not possible.')
                elif withdrawal_amount > 500:
                    print('Withdrawal amount exceeds the $500.00 per withdrawal limit.')
                    continue
                elif counter >= 3:
                    print('You have exceeded the daily withdrawal limit.')
                else:
                    print(f'Your withdrawal of ${withdrawal_amount} was successful. Your new balance is ${total - withdrawal_amount}.')
                    counter += 1
                    back_to_menu = input('Do you want to return to the deposit menu or conclude the operation? y-yes n-no: ').strip().lower()
                    if back_to_menu == 'y':
                        continue
                    else:
                        break
                    
print(f'The total amount deposited is ${total}.')
