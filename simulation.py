from utils import *


with open('data.txt', 'a+') as f:
    answer = [0, 0]
    for i in range(1, 1000):
        for j in xrange(1, 1000, 0.5):
            config = dict()
            omega = i/500
            v = j/100 + 1
            theta = 0
            t, r = 0.001, 0.02
            g = 9.8
            coeff = 0.5
            print(i, j, v, omega)
            config['omega'] = omega
            config['v'] = v
            config['theta'] = theta
            config['t'] = t
            config['r'] = r
            config['g'] = g
            config['e'] = coeff
            duration = t0(r, theta, omega, v, g)
            while not in_equil(g, coeff, theta, t, r, omega, v) and v > 0.01:
                v_in = v - g * duration
                theta_in = (theta + omega * duration) % pi
                v = v_next(e, v_in, omega, r, theta_in)
                omega = omega_next(e, v_in, omega, r, theta_in)
            if not in_equil(g, coeff, theta, t, r, omega, v):  # failed
                answer[0] += 1
            else:
                answer[1] += 1
                print("-----------------------------------------------------------------")
                print("-----------------------------------------------------------------")
                print("-----------------------------------------------------------------")
                print(i)
                print("-----------------------------------------------------------------")
                print("-----------------------------------------------------------------")
                print("-----------------------------------------------------------------")
                print(config, file=f)
    print(answer)
