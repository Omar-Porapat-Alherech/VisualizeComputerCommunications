import matplotlib.pyplot as plt
import random
import numpy


def main():
    busy_packets_avg = []
    dropped_packets_avg = []
    x_values = numpy.array(list(float_mod_range(0, 1, 0.04)))
    for p in x_values:
        dropped_packets = 0
        busy_packets = 0
        for iteration in range(0, 10000):
            input_counter = 0
            for i in range(0, 10):
                rand_int = random.random()
                if rand_int < p:
                    input_counter += 1
            if input_counter is 0:
                busy_packets += 0
                continue
            if input_counter > 3:
                dropped_packets += input_counter - 3
                busy_packets += 3
            else:
                busy_packets += input_counter
        busy_packets_avg.append(packet_avg(busy_packets))
        dropped_packets_avg.append(packet_avg(dropped_packets))
    first_plot = plt.figure(1)
    plt.plot(x_values, dropped_packets_avg, "-b", label="Simulated Average Calculation")
    plt.plot(x_values, dropped_sig_eq(), "-r", label="Model Equation Curve")
    plt.xlabel("Probability of arrival")
    plt.ylabel("Average Number of dropped packets")
    plt.title("Avg Number of dropped packets VS p")
    plt.legend()
    first_plot.show()
    # Busy output plots
    second_plot = plt.figure(2)
    plt.plot(x_values, busy_packets_avg, "-b", label="Simulated Average Calculation")
    plt.plot(x_values, busy_eq(),  "-r", label="Model Equation Curve")
    plt.xlabel("Probability of arrival")
    plt.ylabel("Average Number of busy outputs")
    plt.title("Avg Number of busy outputs VS p")
    plt.legend()
    second_plot.show()


def packet_avg(tenk_trial_total):
    return tenk_trial_total/10000


def busy_eq():
    x_values = numpy.array(list(float_mod_range(0, 1, 0.04)))
    y_value_arr = []
    # Equation for # Busy
    for val in x_values:
        y_val_eq = 3 - (3*(1 - val) ** 10) - (20 * val * ((1 - val) ** 9)) - (
                45 * (val ** 2) * ((1 - val) ** 8))
        y_value_arr.append(y_val_eq)
    return y_value_arr


def dropped_sig_eq():
    x_values = numpy.array(list(float_mod_range(0, 1, 0.04)))
    y_value_arr = []
    # Equation for # dropped
    for val in x_values:
        y_val_eq = (210 * 1 * (val**4) * ((1-val)**6)) + (252 * 2 * (val**5) * ((1-val)**5)) + (210 * 3 * (val**6) * ((1-val)**4)) \
        + (120 * 4 * (val ** 7) * ((1 - val) ** 3)) + (45 * 5 * (val**8)*((1-val)**2)) + (10 * 6 * (val**9)*((1-val)**1)) \
        + (1 * 7 * (val**10)*((1-val)**0))
        y_value_arr.append(y_val_eq)
    return y_value_arr


def float_mod_range(start, end, step):
    while start < end or start == end:
        yield start
        # Too many decimals
        start = round(start + step, 2)


if __name__ == '__main__':
    main()
