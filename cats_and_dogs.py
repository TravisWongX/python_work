def readName(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # pass
        print("File " + filename + " does not exist.")
    else:
        # print(contents.rstrip())
        print(contents.lower().count('the'))  

readName("alice.txt")

