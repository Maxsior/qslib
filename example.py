import limited_queue as lq
import unlimited_queue as ulq
import impatient_queue as iq


if __name__ == '__main__':
    n, m, lamb, mu, v = 3, 4, 10, 3, 6
    ms = iq.get_all_metric(n, m, lamb, mu, v)

    for k in ms:
        print(f'{k:>8}: {ms[k]:10.4f}')

