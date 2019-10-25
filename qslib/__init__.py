from . import utils
from ._probability_property import _ProbabilityProperty
from ._number_property import _NumberProperty
from ._time_proberty import _TimeProperty
from ._const import *

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
                # FIXME Should we store this value in TimeProperty?
                self._properties['input_period'] = kwargs['input_period']
                lamb = 1 / kwargs['input_period']
            else:
                lamb = utils.get_lambda(kwargs['input_sample'])

            self._properties['input_intensity'] = lamb
        return lamb

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
                # FIXME Should we store this value in TimeProperty?
                self._properties['holding_time'] = kwargs['holding_time']
                mu = 1 / kwargs['holding_time']
            else:
                # FIXME handle this case
                t_serve = utils.get_mean_t(kwargs['holding_time_sample'], 1)
                mu = 1 / t_serve

            self._properties['output_intensity'] = mu
        return mu

    def __init__(self, **kwargs):
        closed = kwargs.get('closed', False)
        n = kwargs.get('channels', 1)
        m = kwargs.get('queue', 0)

        # TODO add some behaviours
        behaviours = ['separately', 'unanimously', 'evenly']
        behaviour = kwargs.get('behaviour', SEPARATELY)
        if type(behaviour) is str:
            behaviour = behaviours.index(behaviour)
        if behaviour < 0 or behaviour > len(behaviours):
            raise ValueError('Incorrect behaviour. '
                             'It must be in (isolate, distribute)')

        # TODO read v
        v = kwargs.get('v', 0)

        if not closed:
            if behaviour == SEPARATELY:
                states = n + m + 1
            elif behaviour == UNANIMOUSLY:
                states = m + 2
            elif behaviour == EVENLY:
                states = n + m + 1
        else:
            pass  # TODO count states for closed systems

        # TODO Is _properties field necessary?
        #      Can we write properties just into self?
        self._properties = {
            'closed': closed,
            'channels': n,
            'queue': m,
            # TODO add v
            'behaviour': behaviours[behaviour],
            'states': states
        }

        lambda_ = self.__read_input_characteristic(kwargs)
        mu = self.__read_output_characteristic(kwargs)
        ro = lambda_ / mu
        self._properties['intensity_ratio_single'] = ro
        psi = ro / n
        self._properties['intensity_ratio_multi'] = psi
        self._properties['b'] = v / mu   # FIXME clear name

        self.prob = _ProbabilityProperty(self)
        self.time = _TimeProperty(self)
        self.number = _NumberProperty(self)

    def __getattr__(self, key):
        return self._properties[key]


# TODO Move this in utils
def compare(*args):
    for qs in args:
        pass  # TODO write compare algorithm


if __name__ == '__main__':
    q1 = QS(input_intensity=3, output_intensity=2, channels=2)
    q2 = QS(input_intensity=3, output_intensity=2, channels=2)
    print(q1.input_intensity)
