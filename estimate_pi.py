import random

def estimate_pi(num_samples): 
    pointsInCircle = 0 

    for i in range(num_samples): 
        x = random.random()
        y = random.random()
       
        if x*x + y*y <= 1: 
            pointsInCircle += 1   
       
    pi_estimate = 4 * pointsInCircle/num_samples
    return float(pi_estimate)