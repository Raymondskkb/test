int_rate = 0.2

amount = int(input('Input amount: '))
print('Amount is ', amount)
final_pay = ((amount * int_rate) + amount)
print('After 1 month you will pay ', final_pay) 
monthly_pay = int(input('Enter your monthly payment: '))
if monthly_pay != final_pay:
    balance = (final_pay - monthly_pay)
    new_balance = ((balance * 0.2) + balance)
    print('New balance by EOM is ', new_balance)
else:
    print('Your Loan is complete')