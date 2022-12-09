from collections import deque

class Dir:
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        self.file_size = 0
        self.dirs = dict()
        self.files = set()
        self.folder_size = -1
    def add_file(self,name,size):
        if(name not in self.files):
            self.files.add(name)
            self.file_size += size
    def get_dir(self,name):
        if name not in self.dirs:
            self.dirs[name] = Dir(name,self)
        return self.dirs[name]

top_directory = Dir("/",None)
current_dir = top_directory
lines = open("input7.txt").readlines()
for i in range(1,len(lines)):
    line = lines[i].strip()
    if line == "$ ls":
        continue
    elif line[0:4] == "$ cd":
        next_dir = line.split()[2]
        if next_dir == "..":
            current_dir = current_dir.parent
        else:
            current_dir = current_dir.get_dir(next_dir)
    else:
        arg1,arg2 = line.split()
        if arg1 == "dir":
            current_dir.get_dir(arg2)
        else:
            current_dir.add_file(arg2,int(arg1))

def get_folder_size(d):
    if len(d.dirs) == 0:
        d.folder_size = d.file_size
        return d.file_size
    else:
        total_size = d.file_size
        for sub in d.dirs.values():
            total_size += get_folder_size(sub)
        d.folder_size = total_size
        return total_size
get_folder_size(top_directory)

bfs = deque()
bfs.append(top_directory)
part1 = part2 = 0
part2target = 30000000 - (70000000 - top_directory.folder_size)
while len(bfs) > 0:
    current = bfs.popleft()
    if current.folder_size <= 100000:
        part1 += current.folder_size
    if current.folder_size >= part2target and (part2 == 0 or current.folder_size < part2):
        part2 = current.folder_size
    for sub in current.dirs.values():
        bfs.append(sub)
print("Part 1:",part1,"\nPart 2:",part2)