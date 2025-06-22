#Cell 02 Execise 03; Multiplication
print("Enter the first number: ")
first_number = input()
print("Enter the second number: ")
second_number = input ()
result = (int(first_number)*int(second_number))
print (first_number, "x", second_number, "=", result)
if result <0:
     print("The number is negative.")
if result >0:
    print("The number is positive.")
if result == 0:
    print("The number is both positive and negative.")