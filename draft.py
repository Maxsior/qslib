import qslib.limited_queue as lq


def beauty_print(d):
    for k in d:
        print(f'{k:>8}: {ms[k]:10.4f}')
    print('\n')


if __name__ == '__main__':
    n, m, lamb, mu = 1, 9, 6, 3 * 3
    ms = lq.get_all_metric(n, m, lamb, mu)
    beauty_print(ms)

    n, m, lamb, mu = 3, 7, 6, 3
    ms = lq.get_all_metric(n, m, lamb, mu)
    beauty_print(ms)

    n, m, lamb, mu = 1, 9, 6, 9
    ms = lq.get_all_metric(n, m, lamb, mu)
    beauty_print(ms)


