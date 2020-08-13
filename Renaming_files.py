import os

folder = input('Where are the files located? \n> ')
os.chdir(folder)

keyword = input('What do you want to substitute? \n> ')
newword = input('What do you want to replace it with? \n> ')

for file in os.listdir(folder):
    if keyword in file:
        oldname = file
        newname = file.replace(keyword,newword)

        oldpathandname = os.path.join(folder, oldname)
        newpathandname = os.path.join(folder, newname)

        os.rename(oldpathandname, newpathandname)

print('Done')