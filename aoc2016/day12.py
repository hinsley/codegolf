#!/usr/bin/env python3

import fileinput

registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'sp': 0
}

def evaluate(src):
    try:
        return registers[src]
    except:
        return src

def cmdCpy(src, dest):
    registers[dest] = evaluate(src)

def cmdDec(reg):
    registers[reg] -= 1

def cmdInc(reg):
    registers[reg] += 1

def cmdJnz(condSrc, loc):
    cond = evaluate(condSrc)
    loc = evaluate(loc)
    if cond != 0:
        registers['sp'] += loc - 1

def parseCommand(line):
    cmd = []
    for value in line.strip().split(' '):
        try:
            cmd.append(int(value))
        except:
            cmd.append(value)
    return cmd

instructions = []
for line in fileinput.input():
    instructions.append(parseCommand(line))

while registers['sp'] < len(instructions):
    {
        'cpy': cmdCpy,
        'dec': cmdDec,
        'inc': cmdInc,
        'jnz': cmdJnz
    }[instructions[
          registers['sp']
      ][0]](*instructions[
          registers['sp']]
      [1:])
    registers['sp'] += 1

print(registers['a'])

