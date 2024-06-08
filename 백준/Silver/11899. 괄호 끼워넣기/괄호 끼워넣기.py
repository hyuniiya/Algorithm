def matching_bracket():
    bracket_input = input()
    stack = []
    add_count = 0
    for bracket in bracket_input:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if len(stack) == 0:
                add_count += 1
            else:
                stack.pop()
    print(add_count + len(stack))

matching_bracket()