from common import evaluate_postfix, tokens_to_fraction, infix_to_postfix


e_terms = []
i = 1
while len(e_terms) < 99:
    e_terms.append(1)
    e_terms.append(2 * i)
    e_terms.append(1)
    i += 1

print(e_terms)

def generate_expansion(n):
    stack = []
    expression = "2 + 1 / ("
    stack.append(")")
    
    for i in range(n-1):
        expression += f"{e_terms[i]} + 1 / ("
        stack.append(")")
    
    expression += f"{e_terms[n-1]}"
    expression += "".join(stack)
    return expression

expr = generate_expansion(99)

result = evaluate_postfix(tokens_to_fraction(infix_to_postfix(expr)))
print(result)

print(sum([int(x) for x in str(result.numerator)]))
