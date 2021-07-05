'''
This is Stack Implementation,
stack is having these following operations

1) Push
2) Pop
3) Top
4) is_emply

Stack is like an empty box where we are filling values, top value should be popped out first.
Means, FIFO ( FIRST IN FIRST OUT )

Stack are mainly used
1) Presence of Arrays 
2) Depenedent Loops

'''


class Stack:

    # As soon as class stack is called , init Function works and create an empty Stack
    def __init__(self):
        self.stack = []

    # Push operation , we insert element in stack 1 by 1
    def push(self,element):
        self.stack.append(element)

    # we remove element from stack
    def pop(self):
        self.stack.pop()

    # we don't pop the top element , just view it 
    def top(self):
        if self.is_empty:
            return ' STACK IS EMPTY '
        else:
            return self.stack[-1]

    # is stack empty
    def is_empty(self):
        return False if self.stack else True

    # shows the created stack
    def show_stack(self):
        print(self.stack)


s =  Stack()
list_of_elements = [1,2,3,4,5]


for each_element in list_of_elements:
    s.push(each_element)

# show me the stack
s.show_stack()

# show the top element
s.top()

# pop out the top elment
s.pop()

# show me stack again
s.show_stack()

# is stack emplty
print(s.is_empty())