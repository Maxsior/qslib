from . import utils
from ._probability_property import _ProbabilityProperty
from ._number_property import _NumberProperty
from ._time_property import _TimeProperty
from ._const import *

name = "qslib"


class QS:
    def __read_arrival_rate(self, kwargs):
        characteristic = ['arrival_rate' in kwargs,
                          'input_period' in kwargs,  # FIXME clear name
                          'arrival_rate_sample' in kwargs]
        if characteristic.count(True) != 1:
            raise KeyError('Input stream characteristic is incorrect. '
                           'Please, pass ONE of this parameters: '
                           'arrival_rate, input_period, arrival_rate_sample')
        else:
            if characteristic[0]:
                lamb = kwargs['arrival_rate']
            elif characteristic[1]:
                # FIXME Should we store this value in TimeProperty?
                # self._properties['input_period'] = kwargs['input_period']
                lamb = 1 / kwargs['input_period']
            else:
                lamb = utils.get_lambda(kwargs['arrival_rate_sample'])

            self.arrival_rate = lamb
        return lamb

    def __read_service_rate(self, kwargs):

        characteristic = ['service_rate' in kwargs,
                          'holding_time' in kwargs,
                          'holding_time_sample' in kwargs]

        if characteristic.count(True) != 1:
            raise KeyError('Output stream characteristic is incorrect. '
                           'Please, pass ONE of this parameters: '
                           'service_rate, holding_time, '
                           'holding_time_sample')
        else:
            if characteristic[0]:
                mu = kwargs['service_rate']
            elif characteristic[1]:
                # FIXME Should we store this value in TimeProperty?
                # self._properties['holding_time'] = kwargs['holding_time']
                mu = 1 / kwargs['holding_time']
            else:
                # FIXME handle this case
                t_serve = utils.get_mean_t(kwargs['holding_time_sample'], 1)
                mu = 1 / t_serve

            self.output_intensity = mu
        return mu

    def __read_dropout_rate(self, kwargs):
        characteristic = ['dropout_rate' in kwargs,
                          'mean_time_in_queue' in kwargs,
                          'time_in_queue_sample' in kwargs]

        if characteristic.count(True) != 1:
            raise KeyError('Output stream characteristic is incorrect. '
                           'Please, pass ONE of this parameters: '
                           'dropout_rate, time_in_queue_sample, '
                           'time_in_queue_sample')
        else:
            if characteristic[0]:
                v = kwargs['dropout_rate']
            elif characteristic[1]:
                # FIXME Should we store this value in TimeProperty?
                # self._properties['holding_time'] = kwargs['holding_time']
                v = 1 / kwargs['mean_time_in_queue']
            else:
                # FIXME handle this case
                t_queue = utils.get_mean_t_queue(kwargs['time_in_queue_sample'], 1)
                v = 1 / t_queue

        self.dropout_rate = v
        return v

    def __init__(self, **kwargs):
        self.closed = kwargs.get('closed', False)
        self.channels = kwargs.get('channels', 1)
        self.queue = kwargs.get('queue', 0)

        self.behaviour = kwargs.get('behaviour', SEPARATELY)
        if self.behaviour < 0:
            raise ValueError('Incorrect behaviour. '
                             'It must be in (isolate, distribute)')

        if not self.closed:
            if self.behaviour == SEPARATELY:
                self.states = self.channels + self.queue + 1
            elif self.behaviour == UNANIMOUSLY:
                self.states = self.queue + 2
            elif self.behaviour == EVENLY:
                self.states = self.channels + self.queue + 1
        else:
            pass

        v = self.__read_dropout_rate(kwargs)
        lambda_ = self.__read_arrival_rate(kwargs)
        mu = self.__read_service_rate(kwargs)
        self.utilization_ratio = lambda_ / mu
        psi = self.utilization_ratio / self.channels
        self.intensity_ratio_multi = psi
        self.b = v / mu   # FIXME clear name

        self.prob = _ProbabilityProperty(self)
        self.time = _TimeProperty(self)
        self.number = _NumberProperty(self)


# TODO Move this in utils
def compare(*args):
    for qs in args:
        pass  # TODO write compare algorithm
