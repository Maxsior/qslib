class _NumberProperty:
    # TODO
    def __init__(self, qs):
        self.qs = qs

    def __getitem__(self, i):
        if i == 'queue':
            return 0
        elif i == 'system':
            return 0
        elif i == 'service':
            return 0
        else:
            return 0
