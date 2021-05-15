
filename: str = "./input/Main.java"

print("*** x-deobfuscate starting... ***")

# Read in the file
with open(filename, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('‍', '') # U+200D
filedata = filedata.replace(' ', ' ') # U+2002
filedata = filedata.replace(' ', ' ') # U+2003

# Write the file out again
with open(filename, 'w') as file:
  file.write(filedata)



print("*** x-deobfuscate done ***")
