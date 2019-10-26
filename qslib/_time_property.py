class _TimeProperty:
    # TODO
    def __init__(self, qs):
        self.qs = qs

    def __getitem__(self, i):
        if i == 'lead':
            return 0
        elif i == 'wait':
            return 0
        elif i == 'work':
            return 0
        elif i == 'step':
            return 0
        else:
            return 0
