

import sqlite3
import numpy as np
import matplotlib.pyplot as plt


# https://extendsclass.com/sqlite-browser.html




def fetch():
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()

    c.execute('SELECT pulso FROM sensor')
    data = c.fetchall()
    return data

def show(data):

    fig = plt.figure()
    fig.suptitle('Evolución del ritmo cardíaco', fontsize=15)
    ax = fig.add_subplot()

    ax.plot(data, c='red', label='Pulso')
    ax.legend()
    ax.grid()
    plt.show()

def estadistica(data):

    valor_medio = np.mean(data)
    valor_min = np.min(data)
    valor_max = np.max(data)
    valor_std = np.std(data)

    print('El valor medio del pulso es:', round(valor_medio))
    print('El valor mínimo del pulso es:', valor_min)
    print('El valor máximo del pulso es:', valor_max)
    print('El desvío estandar del pulso es:', round(valor_std))


def regiones(data):

    valor_mean = np.mean(data)
    valor_std = np.std(data)

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    for i in range(len(data)):
        if data[i] <= (valor_mean-valor_std):
            x1.append(i)
            y1.append(data[i])
        elif data[i] >= (valor_mean+valor_std):
            x2.append(i)
            y2.append(data[i])
        else:
            x3.append(i)
            y3.append(data[i])


    fig = plt.figure()
    fig.suptitle('Regiones del pulso', fontsize=15)
    ax = fig.add_subplot()

    ax.scatter(x1, y1, c='cyan', label='Aburrido')
    ax.scatter(x3, y3, c='green', label='Tranquilo')
    ax.scatter(x2, y2, c='purple', label='Entusiasmado')
    ax.legend()
    ax.grid()
    plt.show()




if __name__ == '__main__':

    data = fetch()
    show(data)
    estadistica(data)
    regiones(data)