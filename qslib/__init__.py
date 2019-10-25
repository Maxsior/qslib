from qslib import utils

name = "qslib"


class QS:
    def __read_input_characteristic(self, kwargs):
        characteristic = ['input_intensity' in kwargs,
                          'input_period' in kwargs,
                          'input_sample' in kwargs]
        if characteristic.count(True) != 1:
            raise KeyError('Input stream characteristic is incorrect. '
                           'Please, pass ONE of this parameters: '
                           'input_intensity, input_period, input_sample')
        else:
            if characteristic[0]:
                lamb = kwargs['input_intensity']
            elif characteristic[1]:
                self.properties['input_period'] = kwargs['input_period']
                lamb = 1 / kwargs['input_period']
            else:
                lamb = utils.get_lambda(kwargs['input_sample'])

            self.properties['input_intensity'] = lamb

    def __read_output_characteristic(self, kwargs):
        characteristic = ['output_intensity' in kwargs,
                          'holding_time' in kwargs,
                          'holding_time_sample' in kwargs]
        if characteristic.count(True) != 1:
            raise KeyError('Output stream characteristic is incorrect. '
                           'Please, pass ONE of this parameters: '
                           'output_intensity, holding_time, '
                           'holding_time_sample')
        else:
            if characteristic[0]:
                mu = kwargs['output_intensity']
            elif characteristic[1]:
                self.properties['holding_time'] = kwargs['holding_time']
                mu = 1 / kwargs['holding_time']
            else:
                # FIXME handle this case
                t_serve = utils.get_mean_t(kwargs['holding_time_sample'], 1)
                mu = 1 / t_serve

            self.properties['output_intensity'] = mu

    def __init__(self, **kwargs):
        closed = kwargs.get('closed', False)
        n = kwargs.get('channels', 1)
        m = kwargs.get('queue', 0)

        # TODO add some behaviours
        # TODO handle case when behaviour is out of bounds
        behaviours = {'isolate': 0, 'distribute': 1}
        behaviour = kwargs.get('behaviour', 0)
        if type(behaviour) is str:
            behaviour = behaviours.get(behaviour, -1)

        if behaviour < 0 or behaviour > len(behaviours.keys()):
            raise ValueError('Incorrect behaviour. '
                             'It must be in (isolate, distribute)')

        # TODO read v
        v = kwargs.get('v', 0)

        self.properties = {
            'closed': closed,
            'channels': n,
            'queue': m,
            # TODO add v
        }

        lamb = self.__read_input_characteristic(kwargs)
        mu = self.__read_output_characteristic(kwargs)

    @property
    def probs(self):
        # TODO access to probabilities
        return []


if __name__ == '__main__':
    q1 = QS(input_intensity=3, output_intensity=2, channels=2)

