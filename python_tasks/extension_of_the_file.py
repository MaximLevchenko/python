filename = input("Input the Filename: ")

f_extns = filename.split(".")  # We specify the splitter and make it a '.'. It is a whitespace as default

print(
    "The extension of the file is : " + f_extns[-1])  # Always returns the last object in the list(because of -1)
