import re
from sympy import symbols, simplify_logic

def simplify_expression(expression):
    # Replace the logical operators in the expression with Python's logical operators
    expression = expression.replace('.', ' & ')
    expression = expression.replace('!', ' ~')
    expression = expression.replace('+', ' | ')

    # Extract all unique lowercase letters from the expression
    variables = sorted(set(ch for ch in expression if ch.islower()))

    # Define the symbols
    symbols_dict = {var: symbols(var) for var in variables}

    # Replace the variable names in the expression with their symbolic representations
    expression = re.sub(r'\b(' + '|'.join(variables) + r')\b', lambda match: f'symbols_dict["{match.group()}"]', expression)

    # Simplify the expression
    simplified = simplify_logic(eval(expression))

    # Replace the Python logical operators with the preferred ones
    simplified_expression = str(simplified)
    simplified_expression = simplified_expression.replace('&', '.')
    simplified_expression = simplified_expression.replace('~', '!')
    simplified_expression = simplified_expression.replace('|', '+')

    return str(simplified_expression)

# Nhập biểu thức từ người dùng

while True:
    user_input = input("Enter Logic Expressions (or 'exit' to close): ")
    if user_input.lower() == 'exit':
        break
    else:
        simplified_expression = simplify_expression(user_input)
        print("Simplified Logic Expressions:", simplified_expression)
