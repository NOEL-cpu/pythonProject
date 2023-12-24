#let's count the number of lines in a given file

import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


base_path = resource_path('folder')

inp_path = Path(os.path.join(base_path, "inputs.json"))

file = open('text.txt', 'r')
line_counter = 0
word_counter = 0

for line in file:
    words = line.split()
    word_counter += len(words)
    line_counter += 1

file.close()
print('The number of line is:'+str(line_counter))
print('The number of line is:'+str(word_counter))
file2 = open('result.txt','w')
file2.write('Agala wet')
file2.close()
a = int(input())
b = int(input())
s = a + b
print(s)
def main():
    a=input("Enter a: ")
