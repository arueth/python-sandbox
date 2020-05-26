from sys import argv

try:
  if len(argv) < 2:
    last_num = int(input("Last number: "))
  else:
    last_num = int(argv[1])
except ValueError:
  print("ERROR: Last number must be an integer")
  exit(-1)

for num in range(1, last_num + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
