import random
statsNumbs = {i: 0 for i in range(1, 44)}


def lotto(obereGrenze, durchFuehrungen):
    pulledNumbs = []

    allNumbs = [i for i in range(1, obereGrenze)]
    for i in range(durchFuehrungen):
        randomNumb = random.randint(0, obereGrenze - i)
        pulledNumb = allNumbs[randomNumb]
        lastNumb = allNumbs[obereGrenze  - i]
        allNumbs[obereGrenze - i] = pulledNumb
        allNumbs[randomNumb] = lastNumb
        pulledNumbs.append(pulledNumb)

    print(f'Gezogene Lottozahlen: {pulledNumbs}')
    return pulledNumbs


def ziehungen(anzahl):
    for _ in range(anzahl):
        pulledNumbs = lotto(44,6)
        Stats(pulledNumbs)


def Stats(pulledNumbs):
    for i in pulledNumbs:
        statsNumbs[i] += 1

def test():
    pass

if __name__ == "__main__":
    ziehungen(1000000)
    kak()
    keys = list(statsNumbs.keys())
    values = list(statsNumbs.values())
    plt.bar(keys, values)
    plt.title("Häufigkeit der Lottozahlen (1-45)")
    plt.xlabel("Lottozahlen")
    plt.ylabel("Häufigkeit")
    plt.xticks(keys)
    plt.show()
