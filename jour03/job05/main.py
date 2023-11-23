def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '%':
        return num1 % num2
    elif operator == '/':
        return num1 / num2
    elif operator == '-':
        return num1 - num2

print(f"3 + 7 = {calcule(3,'+',7)}")
print(f"3 * 7 = {calcule(3,'*',7)}")
print(f"3 % 7 = {calcule(3,'%',7)}")
print(f"3 - 7 = {calcule(3,'-',7)}")
print(f"3 / 7 = {calcule(3,'/',7)}")