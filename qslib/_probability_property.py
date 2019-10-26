from math import factorial


class _ProbabilityProperty:
    def __init__(self, qs):
        self.qs = qs
        self.prob_list = [-1.] * qs.states

    def __getitem__(self, i):
        if type(i) == int:
            return self.get_p_k(i)
        elif type(i) == str:
            if i == 'fail':
                return self.get_p_k(self.qs.states - 1)
            else:
                # TODO add p_queue, p_idle, ...
                return -1

    def _get_prod(self, i):
        n = self.qs.channels
        b = self.qs.b
        prod = 1
        for l in range(1, i + 1):
            prod *= (n + l * b)
        return prod

    def get_p0(self):
        if self.prob_list[0] != -1:
            return self.prob_list[0]

        ro = self.qs.utilization_ratio
        n = self.qs.channels
        m = self.qs.queue

        sum0 = 1
        x0 = 1
        for i in range(1, n + 1):
            x0 *= ro / i
            sum0 += x0

        sum1 = 0
        x1 = 1
        for i in range(1, m + 1):
            x1 *= ro
            sum1 += x1 / self._get_prod(i)

        self.prob_list[0] = 1 / (sum0 + sum1 * x0)
        return self.prob_list[0]

    def get_p_k(self, k):
        if self.prob_list[k] != -1:
            return self.prob_list[k]

        p0 = self.get_p0()
        ro = self.qs.utilization_ratio
        n = self.qs.channels

        if k <= self.qs.channels:
            self.prob_list[k] = p0 * ro ** k / factorial(k)
        else:
            pn = ro ** n / factorial(n) * p0
            i = k - n
            self.prob_list[k] = pn * ro ** i / self._get_prod(i)

        return self.prob_list[k]
