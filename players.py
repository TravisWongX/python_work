players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # 与函数 range() 一样， Python 在到达你指定的第二个索引前面的元素后停止
print(players[1:6])
print(players[1:-2])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())