import datetime
d = "2022-W35"
r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
print(r)
