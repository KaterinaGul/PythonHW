import numpy as np
import matplotlib.pyplot as plt

def zadacha1():
    x_list = []
    y_list = []

    for x in range (-10, 11):
        y = 5*x*x + 10*x -30
        x_list.append(x)
        y_list.append(y)

    plt.axhline(y=0, color = "r", linestyle = "--")

    plt.plot(y_list)
    plt.show()


def zadacha2():
    size = 15
    houses = np.random.randint(100, 300, size)
    prices = np.random.randint(3000000, 20000000, size)
    mean_pr = [round(prices[i]/ houses[i]) for i in range(len(prices))]
    print(mean_pr)
    house_names = ["дом 1", "дом 2","дом 3","дом 4","дом 5","дом 6","дом 7","дом 8","дом 9","дом 10","дом 11","дом 12","дом 13","дом 14","дом 15" ]

    plt.axhline(y = 50000, color = "b", linestyle = "--")

    plt.bar(house_names, mean_pr)
    plt.show()