class _NumberProperty:
    def __init__(self, qs):
        self.qs = qs

    def __getitem__(self, i):
        if type(i) == int:
            return 0
        elif type(i) == str:
            if i == 'fail':
                return 1
            else:
                return -1
