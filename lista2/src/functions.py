def countMembers(czlonkowie):
    if czlonkowie:
        return len(czlonkowie)
    else:
        return 0

def printMembers(czlonkowie):
    i = 1
    print("Członkowie zespołu:")
    for member in czlonkowie:
        print(f"{i}. {member}")
        i += 1


def formatGreeting(nazwa_zespolu):
    return f"Witamy w zespole {nazwa_zespolu}"
