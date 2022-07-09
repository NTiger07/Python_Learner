# Sets are similar to lists except that they don't allow duplicate
# values and the order of the elements are not guaranteed

lettersA = {"A", "B", "C", "D"}
lettersB = {"E", "F", "G", "H", "D"}

union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB

print(f"union = {union}")
print(f"intersection = {intersection}")
print(f"difference = {difference}")
