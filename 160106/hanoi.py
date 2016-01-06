def hanoi(start, dropby, dest, number):
    global count

    if number == 1:
        count += 1
        print count, "#", "size", number, " : ", start, "->", dest
        return

    hanoi(start, dest, dropby, number - 1)
    count += 1
    print count, "#", "size", number, " : ", start, "->", dest
    hanoi(dropby, start, dest, number - 1)


n = int(raw_input("Enter the number of rings : "))
count = 0
hanoi("A", "B", "C", n)
