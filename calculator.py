#!/usr/bin/python

import sys, getopt, operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    'x' : operator.mul,
    '/' : operator.div
    "^" : operator.pow
    '%' : operator.mod
}

input_file = open("instructions_file.txt")

running_total = 0

for x in input_file:
  args = x.split()
  first_operand = args[2]
  second_operand = args[3]
  operator = ops.get(args[1])
  running_total = running_total + operator(int(first_operand), int(second_operand))

print running_total