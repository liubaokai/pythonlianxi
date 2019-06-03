def printResult(inputs):
    reversInput = dict()
    for k, v in inputs.items():
        reversInput[v] = k
    start = None
    for k, v in inputs.items():
        if k not in reversInput:
            start = k
            break
    if start = None:
        return
    to = inputs[start]
    print(start + '->' + to)
    start = to
    to = inputs[to]
    while to != None:
        print(',' + start + '->' + to)
        start = to
        to = inputs[to]
