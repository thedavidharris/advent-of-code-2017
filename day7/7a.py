with open('day7.txt', 'r') as f:
    roots = []
    dependencies = []
    for line in f:
        line = line.replace(",","").strip().split()
        roots.append(line[0])
        dependencies.extend(line[3:])
    root = list(set(roots) - set(dependencies))
    print(root[0])



