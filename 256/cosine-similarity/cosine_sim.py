import math

from sklearn.metrics.pairwise import cosine_similarity

X = [
        [3.06, 500, 6],
        [2.68, 320, 4],
        [2.92, 640, 6]
    ]

cosine_similarity(X)

def dot_product(X, Y, a=None, b=None):

    if not a or not b:
        return X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]
    else:
        return X[0] * Y[0] + X[1] * Y[1] * a**2 + X[2] * Y[2] * b**2

    # return f'{X[0] * Y[0]} + {X[1] * Y[1]}a^2 + {X[2] * Y[2]}b^2'

def mag(X, a=None, b=None):
    if not a or not b:
        return math.sqrt(X[0]**2 + X[1]**2 + X[2]**2)
    else:
        return math.sqrt(X[0]**2 + X[1]**2 * a + X[2]**2 * b)

def cos_sim(X, Y, a=None, b=None):
    return dot_product(X, Y, a, b) / (mag(X, a, b) * mag(Y, a, b))

dot_product([3.06, 500, 6],[2.68, 320, 4])
cos_sim([3.06, 500, 6],[2.68, 320, 4])
cos_sim([3.06, 500, 6],[2.92, 640, 6])
cos_sim([2.68, 320, 4],[2.92, 640, 6])


mag([3.06, 500, 6])

