import matpy as mp

def buildFunction(data, degree):
    arr = []
    for n in range(degree+1):
        arr.append([x**n for x in data])

    return mp.Matrix(arr,'col')
