from Stack.stack import Stack

def string_reverse(string):
    reversed_string= Stack()
    for char in string[len(string): 0]:
        reversed_string.push(char)
        print(reversed_string)
    return reversed_string.display()

print(string_reverse("hello"))