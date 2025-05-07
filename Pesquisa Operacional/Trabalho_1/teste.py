import re
import numpy as np

def parse_linear_program(file_path):
    """
    Parse a linear programming problem from a text file and transform it to standard form.
    Uses NumPy for matrix operations.
    """
    # Variables to store our linear program components
    objective_type = None  # "Max" or "Min"
    objective_function = []  # Coefficients of the objective function
    constraint_matrix = []  # Matrix A for constraints
    constraint_types = []  # <=, >=, or =
    constraint_values = []  # Values b for constraints
    variable_names = []  # Names of variables (x1, x2, etc.)
    
    # Read the file
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    # Process the objective function (first line)
    obj_line = lines[0].strip()
    
    # Determine if it's a maximization or minimization problem
    if obj_line.startswith("Max"):
        objective_type = "Max"
    elif obj_line.startswith("Min"):
        objective_type = "Min"
    else:
        raise ValueError("First line must start with 'Max' or 'Min'")
    
    # Extract the objective function
    obj_match = re.search(r'(?:Max|Min)\s+(\w+)\s*=\s*(.*)', obj_line)
    if not obj_match:
        raise ValueError("Invalid objective function format")
    
    obj_var = obj_match.group(1)  # Usually 'z'
    obj_expr = obj_match.group(2).strip()
    
    # Extract variable names and coefficients from the objective function
    obj_terms = re.findall(r'([+-]?\s*\d*\.?\d*)(?:\s*\*\s*|\s+)?(\w+\d*)', obj_expr)
    
    # Collect variable names
    for _, var in obj_terms:
        if var not in variable_names:
            variable_names.append(var)
    
    # Initialize objective function coefficients
    objective_function = np.zeros(len(variable_names))
    
    # Fill objective function coefficients
    for coef, var in obj_terms:
        coef = coef.replace(" ", "")
        if coef == "" or coef == "+":
            coef = 1
        elif coef == "-":
            coef = -1
        else:
            coef = float(coef)
        
        var_index = variable_names.index(var)
        objective_function[var_index] = coef
    
    # Temporary list to build the constraint matrix
    temp_constraint_matrix = []
    
    # Process constraints (remaining lines)
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        
        # Check for constraint type
        constraint_type = None
        if "<=" in line:
            constraint_type = "<="
            parts = line.split("<=")
        elif ">=" in line:
            constraint_type = ">="
            parts = line.split(">=")
        elif "=" in line:
            constraint_type = "="
            parts = line.split("=")
        else:
            raise ValueError(f"Invalid constraint format: {line}")
        
        constraint_types.append(constraint_type)
        
        # Extract the left-hand side (LHS) and right-hand side (RHS)
        lhs = parts[0].strip()
        rhs = float(parts[1].strip())
        constraint_values.append(rhs)
        
        # Extract coefficients for the constraint
        terms = re.findall(r'([+-]?\s*\d*\.?\d*)(?:\s*\*\s*|\s+)?(\w+\d*)', lhs)
        
        # Initialize row for constraint matrix
        constraint_row = np.zeros(len(variable_names))
        
        # Fill constraint row
        for coef, var in terms:
            coef = coef.replace(" ", "")
            if coef == "" or coef == "+":
                coef = 1
            elif coef == "-":
                coef = -1
            else:
                coef = float(coef)
            
            if var not in variable_names:
                variable_names.append(var)
                # Extend existing rows and objective function
                objective_function = np.append(objective_function, 0)
                for i in range(len(temp_constraint_matrix)):
                    temp_constraint_matrix[i] = np.append(temp_constraint_matrix[i], 0)
                constraint_row = np.append(constraint_row, 0)
            
            var_index = variable_names.index(var)
            constraint_row[var_index] = coef
        
        temp_constraint_matrix.append(constraint_row)
    
    # Convert temporary constraint matrix to NumPy array
    constraint_matrix = np.array(temp_constraint_matrix)
    constraint_values = np.array(constraint_values)
    
    # Create standard form with slack variables
    standard_form = add_slack_variables(
        objective_type,
        objective_function,
        constraint_matrix,
        constraint_types,
        constraint_values,
        variable_names
    )
    
    return {
        'original': {
            'objective_type': objective_type,
            'objective_function': objective_function,
            'constraint_matrix': constraint_matrix,
            'constraint_types': constraint_types,
            'constraint_values': constraint_values,
            'variable_names': variable_names
        },
        'standard_form': standard_form
    }

def add_slack_variables(objective_type, objective_function, constraint_matrix, constraint_types, constraint_values, variable_names):
    """
    Add slack, surplus, and artificial variables to transform the LP to standard form.
    """
    # Create copies of the arrays to avoid modifying originals
    new_objective_function = objective_function.copy()
    new_constraint_matrix = constraint_matrix.copy()
    new_constraint_values = constraint_values.copy()
    new_variable_names = variable_names.copy()
    
    slack_count = 1
    surplus_count = 1
    artificial_count = 1
    
    # Number of constraints and variables
    m, n = new_constraint_matrix.shape
    
    # Lists to hold new columns
    slack_columns = []
    identities_needed = 0
    
    # Count how many identity columns we need to add for slack/surplus/artificial variables
    for constraint_type in constraint_types:
        if constraint_type == "<=":
            identities_needed += 1  # One slack variable
        elif constraint_type == ">=":
            identities_needed += 2  # One surplus and one artificial variable
        elif constraint_type == "=":
            identities_needed += 1  # One artificial variable
    
    # Create identity matrix for slack variables
    slack_identity = np.eye(m, dtype=float)
    
    # Initialize the extended matrix with zeros
    extended_A = np.zeros((m, n + identities_needed))
    extended_A[:, :n] = new_constraint_matrix
    
    # Initialize the extended objective function with zeros
    extended_c = np.zeros(n + identities_needed)
    extended_c[:n] = new_objective_function
    
    # Add slack/surplus/artificial variables
    col_index = n
    for i, constraint_type in enumerate(constraint_types):
        if constraint_type == "<=":
            # Add slack variable (s_i) with coefficient 1
            extended_A[i, col_index] = 1
            new_variable_names.append(f"s{slack_count}")
            slack_count += 1
            col_index += 1
        
        elif constraint_type == ">=":
            # Add surplus variable (e_i) with coefficient -1
            extended_A[i, col_index] = -1
            new_variable_names.append(f"e{surplus_count}")
            surplus_count += 1
            col_index += 1
            
            # Add artificial variable (a_i) with coefficient 1
            extended_A[i, col_index] = 1
            # Add large negative/positive coefficient to objective function (Big M)
            big_m_coef = -1000 if objective_type == "Max" else 1000
            extended_c[col_index] = big_m_coef
            new_variable_names.append(f"a{artificial_count}")
            artificial_count += 1
            col_index += 1
        
        elif constraint_type == "=":
            # Add artificial variable (a_i) with coefficient 1
            extended_A[i, col_index] = 1
            # Add large negative/positive coefficient to objective function (Big M)
            big_m_coef = -1000 if objective_type == "Max" else 1000
            extended_c[col_index] = big_m_coef
            new_variable_names.append(f"a{artificial_count}")
            artificial_count += 1
            col_index += 1
    
    # Create new standard form constraint types (all equality)
    new_constraint_types = ["=" for _ in constraint_types]
    
    return {
        'objective_type': objective_type,
        'objective_function': extended_c,
        'constraint_matrix': extended_A,
        'constraint_types': new_constraint_types,
        'constraint_values': new_constraint_values,
        'variable_names': new_variable_names
    }

def print_linear_program(lp, title="Linear Programming Problem"):
    """
    Print a linear programming problem in a human-readable format.
    """
    print(f"\n{title}:")
    print(f"Objective Type: {lp['objective_type']}")
    print(f"Variables: {lp['variable_names']}")
    
    print("\nObjective Function:")
    c = lp['objective_function']
    obj_str = ""
    for i, coef in enumerate(c):
        if coef == 0:
            continue
            
        if i == 0 or not obj_str:
            obj_str += f"{coef} {lp['variable_names'][i]}"
        else:
            obj_str += f" + {coef} {lp['variable_names'][i]}" if coef >= 0 else f" - {abs(coef)} {lp['variable_names'][i]}"
    print(obj_str)
    
    print("\nConstraints:")
    A = lp['constraint_matrix']
    b = lp['constraint_values']
    types = lp['constraint_types']
    
    for i in range(len(A)):
        constr_str = ""
        first_term = True
        
        for j in range(len(A[i])):
            if A[i][j] == 0:
                continue
                
            if first_term:
                constr_str += f"{A[i][j]} {lp['variable_names'][j]}"
                first_term = False
            else:
                constr_str += f" + {A[i][j]} {lp['variable_names'][j]}" if A[i][j] > 0 else f" - {abs(A[i][j])} {lp['variable_names'][j]}"
        
        constr_str += f" {types[i]} {b[i]}"
        print(constr_str)

def print_tableau(lp):
    """
    Print the initial simplex tableau format of the LP problem.
    """
    # Prepare the tableau
    A = lp['constraint_matrix']
    b = lp['constraint_values']
    c = lp['objective_function']
    
    # Create the tableau: [A | b]
    #                     [c | 0]
    m, n = A.shape
    tableau = np.zeros((m+1, n+1))
    tableau[0:m, 0:n] = A
    tableau[0:m, n] = b
    tableau[m, 0:n] = -c  # Negative c for standard form
    
    print("\nInitial Simplex Tableau:")
    print(tableau)
    
    return tableau

# Execute the code
if __name__ == "__main__":
    file_path = "funcao.txt"
    result = parse_linear_program(file_path)
    
    # Print the original problem
    print_linear_program(result['original'], "Original Linear Programming Problem")
    
    # Print the standard form with slack variables
    print_linear_program(result['standard_form'], "Standard Form with Slack Variables")
    
    # Print raw matrix data of standard form
    print("\nStandard Form Matrix Representation:")
    print(f"Objective Function (c): {result['standard_form']['objective_function']}")
    print(f"Constraint Matrix (A):")
    print(result['standard_form']['constraint_matrix'])
    print(f"Constraint Values (b): {result['standard_form']['constraint_values']}")
    print(f"Variable Names: {result['standard_form']['variable_names']}")
    
    # Print the initial simplex tableau
    tableau = print_tableau(result['standard_form'])