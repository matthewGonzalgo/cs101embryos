import os

if __name__ == '__main__':
    with open('./test.list', 'r') as f:
        lines = f.read().splitlines()
    new_lines = []
    for line in lines:
        embryo_dir = os.path.dirname(line)
        dirs = os.listdir(embryo_dir)
        num = []
        for name in dirs:
            if name[0] == 'c':
                num.append(int(name.split('.')[0].split('t')[0].split('z')[1]))
        num = sorted(num)
        min_index = num[0]
        max_index = num[-1]
        min_z = (min_index + max_index) // 2 - 5
        max_z = min_z + 9
        sp = line.split('/')
        embryo = sp[8]
        z = int(sp[10].split('t')[0][3:])
        if min_z <= z <= max_z:
            continue
        else:
            new_lines.append(line)
    new_lines = [line  + '\n' for line in new_lines]
    with open('./del.list', 'w') as f:
        f.writelines(new_lines)
