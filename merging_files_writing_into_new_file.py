'''To merge the text files into a single file with the current date-time stamp'''
import datetime
import glob2
c_files = glob2.glob("*.txt")
files_content=[]

for x in c_files:
    with open(x,'r') as file:
        content = file.read()
        files_content.append(content)

filename = datetime.datetime.now()

with open(filename.strftime("%Y-%M-%d-%H-%m")+".txt",'w') as file:
    for x in files_content:
        file.write(x+'\n')

print("Action Performed")
