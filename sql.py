import pymssql

conn = pymssql.connect(host='127.0.0.1',
                       user='sa',
                       password='ynsa@0805',
                       database='GAGDBP06',
                       charset='utf8')

cursor = conn.cursor()
sql = 'select * from branchDistributionGD'
cursor.execute(sql)

rs = cursor.fetchall()

print(rs)