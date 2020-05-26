import os
import sys

terminal_size = os.get_terminal_size() 

x = None
try:
  if len(sys.argv) < 2:
    x = int(input("Input x: "))
  else:
    x = int(sys.argv[1])
except ValueError:
  print("ERROR: x must be an integer")
  exit(-1)

y = None
try:
  if len(sys.argv) < 3:
    y = int(input("Input y: "))
  else:
    y = int(sys.argv[2])
except ValueError:
  print("ERROR: y must be an integer")
  exit(-1)

if x <= 0 or y <= 0:
  print("Both x and y must be positive, non zero integers")
  exit(-1)
max_length = len(str(x * y))
if (x * max_length) + x > terminal_size.columns:
  print("Output width is larger than your terminal size, line wrapping will occur.")
  input("Press any key to continue...")

header = True
print(f'{0:{max_length}} ', end='')
for row in range(0, y + 1):
  if row == 0:
    row = 1
  for column in range(1, x + 1 ):
    if column == 1 and not header:
      print(f'{row:{max_length}} ', end='')
    print(f'{(row * column):{max_length}} ', end='')
  header = False
  print('')
exit(0)
