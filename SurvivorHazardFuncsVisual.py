import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import optimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from scipy.stats import multivariate_normal

import numpy as np
from scipy.stats import multivariate_normal



def survivor_series(x):
    return (math.e ** (-4 * x))


def survivor_parallel(x):
    return  ((math.e ** (-1 * x)) + (math.e ** (-3 * x)) - (math.e ** (-4 * x)))


def hazard_series(x):
    return 4


def hazard_parallel(x):
    return (((math.e ** (-1 * x)) + 3*(math.e ** (-3 * x)) - 4*(math.e ** (-4 * x)))/
            ((math.e ** (-1 * x)) + (math.e ** (-3 * x)) - (math.e ** (-4 * x))))


if __name__ == "__main__":
    # #   PART 1
    # with open("data.txt", "r") as f:
    #     x_val = np.arange(0 , 4, 0.10)
    #     survivor_series_y_values = []
    #     survivor_parallel_y_values = []
    #     print(x_val)
    #     for num in x_val:
    #         survivor_series_y_values.append(survivor_series(num))
    #         survivor_parallel_y_values.append(survivor_parallel(num))
    #     # plt.scatter(x_val, y_val)
    #     plt.plot(x_val, survivor_series_y_values, '-r', label="Series Circuit System Survivor Function")
    #     plt.plot(x_val, survivor_parallel_y_values, '-b', label="Parallel Circuit System Survivor Function")
    #     plt.legend()
    #     plt.title("Circuit System Survivor functions")
    #     plt.xlabel("t values")
    #     plt.ylabel("S(t)")
    #     # yfit = [a + b * xi for xi in x_val]
    #     # plt.plot(x_val, yfit, '-r')
    #     plt.show()
    #     plt.savefig('survivor_functions.png')

    # PART TWO

    # with open("data.txt", "r") as f:
    #     x_val = np.arange(0 , 4, 0.10)
    #     survivor_series_y_values = []
    #     survivor_parallel_y_values = []
    #     print(x_val)
    #     for num in x_val:
    #         survivor_series_y_values.append(hazard_series(num))
    #         survivor_parallel_y_values.append(hazard_parallel(num))
    #     # plt.scatter(x_val, y_val)
    #     plt.plot(x_val, survivor_series_y_values, '-r', label="Series Circuit System Hazard Function")
    #     plt.plot(x_val, survivor_parallel_y_values, '-b', label="Parallel Circuit System Hazard Function")
    #     plt.legend()
    #     plt.title("Circuit System Hazard functions")
    #     plt.xlabel("t values")
    #     plt.ylabel("h(t)")
    #     # yfit = [a + b * xi for xi in x_val]
    #     # plt.plot(x_val, yfit, '-r')
    #     plt.show()
    #     plt.savefig('hazard_functions.png')

    x, y = np.mgrid[-1.0:1.0:30j, -1.0:1.0:30j]

    # Need an (N, 2) array of (x, y) pairs.
    xy = np.column_stack([x.flat, y.flat])

    mu = np.array([0.0, 0.0])

    sigma = np.array([.5, .5])
    covariance = np.diag(sigma ** 2)

    z = multivariate_normal.pdf(xy, mean=mu, cov=covariance)

    # Reshape back to a (30, 30) grid.
    z = z.reshape(x.shape)

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z)
    # ax.plot_wireframe(x,y,z)

    plt.show()



