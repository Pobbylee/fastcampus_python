# gugu class

class guguClass:
    """
    calculate gugudan
    """

    def __init__(self, number):
        self.lastdan = number

    def print_gugu(self):
        for front in range(2, self.lastdan + 1):
            for back in range(1, self.lastdan + 1):
                print front, "*", back, "=", front * back

userinput = int(raw_input("Enter number: "))
mygugu = guguClass(userinput)
indiagugu = guguClass(19)
mygugu.print_gugu()
indiagugu.print_gugu()
