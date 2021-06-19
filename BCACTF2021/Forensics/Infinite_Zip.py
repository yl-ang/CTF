from os import system

system('jar xf ./flag.zip')
for i in range(999, -1, -1):
  system('jar xf ./{}.zip'.format(i+1, i))


# Next grep the flag picture using ```grep "bcactf{``` <name of file> after extracting all the 1000 zip files.