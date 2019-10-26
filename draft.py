import qslib


if __name__ == '__main__':
    q1 = qslib.QS(arrival_rate=6, service_rate=1, channels=4,
                  behaviour=qslib.SEPARATELY)
    print(list(q1.prob))
    print('sum of probabilities = 1 ->', abs(sum(list(q1.prob)) - 1) < 1e-15)
    # q2 = qslib.QS(input_intensity=4, output_intensity=2, channels=2,
    #               behaviour=qslib.UNANIMOUSLY)
    # q3 = qslib.QS(input_intensity=4, output_intensity=2, channels=2,
    #               behaviour=qslib.EVENLY)
    # qslib.compare(q1, q2, q3)

