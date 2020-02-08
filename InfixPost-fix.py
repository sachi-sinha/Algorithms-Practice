# implementing stacks using lists in Python

class ArrayStack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        return "Stack is empty"

    def top(self):
        if not self.empty():
            return self.stack[len(self.stack) - 1]
        return "Stack is empty"

    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Evaluating Infix to Postfix Expression
class InfixPostfix:

    def __init__(self, infix):
        self.infix = infix
        self.operators = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        self.output = ""
        self.stack = ArrayStack()

    def infixToPostfix(self):
        for i in range(0, len(self.infix)):

            if self.infix[i].isdigit():
                self.output += self.infix[i]

            elif self.infix[i] == '(':
                self.stack.push(self.infix[i])

            elif self.infix[i] == ')':
                while self.stack.top() != '(':
                    self.output += self.stack.pop()
                self.stack.pop()

            elif self.infix[i] == '^' or self.infix[i] == '*' or self.infix[i] == '/' or self.infix[i] == '+' or \
                    self.infix[i] == '-':

                if self.stack.empty() or self.stack.top() == '(':
                    self.stack.push(self.infix[i])

                elif self.operators[self.infix[i]] > self.operators[self.stack.top()]:
                    self.stack.push(self.infix[i])

                else:
                    while not self.stack.empty():
                        self.output += self.stack.pop()

                    self.stack.push(self.infix[i])

            else:
                return "Invalid Expression"

        while not self.stack.empty():
            self.output += self.stack.pop()

        return self.output

# Evaluating the postfix expression to obtain numeric value
class Evaluation:

    def __init__(self, postfix):
        self.postfix = postfix
        self.stack = ArrayStack()

    def convert(self):
        for i in range(0, len(self.postfix)):

            if self.postfix[i].isdigit():
                self.stack.push(int(self.postfix[i]))

            else:
                operand1 = float(self.stack.pop())
                operand2 = float(self.stack.pop())

                if self.postfix[i] == '^':
                    self.stack.push(operand2 ** operand1)

                elif self.postfix[i] == '*':
                    self.stack.push(operand2 * operand1)

                elif self.postfix[i] == '/':
                    self.stack.push(operand2 / operand1)

                elif self.postfix[i] == '+':
                    self.stack.push(operand2 + operand1)

                else:
                    self.stack.push(operand2 - operand1)

        return self.stack.pop()


# Testing the code above
infixString = input("Enter Algebraic Expression: ")

# String length from 3 to 20 characters
while len(infixString) < 3 or len(infixString) > 20:
    infixString = input("Enter Algebraic Expression: ")

infix = InfixPostfix(infixString)
postfix = infix.infixToPostfix()

# String needs to contain valid characters only
while postfix == "Invalid Expression":
    infixString = input("Enter Algebraic Expression: ")
    infix = InfixPostfix(infixString)
    postfix = infix.infixToPostfix()

# Evaluating String for Numeric Value
evaluate = Evaluation(postfix)

print("Infix: " + infixString + "\n" + "Postfix: " + postfix + "\n" + "Evaluation: ", evaluate.convert())
