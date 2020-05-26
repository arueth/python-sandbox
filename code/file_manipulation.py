my_file = open('files/my_file.txt')

print("1:" + my_file.read())
print("2:" + my_file.read())
my_file.seek(0)
print("3:" + my_file.read())

my_file.seek(0)
my_content_raw = my_file.read()
print("raw:" + my_content_raw)

my_file.seek(0)
my_content = my_file.readlines()
print("list:", end ='')
print(my_content)

my_file.close()

# Open file for read
with open('files/my_file.txt', mode='r') as my_new_file:
  content_raw = my_new_file.read()
  print("new_raw:" + content_raw)

# Open file for append
with open('files/my_file.txt', mode='a') as my_new_file:
  my_new_file.write("This is the forth line of the text file")
