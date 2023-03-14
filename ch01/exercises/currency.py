rate = float(input("What is the exchange rate for the Euro to Dollar?"))
print(rate,type(rate))
amount = float(input("What amount of currency would you like to exchange?"))
print(amount,type(amount)) 
total = float(rate*amount)
result = float(total-3)
print(result)

