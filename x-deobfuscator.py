import os
import re


# variables
input_dir: str = "input/"


# functions
def is_java_file(filename: str) -> bool:
    regex = re.compile(
        "(\.java)$",
        re.IGNORECASE # use this instead of (?i) because it's deprecated
    )
    result = re.search(regex, filename)

    if isinstance(result, re.Match):
            print(result.group(0))
            return True
    else:
        return False

def replace_wrong_chars(filename: str):

    print("* [", filename,"] *")

    # Read in the file
    # https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('‍', '')  # U+200D
    filedata = filedata.replace(' ', ' ')  # U+2002
    filedata = filedata.replace(' ', ' ')  # U+2003

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)



# run script
print("*** x-deobfuscate starting... ***")

for filename in os.listdir(input_dir):
    print("file: ", filename)

    if is_java_file(filename):
        filepath = os.path.join(input_dir, filename)
        replace_wrong_chars(filepath)


print("*** x-deobfuscate done ***")
