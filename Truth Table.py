from sympy import symbols
import re

def evaluate_expression(expression, input_values):
    # Replace the logical operators in the expression with Python's logical operators
    expression = expression.replace('.', ' and ')
    expression = expression.replace('!', ' not ')
    expression = expression.replace('+', ' or ')
    
    # Extract all unique lowercase letters from the expression
    variables = sorted(set(ch for ch in expression if ch.islower()))
    
    # Define the symbols
    symbols_dict = {var: symbols(var) for var in variables}
    
    # Replace the variable names in the expression with their symbolic representations
    expression = re.sub(r'\b(' + '|'.join(variables) + r')\b', lambda match: str(symbols_dict[match.group()]), expression)
    
    # Perform evaluation of the logic expression with the input values
    result = eval(expression, {**globals(), **{symbol: value for symbol, value in zip(variables, input_values)}})
    return result

def draw_truth_table(expression):
    # Analyze the expression to determine the variables
    symbols_list = sorted(list(set([char for char in expression if char.isalpha()])))
    num_variables = len(symbols_list)
    
    # Create all possible combinations of input values for the variables
    input_combinations = []
    for i in range(2**num_variables):
        input_combinations.append(format(i, f'0{num_variables}b'))
    
    # Draw the truth table header
    header = ' | '.join(symbols_list + ['X'])
    print(header)
    print('-' * len(header))
    
    # Evaluate the logic expression for each input combination and draw the truth table
    for combination in input_combinations:
        input_values = [bool(int(combination[i])) for i in range(num_variables)]
        result = evaluate_expression(expression, input_values)
        input_str = ' | '.join([str(int(input_values[i])) for i in range(num_variables)])
        print(input_str + ' | ' + str(int(result)))

# Get user input for the logic expression
while True:
    user_input = input("Enter Logical Expression (or 'exit' to close): ")
    if user_input.lower() == 'exit':
        break
    else:
        print("Truth Table:")
        draw_truth_table(user_input)
