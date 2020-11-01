def arithmetic_arranger(problems, showResults=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = ''
    second_line = ''
    equal_line = ''
    result_line = ''
    problem_separator = 4 * ' '

    for problem in problems:
        problem_parts = problem.split()
        operator = problem_parts[1]

        if operator == '*' or operator == '/':
            return 'Error: Operator must be \'+\' or \'-\'.'

        first_operand = problem_parts[0]        
        second_operand = problem_parts[2]

        if not first_operand.isdigit() or not second_operand.isdigit():
           return 'Error: Numbers must only contain digits.'

        first_operand_len = len(first_operand)
        second_operand_len = len(second_operand)

        if first_operand_len > 4 or second_operand_len > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        if first_line != '':
          first_line += problem_separator
          second_line += problem_separator
          equal_line += problem_separator
          if showResults:              
              result_line += problem_separator
        equal_sign = (max(first_operand_len, second_operand_len) + 2) * '-'
        equal_line += equal_sign

        if showResults:  
          first_op_nbr = int(first_operand)
          second_op_nbr = int(second_operand)
          result = str(first_op_nbr + second_op_nbr if operator == '+' else first_op_nbr - second_op_nbr)
          result_line += (len(equal_sign) - len(result)) * ' '  + result

        first_line += (len(equal_sign) - first_operand_len) * ' ' + first_operand
        second_line += operator + (len(equal_sign) - second_operand_len - 1) * ' ' + second_operand
    arranged_problems = first_line + '\n' + second_line + '\n' + equal_line

    if showResults:
       arranged_problems += '\n' + result_line

    return arranged_problems