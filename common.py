import pyprimesieve


def proper_divisors(n) -> set:
    div = divisors(n)
    div.remove(n)
    return div

def divisors(n):
    factors = pyprimesieve.factorize(n)
    return proper_divisors_rec(factors, 0, 0, 1)

def proper_divisors_rec(factors, i, exponent, divisor):
    divisors = set()
    if i == len(factors):
        divisors.add(divisor)
        return divisors
    
    divisors.update(proper_divisors_rec(factors, i + 1, 0, divisor * factors[i][0] ** exponent))
    if exponent < factors[i][1]:
        divisors.update(proper_divisors_rec(factors, i, exponent + 1, divisor))

    return divisors




from dataclasses import dataclass

@dataclass
class Fraction:
    numerator: int
    denominator: int

    def simplify(self):
        for i in range(2, min(self.numerator, self.denominator)):
            while self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator //= i
                self.denominator //= i

    def __add__(self, other):
        new_fraction = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

        # Check if the fraction can be simplified
        # for i in range(2, min(new_fraction.numerator, new_fraction.denominator)):
        #     while new_fraction.numerator % i == 0 and new_fraction.denominator % i == 0:
        #         new_fraction.numerator //= i
        #         new_fraction.denominator //= i

        return new_fraction
    
    def __sub__(self, other):
        new_fraction = Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

        # Check if the fraction can be simplified
        # for i in range(2, min(new_fraction.numerator, new_fraction.denominator)):
        #     while new_fraction.numerator % i == 0 and new_fraction.denominator % i == 0:
        #         new_fraction.numerator //= i
        #         new_fraction.denominator //= i

        return new_fraction

    def __mul__(self, other):
        new_fraction = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

        # Check if the fraction can be simplified
        # for i in range(2, min(new_fraction.numerator, new_fraction.denominator)):
        #     while new_fraction.numerator % i == 0 and new_fraction.denominator % i == 0:
        #         new_fraction.numerator //= i
        #         new_fraction.denominator //= i
        
        return new_fraction
    
    def __truediv__(self, other):
        new_fraction = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

        # Check if the fraction can be simplified
        # for i in range(2, min(new_fraction.numerator, new_fraction.denominator)):
        #     while new_fraction.numerator % i == 0 and new_fraction.denominator % i == 0:
        #         new_fraction.numerator //= i
        #         new_fraction.denominator //= i

        return new_fraction
    
    def __floordiv__(self, other):
        new_fraction = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        new_fraction.numerator //= new_fraction.denominator
        new_fraction.denominator = 1

        return new_fraction

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        return f"[{self.numerator}/{self.denominator}]"
    
    def __repr__(self):
        return f"[{self.numerator}/{self.denominator}]"

def infix_to_postfix(expression):
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    stack = []
    postfix = []
    for token in numbers_to_tokens(expression):
        if type(token) == int or type(token) == float or type(token) == Fraction:
            postfix.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix

def numbers_to_tokens(expression):
    expression += " " # To make sure the last number is added to the tokens
    tokens = []
    current_number = ""
    for i in range(len(expression)):
        if expression[i] == "-" and current_number == "":
            current_number += expression[i]
        elif expression[i].isalnum() or expression[i] == ".":
            current_number += expression[i]
        else:
            if current_number:
                if "." in current_number:
                    tokens.append(float(current_number))
                else:
                    tokens.append(int(current_number))
            if expression[i] != " ":
                tokens.append(expression[i])
            current_number = ""
    return tokens

def tokens_to_fraction(tokens):
    stack = []
    for token in tokens:
        if type(token) == int or type(token) == float:
            stack.append(Fraction(token, 1))
        else:
            stack.append(token)
    return stack

def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if type(token) == Fraction or type(token) == int or type(token) == float:
            stack.append(token)
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if token == "+":
                stack.append(num2 + num1)
            elif token == "-":
                stack.append(num2 - num1)
            elif token == "*":
                stack.append(num2 * num1)
            elif token == "/":
                stack.append(num2 / num1)
        
    
    return stack[0]



@dataclass
class irrational_square_root:
    whole_part: int
    repeating_part: list

    def generate_expansion(self, n):
        stack = []
        expression = f"{self.whole_part}"
        
        for i in range(n-1):
            expression += f"+ 1 / ( {self.repeating_part[i % len(self.repeating_part)]}"
            stack.append(")")
        expression += "".join(stack)
        return expression

def get_irrational_square_root(n: int) -> irrational_square_root:
    whole_part = int(n ** 0.5)
    repeating_part = []
    

    known = set()
    subtrahend = whole_part
    numerator = 1
    while True:
        known.add((subtrahend, numerator))
        denominator = n - subtrahend ** 2

        denominator = denominator // numerator
        numerator = 1

        a = int((numerator * (whole_part + subtrahend)) / denominator)
        repeating_part.append(a)
        subtrahend = (numerator * (whole_part + subtrahend)) - (a * denominator) - whole_part
        subtrahend = -subtrahend

        numerator = denominator
        if (subtrahend, numerator) in known:
            break

    return irrational_square_root(whole_part, repeating_part)

def gcd(a, b):
    a_factors = pyprimesieve.factorize(a)
    b_factors = pyprimesieve.factorize(b)
    common_factors = set(a_factors.keys()).intersection(b_factors.keys())
    gcd = 1
    for factor in common_factors:
        gcd *= factor ** min(a_factors[factor], b_factors[factor])

def are_coprime(a, b):
    a_factors = pyprimesieve.factorize(a)
    b_factors = pyprimesieve.factorize(b)
    common_factors = set([x[0] for x in a_factors]).intersection([x[0] for x in b_factors])
    return len(common_factors) == 0


def phi(n):
    count = n
    factors = pyprimesieve.factorize(n)
    for factor, _ in factors:
        count *= (1 - 1/factor)
    
    return count