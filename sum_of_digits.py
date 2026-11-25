# find the sum of 3 digit number entered by user

x = int(input("Enter a three digit number "))

    a = x % 10
    print(a)

    b = (x // 10) % 10
    print(b)

    c = (x // 100) % 10
    print(c)

print(a+b+c)