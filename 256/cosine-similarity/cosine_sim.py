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




##################################################################################################################
'''
Austin Wilson 
Sep 22 2021
SJSU CMPE 272
python source code for cosine similarity homework 
'''
import math
from sklearn.metrics.pairwise import cosine_similarity
A = [3.06, 500, 6]
B = [2.68, 320, 4]
C = [2.92, 640, 6]

A1 = [3.06, 5, 3]
B1 = [2.68, 3.2, 2]
C1 = [2.92, 6.4, 3]
# these values are to test the cosine similarity using sklearn 
AB = [A, B]
AC = [A, C]
BC = [B, C]

AB1 = [A1, B1]
AC1 = [A1, C1]
BC1 = [B1, C1]

# calculate coefficients
def calc_coefficients_numerator(X, Y):
    return X[0] * Y[0], X[1] * Y[1], X[2] * Y[2]

def calc_coefficients_denominator(X, Y):
    x1_squared = X[0] ** 2
    x2_squared = X[1] ** 2
    x3_squared = X[2] ** 2
    
    y1_squared = Y[0] ** 2
    y2_squared = Y[1] ** 2
    y3_squared = Y[2] ** 2

    constant_term = x1_squared * y1_squared
    alpha2 = x1_squared * y2_squared + x2_squared * y1_squared
    beta2 = x1_squared * y3_squared + x3_squared * y1_squared
    alpha2_beta2 = x2_squared * y3_squared + x3_squared * y2_squared
    alpha4 = x2_squared * y2_squared
    beta4 = x3_squared * y3_squared
    return constant_term, alpha2, beta2, alpha2_beta2, alpha4, beta4

def cosdist(alpha, beta, a,b,c,d,e,f,g,h,i):
    alpha2 = alpha ** 2
    beta2 = beta ** 2
    numerator = a + b * alpha2 + c * beta2
    denominator = d + e * alpha2 + f * beta2 + g * alpha2 * beta2 + h * alpha ** 4 + i * beta ** 4
    return numerator / math.sqrt(denominator)

print(f'for A={A} B={B}')
a, b, c = calc_coefficients_numerator(A, B)
d, e, f, g, h, i = calc_coefficients_denominator(A, B)
coeff = f'a={a} b={b} c={c} d={d} e={e} f={f} g={g} h={h} i={i}'
cos_sim = cosdist(1,1,a,b,c,d,e,f,g,h,i)
cos_sim2 = cosdist(.01,.5,a,b,c,d,e,f,g,h,i)
cos_sim_sklearn = cosine_similarity(AB)[0][1]
cos_sim_sklearn1 = cosine_similarity(AB)[0][1]
theta_ab1 = math.acos(cos_sim)
theta_ab2 = math.acos(cos_sim2)
print(coeff)
print(f"cosine distance from calculation: {cos_sim}\ncosine distance from sklearn:     {cos_sim_sklearn}\n\n")
print(f"for alpha=beta=1 angle between A and B is: {theta_ab1}")
print(f"for alpha=.01 beta=.5 angle between A and B is: {theta_ab2}\ncosine similarity is:{cos_sim2}")

print(f'for A={A} C={C}')
a, b, c = calc_coefficients_numerator(A, C)
d, e, f, g, h, i = calc_coefficients_denominator(A, C)
coeff = f'a={a} b={b} c={c} d={d} e={e} f={f} g={g} h={h} i={i}'
cos_sim = cosdist(1,1,a,b,c,d,e,f,g,h,i)
cos_sim2 = cosdist(.01,.5,a,b,c,d,e,f,g,h,i)
cos_sim_sklearn = cosine_similarity(AC)[0][1]
cos_sim_sklearn2 = cosine_similarity(AC)[0][1]

theta_ac1 = math.acos(cos_sim)
theta_ac2 = math.acos(cos_sim2)
print(coeff)
print(f"cosine distance from calculation: {cos_sim}\ncosine distance from sklearn:     {cos_sim_sklearn}\n\n")
print(f"for alpha=beta=1 angle between A and C is: {theta_ac1}")
print(f"for alpha=.01 beta=.5 angle between A and C is: {theta_ac2}\ncosine similarity is:{cos_sim2}")

print(f'for B={B} C={C}')
a, b, c = calc_coefficients_numerator(B, C)
d, e, f, g, h, i = calc_coefficients_denominator(B, C)
coeff = f'a={a} b={b} c={c} d={d} e={e} f={f} g={g} h={h} i={i}'
cos_sim = cosdist(1,1,a,b,c,d,e,f,g,h,i)
cos_sim2 = cosdist(.01,.5,a,b,c,d,e,f,g,h,i)
cos_sim_sklearn = cosine_similarity(BC)[0][1]
cos_sim_sklearn3 = cosine_similarity(BC)[0][1]
theta_bc1 = math.acos(cos_sim)
theta_bc2 = math.acos(cos_sim2)
print(coeff)
print(f"cosine distance from calculation: {cos_sim}\ncosine distance from sklearn:     {cos_sim_sklearn}\n\n")
print(f"for alpha=beta=1 angle between B and C is: {theta_bc1}")
print(f"for alpha=.01 beta=.5 angle between B and C is: {theta_bc2}\ncosine similarity is:{cos_sim2}")




'''åå≈ç√∫˜µ≤≥÷æ…¬˚∆˙©ƒ∂ß∂ßœ∑´®†¥¨ˆøπ“‘'''
##################################################################################################################


cos_sim_sklearn1
cos_sim_sklearn2
cos_sim_sklearn3