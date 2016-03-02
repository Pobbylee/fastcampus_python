# my stack class

class myStack:
    """
    stack using list
    """

    def __init__(self, size):
        self.stack_list = []
        self.stack_size = size

    def push(self, element):
        """
        push something into this stack.
        element: something you want to push into stack
        """
        if self.stack_size == len(self.stack_list):
            # overflow check, stack is full
            print "Stack overflow"
            return

        self.stack_list.append(element)
        print element, "pushed"

    def pop(self):
        """
        pop element which is top of this stack
        """
        if len(self.stack_list) == 0:
            # when pop() is called while stack_list is empty -> underflow
            print "Stack underflow"
            return

        self.stack_list.pop()
        print "pop!"
 
    def top(self):
        """
        returning the top element of this stack
        """
        if len(self.stack_list) == 0:
            # when top() is called while stack_list is empty
            print "This stack is empty"
            return

        return self.stack_list[-1]



while True:
    userinput = int(raw_input("Enter the number you want to set stack size : "))
    userstack = myStack(userinput)

    while True:
        userinput = raw_input("\n1: push\n2: pop\n3: top\n4: make another stack\nelse: exit\n\nyour choice: ")
        if userinput == "1":
            userinput = raw_input("Enter string you want to push: ")
            userstack.push(userinput)
        elif userinput == "2":
            userstack.pop()
        elif userinput == "3":
            print "The top element is", userstack.top()
        elif userinput == "4":
            break
        else:
            exit()
