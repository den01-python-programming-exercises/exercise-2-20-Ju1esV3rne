def main():
    number = 0
    cur = 0
    sum = 0
    even = 0
    odd = 0

    while True:
        number = int(input("Give numbers:"))
        if number == -1:
            break
        elif number % 2 == 0:
            even += 1
        else:
            odd += 1
        sum += number
        cur += 1
        avg = sum/cur

    print("Thx! Bye!")
    print("Sum: " + str(sum))
    print("Numbers: " + str(cur))
    print("Average: " + str(avg))
    print("Even: " + str(even))
    print("Odd: " + str(odd))

if __name__ == '__main__':
    main()
