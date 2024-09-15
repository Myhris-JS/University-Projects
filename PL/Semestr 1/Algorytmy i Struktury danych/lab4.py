#Zadanie 1
def isvalid(expression):
    stack = []
    opening_brackets = ['(', '[']
    closing_brackets = [')', ']']
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets[closing_brackets.index(char)] != stack.pop():
                return False

    return not stack

print(isvalid('(())'))  
print(isvalid('([])'))  
print(isvalid('((2 + 5) * (2 + 3)) / 2'))  
print(isvalid('a = [(3, 5), (2, 5), (2, 9)]'))
print(isvalid('(]()[]')) 
print(isvalid('[[((]]))')) 

#Zadanie 2
from collections import deque

def mail(line):
    queue = deque(line)
    outgoing = []

    while queue:
        person = queue.popleft()
        name, needs_second_visit = person

        if needs_second_visit:
            queue.append(person)
        else:
            outgoing.append(name)

    return outgoing

line = [
    ('Grażyna', True),
    ('Laura', False),
    ('Bartek', False),
    ('Andrzej', True),
    ('Wiesiek', False)
]
print(mail(line)) 

#Zadanie 3
def sort_stack(stack):
    aux_stack = []
    while stack:
        temp = stack.pop()
        while aux_stack and aux_stack[-1] > temp:
            stack.append(aux_stack.pop())
        aux_stack.append(temp)
    return aux_stack

stack_to_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_stack = sort_stack(stack_to_sort)
print(sorted_stack)
