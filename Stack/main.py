from Stack.stack import Stack

def isParenBalanced(parenString):
    s= Stack
    index= 0

    while index < len(parenString):
        paren = parenString[index]
        if paren in "[{(":
            s.push(paren)
        