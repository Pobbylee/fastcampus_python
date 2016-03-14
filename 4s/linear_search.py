def mysearch(ls, inp):
    for n in range(0, len(ls)): # [0, len(ls))
        if ls[n] == inp:
            return n

    return None

mylist = [1, 3, 5, 7, 9]

userinput = int(raw_input("Enter the number you want to find: "))
print mysearch(ls=mylist, inp=userinput)
