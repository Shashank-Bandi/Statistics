import numpy
#Variance
a =[3.9,3.9,3.85,3.08,3.15,2.76,3.21,3.69,
    3.92,3.92,3.92,3.07,3.07,3.07,2.93,3,3.23,
    4.08,4.93,4.22,3.7,2.76,3.15,3.73,3.08,4.08,
    4.43,3.77,4.22,3.62,3.54,4.11]
points = list(a)
#print("Points are",points)To check if the data is getting converted into list or not
b =[2.62,2.875,2.32,3.215,3.44,3.46,3.57,3.19,3.15,3.44,
    3.44,4.07,3.73,3.78,5.25,5.424,5.345,2.2,1.615,1.835,
    2.465,3.52,3.435,3.84,3.845,1.935,2.14,1.513,3.17,2.77,
    3.57,2.78]
score = list(b)
#print("Scores are",score) To check if the data is getting converted into list or not
c =[16.46,17.02,18.61,19.44,17.02,20.22,15.84,20,22.9,18.3,
    18.9,17.4,17.6,18,17.98,17.82,17.42,19.47,18.52,19.9,20.01,
    16.87,17.3,15.41,17.05,18.9,16.7,16.9,14.5,15.5,14.6,18.6]
weights = list(c)

print("Variance of points is",numpy.var(points))
print("Variance of scores is",numpy.var(score))

print("Variance of Weights is",numpy.var(weights))
