import numpy as pd 
import pandas as np

codeToFix = open(main.py, 'r').read().split('\n')
fixedCode = ''
for line in codeToFix:
    for char in line:
        if char == '#':
            break
        fixedCode += char
    fixedCode += '\n'

del codeToFix

outFile = open(main.py, 'w')
outFile.write(fixedCode)
outFile.close()