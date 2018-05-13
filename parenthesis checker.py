"""Given an expression string exp, examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”"""


def balance_check(pairs):
    closing_position = -1
    closed = True
    for i in range(0, len(pairs)):
        if pairs[i] == "{" and pairs.find("}", i) != -1:
            if closed:
                closing_position = pairs.find("}", i)
                closed = False
            elif pairs.find("}", i) >= closing_position:
                return "not balanced"
            else:
                closing_position = pairs.find("}", i)
            if pairs.find("{", i + 1, closing_position) != -1:
                closing_position = pairs.find("}", closing_position + 1)
        elif pairs[i] == "[" and pairs.find("]", i) != -1:
            if closed:
                closing_position = pairs.find("]", i)
                closed = False
            elif pairs.find("]", i) >= closing_position:
                return "not balanced"
            else:
                closing_position = pairs.find("]", i)
            if pairs.find("[", i + 1, closing_position) != -1:
                closing_position = pairs.find("]", closing_position + 1)
        elif pairs[i] == "(" and pairs.find(")", i) != -1:
            if closed:
                closing_position = pairs.find(")", i)
                closed = False
            elif pairs.find(")", i) >= closing_position:
                return "not balanced"
            else:
                closing_position = pairs.find(")", i)
            if pairs.find("(", i + 1, closing_position) != -1:
                closing_position = pairs.find(")", closing_position + 1)
        elif pairs[i] == "}" or "]" or ")":
            if i == 0:
                return "not balanced"
            elif i == closing_position:
                closed = True
            elif i < closing_position:
                return "not balanced"
        else:
            return "not balanced"
    if closed:
        return "balanced"
    else:
        return "not balanced"


t = int(input())
while t > 0:
    n = str(input())
    print(balance_check(n))
    t -= 1
