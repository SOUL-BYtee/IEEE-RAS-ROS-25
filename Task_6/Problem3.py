class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Example
calc = Calculator()
print("add:", calc.add(10, 5))
print("subtract:", calc.subtract(10, 5))
print("multiply:", calc.multiply(10, 5))
print("divide:", calc.divide(10, 5))