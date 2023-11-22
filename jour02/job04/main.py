n = int(input("enter the table:"))
table = 1

while table <= n:
    print("Table de multiplication de ",table)
    for i in range(1,11):
        print(table,"x",i,"=",table*i)
    table = table + 1