def get_lambda(data):
    """
    Calculates the lambda parameter based on the passed sample

    :param data: sample of applicant frequency
    :type data: list of int
    :return: float
    """

    max_ = max(data)
    expected = 0
    a = []

    for i in range(max_ + 1):
        c = data.count(i)
        a.append(c)
        expected += c * i

    total = sum(a)

    if total == 0:
        return 0

    return expected / total


def get_mean_t(data, step):
    """
    Calculates the expected value of time based on the passed sample

    :param data: time distribution table
    :type data: list of int
    :param step: step in the time distribution table
    :type step: float
    :return: float
    """
    
    n = len(data)
    middles = [(i + 0.5) * step for i in range(n)]

    expected = 0
    for i in range(n):
        expected += middles[i] * data[i]

    total = sum(data)

    if total == 0:
        return 0

    return expected / total
