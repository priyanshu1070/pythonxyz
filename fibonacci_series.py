a = int(input("Enter the number you want your fibonacci series upto: "))
b = 0
c = 1
for r in range(1, a + 1):
    acc = b + c
    print(acc)
    b = c
    c = acc
