with open('input', 'r') as fp:
    elves = []
    n = 0
    for elf in fp.read().split('\n\n'):
        for calories in elf.split():
            #print(calories)
            try:
                elves[n] += int(calories)
            except IndexError:
                elves.append(int(calories))
        n += 1

print(max(elves))
elves_sorted = sorted(elves, reverse=True)
print(sum(elves_sorted[:3]))