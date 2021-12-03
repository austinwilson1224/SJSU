import numpy as np 
import pandas as pd 

'''
    @x: numpy array containing the data we want to cluster

    example 
    [
        [1,2],
        [3,4],
        [5,6]
     ]
'''
example_data = [
        [1,2],
        [3,4],
        [5,6]]
c1 = [1,3,5]
c2 = [2,4,6]
tr = np.column_stack([c1,c2])
tr
example_data2 = np.array(example_data)
example_data3 = pd.DataFrame(example_data)
example_data3 = np.array(example_data3)
example_data3

example_data
example_data2
example_data3
len(example_data)
len(example_data2)
len(example_data3)
example_data.shape[1]
def k_means(x,k):
    # these are the initialized cluster values
    # there are k value we need to calculate distance from 
    # each value is same dimension as x
    x = np.array(x)
    k_means = np.random.randint(low=1, high=5, size=(k, x.shape[1]))

    # number of records in dataset n
    n =  len(x)

    for i in range(n):
        distances = []
        for j in range(k):
            l1_dist = np.linalg.norm((x[i]-k_means[j]))
            distances.append(l1_dist)
        cluster_number = np.argmin(distances)
        k_means[cluster_number] = np.mean([k_means[cluster_number], x[i]], axis=0)

    return k_means

test = k_means(example_data, 2)
test2 = k_means(example_data2, 2)
test3 = k_means(example_data3, 2)
test
test2
test3
