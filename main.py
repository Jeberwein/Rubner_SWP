import random
import matplotlib.pyplot as plt

statsNumbs = {i: 0 for i in range(1, 46)}


def lotto():
    pulledNumbs = []
    allNumbs = [i for i in range(1, 46)]
    for i in range(6):
        randomNumb = random.randint(0, 44 - i)
        pulledNumb = allNumbs[randomNumb]
        lastNumb = allNumbs[44 - i]
        allNumbs[44 - i] = pulledNumb
        allNumbs[randomNumb] = lastNumb
        pulledNumbs.append(pulledNumb)

    print(f'Gezogene Lottozahlen: {pulledNumbs}')
    return pulledNumbs


def ziehungen(anzahl=1000):
    for _ in range(anzahl):
        pulledNumbs = lotto()
        Stats(pulledNumbs)


def Stats(pulledNumbs):
    for i in pulledNumbs:
        statsNumbs[i] += 1


if __name__ == "__main__":
    ziehungen()
    keys = list(statsNumbs.keys())
    values = list(statsNumbs.values())
    plt.bar(keys, values)
    plt.title("Häufigkeit der Lottozahlen (1-45)")
    plt.xlabel("Lottozahlen")
    plt.ylabel("Häufigkeit")
    plt.xticks(keys)
    plt.show()
