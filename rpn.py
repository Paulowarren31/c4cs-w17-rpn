#!/usr/bin/env python3
import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
    }
    
def calculate(arg):
  stack = []
  split = arg.split(' ')
  for token in split:
    if token.isdigit(): 
      stack.append(int(token))
    else:
      if token in operators and len(stack) >= 2:
        b = stack.pop()
        a = stack.pop()
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
    print('haha not tested')
    print('haha not tested')
    print('haha not tested')
    print('haha not tested')
    print('haha not tested')
    print('haha not tested')
    print('haha not tested')
    print('haha not tested')
    print('haha not tested')
    print('haha not tested')
    print('haha not tested')
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
