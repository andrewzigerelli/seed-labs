last = 0
#with open('FRAMES', 'r') as f:
#    for line in f:
#        print(int(line,0) - last)
#        last = int(line,0)

with open('2addr', 'r') as f:
        lines = f.readlines()
        lines = [int(y,0) - int(x,0) for (x,y) in zip(lines[1:len(lines):2], lines[::2])]
        print(lines)

