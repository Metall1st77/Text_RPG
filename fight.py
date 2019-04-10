class fight():
    def __init__(self, file):
        f = open(file, 'r')
        for line in f:
            print(line, end='')

# Fight = fight('demon1.txt')
