# qslib
It is a package for analysis of queueing systems

## Examples
Make your service better with our analytics!

Analyse characteristics of your system:
```python
import qslib
# intensity is in person per hour
market = qslib.QS(input_intensity=50, output_intensity=20, channels=2)
market.prob['fail']     # probability that the client will leave
list(market.prob)       # probability of each state
market.number['queue']  # average number of people in the queue
market.time['queue']    # average queue time
```

Compare various systems configuration:
```python
import qslib
q1 = qslib.QS(input_intensity=4, output_intensity=2, channels=3,
              behaviour=qslib.SEPARATELY)
q2 = qslib.QS(input_intensity=4, output_intensity=2, channels=2,
              behaviour=qslib.UNANIMOUSLY)
q3 = qslib.QS(input_intensity=4, output_intensity=2, channels=2,
              behaviour=qslib.EVENLY)
qslib.compare(q1, q2, q3)
```

Build more complex systems with QSim and rate it:
```python
from qslib import QSim
qsim = QSim()
### Work In Progress
```

## TODOs
- [ ] write tests
- [ ] write Erlang Queueuing Systems module
- [ ] write simulator engine
- [ ] write simuator GUI
- [ ] write docs
