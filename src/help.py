import os

directory = os.fsencode('/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src')
str=[]

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pkl"):
        str.append(filename)
        # print(os.path.join(directory, filename))
        continue
    else:
        continue

file = open('testcases.txt', 'w')
file.write('testcases=[\n')
for testcase in str:
    file.write("'"+testcase+"'"+'\n')

file.write(']')
file.close()