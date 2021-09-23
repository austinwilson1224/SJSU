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
cosine_similarity(BC)
def get_sk_cos_sim_round(X):
    cos_sim = cosine_similarity(X)[0][1]
    return round(math.acos(cos_sim) * 180 / math.pi, 2)

get_sk_cos_sim_round(AB)
get_sk_cos_sim_round(AB1)
get_sk_cos_sim_round(AC)
get_sk_cos_sim_round(AC1)
get_sk_cos_sim_round(BC)
get_sk_cos_sim_round(BC1)


def get_sk_cos_sim_round_rad(X):
    cos_sim = cosine_similarity(X)[0][1]
    return round(math.acos(cos_sim), 4)


get_sk_cos_sim_round_rad(AB)
get_sk_cos_sim_round_rad(AC)
get_sk_cos_sim_round_rad(BC)

b = [
    get_sk_cos_sim_round_rad(AB),
    get_sk_cos_sim_round_rad(AC),
    get_sk_cos_sim_round_rad(BC)
    ]


get_sk_cos_sim_round_rad(AB1)
get_sk_cos_sim_round_rad(AC1)
get_sk_cos_sim_round_rad(BC1)

c = [
    get_sk_cos_sim_round_rad(AB1),
    get_sk_cos_sim_round_rad(AC1),
    get_sk_cos_sim_round_rad(BC1)
]



b

c 





cs_ab = cosine_similarity(AB)[0][1]
cs_ab1 = cosine_similarity(AB1)[0][1]
cs_ab
cs_ab1
round(math.acos(cs_ab) * 180 / math.pi, 2)

cs_ac = cosine_similarity(AC)
cs_ac1 = cosine_similarity(AC1)

cs_bc = cosine_similarity(BC)
cs_bc1 = cosine_similarity(BC1)