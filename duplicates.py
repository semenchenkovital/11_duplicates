import os
def walk(dir,a):
    for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isfile(path):
        print(path)
        
    else:
        walk(path)
file = open("d:\\d.josm", "w")
walk('d:\\BGS')
if __name__ == '__main__':
    pass
