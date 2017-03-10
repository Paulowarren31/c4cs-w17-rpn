#!/usr/bin/env python3


def add(a,b):
  return a + b

def sub(a, b):
  return b - a

def mult(a, b):
  return a * b

def div(a, b):
  return b / a

operators = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div
    }
    
def calculate(arg):
  stack = []
  split = arg.split(' ')
  for token in split:
    if token.isdigit(): 
      stack.append(int(token))
    else:
      if token in operators and len(stack) >= 2:
        a = stack.pop()
        b = stack.pop()
        stack.append(operators[token](a, b))
      else:
        print('Error: Malformed expression')
        return 

  if len(stack) != 1:
    print('Error: Malformed expression')
    return
  else:
    print(float(stack[len(stack) - 1]))
    return stack.pop()


def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
