from math import factorial


def _get_prod(i, b, n):
    prod = 1
    for l in range(1, i + 1):
        prod *= (n + l * b)
    return prod


def get_p0(ro, b, n, m):
    sum0 = 1
    x0 = 1
    for i in range(1, n + 1):
        x0 *= ro / i
        sum0 += x0

    sum1 = 0
    x1 = 1
    for i in range(1, m + 1):
        x1 *= ro
        sum1 += x1 / _get_prod(i, b, n)

    return 1 / (sum0 + sum1 * x0)


def get_p_k(k, n, b, ro, p0):
    if k <= n:
        return p0 * ro ** k / factorial(k)
    else:
        pn = ro ** n / factorial(n) * p0
        i = k - n
        return pn * ro ** i / _get_prod(i, b, n)


def get_p_fail(m, n, b, ro, p0):
    return get_p_k(n + m, n, b, ro, p0)


def get_p_idle(n, ro, p0):
    p = p0
    s = p
    for k in range(1, n):
        p *= ro / k
        s += p
    return s


def get_p_queue(m, n, b, ro, p0):
    pn = get_p_k(n, n, b, ro, p0)
    s = 1
    for i in range(1, m):
        s += ro ** i / _get_prod(i, b, n)

    return pn * s


def get_n_serv(m, n, b, ro, p0):
    sum0 = 0
    for k in range(1, n + 1):
        sum0 += k * get_p_k(k, n, b, ro, p0)

    sum1 = 0
    for i in range(1, m + 1):
        sum1 += n * get_p_k(n + i, n, b, ro, p0)

    return sum0 + sum1


def get_n_queue(m, n, b, ro, p0):
    pn = get_p_k(n, n, b, ro, p0)
    s = 0
    for i in range(1, m + 1):
        s += i * ro ** i / _get_prod(i, b, n)

    return pn * s


def get_all_metric(n=1, m=0, lamb, mu, v=0):
    b = v / mu
    ro = lamb / mu
    p0 = get_p0(ro, b, n, m)

    p_fail = get_p_fail(m, n, b, ro, p0)
    p_idle = get_p_idle(n, ro, p0)
    p_queue = get_p_queue(m, n, b, ro, p0)
    n_queue = get_n_queue(m, n, b, ro, p0)  # t_wait * lamb
    n_serv = get_n_serv(m, n, b, ro, p0)
    n_sys = n_serv + n_queue
    Q = 1 - p_fail

    return {
        "N_queue": n_queue,
        "N_serv": n_serv,
        "N_sys": n_sys,
        "T_queue": n_queue / lamb,
        "T_sys": n_sys / lamb,
        "T_serv": n_serv / lamb,
        "P_idle": p_idle,  # FIXME
        "P_fail": p_fail,
        "P_queue": p_queue,
        "P0": p0,
        "Q": Q,
        "A": lamb * Q
    }

