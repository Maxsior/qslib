from math import factorial


def get_p0(n, ro):
    psi = ro / n
    if psi > 1:
        # FIXME обработать случай psi > 1
        raise ValueError("lamb > ro")

    s = 1
    x = 1
    for k in range(1, n):
        x *= ro / k
        s += x

    if psi < 1:
        s += x * ro / (n - ro)

    return 1 / s


def get_n_queue(n, ro, p0):
    # FIXME psi == 1
    return ro ** (n + 1) / factorial(n - 1) / (n - ro) ** 2 * p0


def get_all_metric(n, lamb, mu):
    ro = lamb / mu
    p0 = get_p0(n, ro)
    p_fail = 0
    Q = 1
    A = lamb
    K = ro  # n_serv
    n_queue = get_n_queue(n, ro, p0)
    t_queue = n_queue / lamb
    t_sys = K / lamb + t_queue
    n_sys = lamb * t_sys
    nu = K / n

    return {
        'P0': p0,
        'P_fail': p_fail,
        'K': K,
        'N_queue': n_queue,
        'T_queue': t_queue,
        'N_sys': n_sys,
        'T_sys': t_sys,
        'nu': nu,
        'Q': Q,
        'A': A 
    }
