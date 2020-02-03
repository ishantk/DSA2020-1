# Stacks with Lists

stack = []
size = 0

def push(element):
    global size
    if size >= 10:
        print(">> STACK OVERFLOW")
    else:
        size += 1
        stack.append(element)

def pop():
    global size
    size -= 1
    if size < 0:
        print(">> STACK UNDERFLOW")
    else:
        # stack.pop()
        del stack[len(stack)-1]  # remove last element



push(10)
push(20)
push(30)
push(40)
push(50)
push(10)
push(20)
push(30)
push(40)
push(50)
push(10)
push(20)
push(30)
push(40)
push(50)

print(stack)
print("STACK SIZE:", size)
pop()
pop()
pop()
pop()
pop()
pop()
pop()

print(stack)
print("STACK SIZE:", size)

