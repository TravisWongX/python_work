import json

def greet_user():
    """问候用户"""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            name = json.load(f_obj)  # 文件对象，不是文件名
    except FileNotFoundError:
        with open(filename, 'w') as f_obj:
            name = input("What's your name?")
            json.dump(name, f_obj)
        print("See you, " + name + "!")
    else:
        print("Welcome back, " + name + "!")


greet_user()
