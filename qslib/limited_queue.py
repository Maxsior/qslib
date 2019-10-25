from math import factorial


def get_p0(n, m, ro):
    s = 1
    x = 1
    for k in range(1, n + 1):
        x *= ro / k
        s += x

    x2 = x
    for k in range(n+1, n+m+1):
        x2 *= ro / n
        s += x2

    return 1 / s


def get_p0_psi(n, m, psi):
    if psi == 1:
        s = 1
        x = 1
        for k in range(1, n + 1):
            x *= n / k
            s += x

        s += x * m

        return 1 / s
    else:
        raise ValueError('TODO get_p0_psi, when psi != 1')


def get_p_fail(n, m, psi, p0):
    return n**n / factorial(n) * psi**(n + m) * p0


def get_n_queue(n, m, psi, p0):
    if psi != 1:
        return (
            n**n / factorial(n) * psi**(n + 1)
            *
            (1 - psi**m * (m + 1 - m * psi)) / (1 - psi)**2
        ) * p0
    else:
        return n**n / factorial(n) * m * (m + 1) / 2 * p0


def get_all_metric(n, m, lamb, mu):
    ro = lamb / mu
    psi = ro / n
    p0 = get_p0(n, m, ro)

    p_fail = get_p_fail(n, m, psi, p0)
    Q = 1 - p_fail
    A = lamb * Q
    K = ro * Q
    n_queue = get_n_queue(n, m, psi, p0)
    t_queue = n_queue / lamb
    t_sys = K / lamb + t_queue
    nu = K / n
    
    return {
        'P0': p0,
        'P_fail': p_fail,
        'K': K,
        'N_queue': n_queue,
        'T_queue': t_queue,
        'T_sys': t_sys,
        'nu': nu,
        'Q': Q,
        'A': A 
    }
