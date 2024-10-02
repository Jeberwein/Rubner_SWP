import random
import matplotlib.pyplot as plt
statsNumbs = {i: 0 for i in range(1, 46)}
def lotto():
    for g in range(1000):
        PulledNumbs = []
        for i in range(6):
            AllNumbs = [i for i in range(1, 46)]
            randomNumb = random.randint(0, 44 - i)
            PulledNumb = AllNumbs[randomNumb]
            lastNumb = AllNumbs[44 - i]
            AllNumbs[44 - i] = PulledNumb
            AllNumbs[randomNumb] = lastNumb
            PulledNumbs.append(PulledNumb)
        Stats(PulledNumbs)
def Stats(PulledNumbs):
    for i in PulledNumbs:
        statsNumbs[i] += 1

if __name__ == "__main__":
    lotto()
    keys = list(statsNumbs.keys())
    values = list(statsNumbs.values())
    plt.bar(keys, values)
    plt.title("Häufigkeit der Lottozahlen (1-45)")
    plt.xlabel("Lottozahlen")
    plt.ylabel("Häufigkeit")
    plt.xticks(keys)
    plt.show()
