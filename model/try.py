f = open('data3.csv')
words = [ line.rstrip() for line in f.readlines()]
print words