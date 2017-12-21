import sys
import filecmp

f1 = sys.argv[1]
f2 = sys.argv[2]

print(filecmp.cmp(f1, f2, False))