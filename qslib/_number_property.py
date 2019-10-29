class _NumberProperty:
    def __init__(self, qs):
        self.qs = qs
        self.num_list = dict.fromkeys(['queue', 'system', 'service'])

    def __getitem__(self, i):
        if i == 'queue':
            return 0
        elif i == 'system':
            return 0
        elif i == 'service':
            return 0
        else:
            raise Exception("Invalid input")

    def _get_prod(self, i):
        n = self.qs.channels
        b = self.qs.b
        prod = 1
        for l in range(1, i + 1):
            prod *= (n + l * b)
        return prod

    def _get_n_queue_(self):
        if self.num_list['queue'] != None:
            return self.num_list['queue']
        else:
            n = self.qs.channels
            m = self.qs.queue
            ro = self.qs.utilization_ratio

            pn = self.qs.prob[n]
            s = 0

            for i in range(1, m + 1):
                s += i * ro ** i / self._get_prod(i)

            return pn * s

    def _get_n_service_(self):
        if self.num_list['service'] != None:
            return self.num_list['service']
        else:
            n = self.qs.channels
            m = self.qs.queue

            sum0 = 0
            for k in range(1, n + 1):
                sum0 += k * self.qs.prob[k]

            sum1 = 0
            for i in range(1, m + 1):
                sum1 += n * self.qs.prob[n + i]

            return sum0 + sum1

    def _get_n_system_(self):
        if self.num_list['system'] != None:
            return self.num_list['system']
        else:
            n_serv = self._get_n_service_()
            n_queue = self._get_n_queue_()
            return n_serv + n_queue
