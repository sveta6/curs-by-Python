def bracket_check(str):
    stack = list()
    for element in str:
        if element == "(":
            stack.append(element)
        elif element == ")":
            stack.pop()
    print(('NO', 'YES')[len(stack) == 0])

