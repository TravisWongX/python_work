filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()  # 按空格拆分成单词，存入数组
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

    
