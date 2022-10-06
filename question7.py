# 7. Write a Python script to count the number of Python keywords occurring in a python source file.
def count(filename,mode):
  kywrd=['False', 'None', 'True', 'and', 'as', 'assert', 
  'async', 'await', 'break', 'class', 'continue', 
  'def', 'del', 'elif', 'else', 'except', 'finally', 
  'for', 'from', 'global', 'if', 'import', 'in', 'is', 
  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
  with open(filename,mode) as f:
    count = 0
    keywordList = []
    for line in f.readlines():
      kwrd = line.split(" ")
      for i in kwrd:
        if i in kywrd and i not in keywordList:
          keywordList.append(i)
          count = count+1
        else:
          pass
  print('The number of keyword are:', len(keywordList))
  print(keywordList)
count('sourcefile.py','r')