import qslib.utils
import qslib.impatient_queue as iq

if __name__ == '__main__':
    sample = [1, 3, 5, 1, 8, 2, 1]
    lamb = qslib.utils.get_lambda(sample)  # 3
    print(lamb)
    n, m, mu, v = 3, 4, 3, 6
    ms = iq.get_all_metric(n, m, lamb, mu, v)

    for k in ms:
        print(f'{k:>8}: {ms[k]:10.4f}')

