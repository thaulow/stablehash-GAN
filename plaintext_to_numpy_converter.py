import os
from numpy import genfromtxt
import numpy

input = '/home/ubuntu/trainingfiles/frgc_cluster_centers/'
output = '/home/ubuntu/trainingfiles/frgc_centers_converted/'
if not os.path.exists(output):
    os.makedirs(output)

for filename in os.listdir(input):
    if not filename.startswith('.'):
        print(filename)
        cluster_center = genfromtxt(os.path.join(input, filename), delimiter=',')
        print(cluster_center)
        numpy.save(os.path.join(output, filename), numpy.array(cluster_center))
