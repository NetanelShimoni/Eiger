def sequencer(biggest, i):
    x = input("Insert number ")
    x = int(x)
    if (x == 0):
        if (biggest == float('-inf')):
            return "(Empty input)"
        return f"({biggest};{i})"
    if (x > biggest):
        return sequencer(x, 1)
    elif (x == biggest):
        return sequencer(x, i=i+1)
    return sequencer(biggest, i)


print(sequencer(float('-inf'), 0))
