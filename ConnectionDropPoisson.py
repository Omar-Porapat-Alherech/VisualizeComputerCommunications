import matplotlib.pyplot as plt
import math
import numpy


def main():
    x_values = numpy.array(list(float_mod_range(0, 10, 0.01)))
    first_plot = plt.figure(1)
    plt.xlim(0, 10)
    plt.ylim(0, 1)
    plt.plot(x_values, poisson_dist(0), "-r", label="n=0")
    plt.plot(x_values, poisson_dist(1), "-g", label="n=1")
    plt.plot(x_values, poisson_dist(2), "-b", label="n=2")
    plt.plot(x_values, poisson_dist(3), "-y", label="n=3")

    plt.title("The Poisson Distribution, lambda = 1")
    plt.xlabel("t(s)")
    plt.ylabel("$\mathregular{P_n}$(t)")
    plt.legend()
    first_plot.savefig("project_2_graph.png")
    first_plot.show()


def poisson_dist(n_val):
    x_values = numpy.array(list(float_mod_range(0, 10, 0.01)))
    lambda_val = 1
    y_value_arr = []
    # Equation for # Busy
    for t_val in x_values:
        y_val_eq = (((lambda_val*t_val)**n_val) * math.exp(-lambda_val*t_val))/(math.factorial(n_val))
        y_value_arr.append(y_val_eq)
    return y_value_arr


def float_mod_range(start, end, step):
    while start < end or start == end:
        yield start
        # Too many decimals
        start = round(start + step, 2)


if __name__ == '__main__':
    main()


