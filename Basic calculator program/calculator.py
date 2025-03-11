def calculator():

  num1 = input('Enter first number : ')
  num2 = input('Enter second number: ')
  add_operator = input('Enter the operator (+): ')

  if add_operator == "+":
    result =  int(num1) + int(num2)
    print('Sum: ',result )
  else:
    print("invalid operator: Please enter '+'.")

calculator()    