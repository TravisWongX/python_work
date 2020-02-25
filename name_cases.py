famous_name = "  alber einstein    "
quotes = "\tLearn from yesterday,live for today, hope for tomorrow." + "\n\tThe important thing is not to stop questioning.\t"
famous_name = famous_name.lstrip()
famous_name = famous_name.rstrip()
quotes = quotes.strip()

message = famous_name.title() + ' said: "\n' + quotes +"\""
print(message)