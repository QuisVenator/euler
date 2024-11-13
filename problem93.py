from itertools import count

# If we use postfix instead of infix notation, we can avoid the need for parentheses and the order of operations is always clear.
# In postfix the first two elements must nescerally be operands. From there on, elements may be either operands or operators.
# We also know that the last element must be an operator.
# Having 4 digits as numbers and 4 operators, we have a total number of possible postfix expressions as 4 * 3 * 4 * 5! = 5760
# Explanation: Of the 4 digits take any as first, of the remaining 3 take any as second, now take any of the 4 operators to put at the end.
# Now we have 5 elements left, 3 digits and 2 operators, these we can combine any which way.

def is_valid_postfix_expression(expression):
    stack = []
    for token in expression:
        if token in digits:
            stack.append(token)
        else:
            if len(stack) < 2:
                return False
            stack.pop()
            stack.pop()
            stack.append(0)
    return len(stack) == 1


def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token in digits:
            stack.append(digit_map[token])
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if num1 == 0 and token == "/":
                return 0
            if token == "+":
                stack.append(num2 + num1)
            elif token == "-":
                stack.append(num2 - num1)
            elif token == "*":
                stack.append(num2 * num1)
            elif token == "/":
                stack.append(num2 / num1)
        
    
    return stack[0]

digit_map = {}
digits = ['a','b','c','d']
operators = ['+','-','*','/']
terms = digits + operators

def generate_postfix_expressions():
    postfix_expressions = []
    expression = []
    for t1 in terms:
        expression.append(t1)
        for t2 in terms:
            if t2 in expression and not t2 in operators:
                continue
            expression.append(t2)
            for t3 in terms:
                if t3 in expression and not t3 in operators:
                    continue
                expression.append(t3)
                for t4 in terms:
                    if t4 in expression and not t4 in operators:
                        continue
                    expression.append(t4)
                    for t5 in terms:
                        if t5 in expression and not t5 in operators:
                            continue
                        expression.append(t5)
                        for t6 in terms:
                            if t6 in expression and not t6 in operators:
                                continue
                            expression.append(t6)
                            for t7 in terms:
                                if t7 in expression and not t7 in operators:
                                    continue
                                expression.append(t7)
                                if is_valid_postfix_expression(expression):
                                    postfix_expressions.append(expression.copy())
                                expression.pop()
                            expression.pop()
                        expression.pop()
                    expression.pop()
                expression.pop()
            expression.pop()
        expression.pop()
        
    return postfix_expressions

expressions = generate_postfix_expressions()

max_length = 28
max_digits = [1,2,3,4]
for d1 in range(1,10):
    digit_map['a'] = d1
    for d2 in range(d1+1, 10):
        digit_map['b'] = d2
        for d3 in range(d2+1, 10):
            digit_map['c'] = d3
            for d4 in range(d3+1, 10):
                digit_map['d'] = d4
                results = set()
                for expression in expressions:
                    results.add(evaluate_postfix(expression))
                for i in count(1):
                    if i not in results:
                        if i-1 > max_length:
                            max_length = i-1
                            max_digits = [d1,d2,d3,d4]
                        break
print(max_digits, max_length)

# Answer: 1258