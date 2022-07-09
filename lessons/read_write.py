import os.path

# w: Writing
# r: Reading
# r+: Reading and writing
# a: Append

filename = 'data.csv'

if os.path.isfile(filename):
    with open(filename,"r") as file:
        print(file.read())       
else:
    print(f"file {filename} does not exist")
    
    
# file = open("./data.csv", "r")
# file.write("Name age car\n")
# file.write("Favour 16 Audi\n")
# file.write("Beckham 50 SUV\n")
# print(file.read())
# for line in file:
#     print(line)

