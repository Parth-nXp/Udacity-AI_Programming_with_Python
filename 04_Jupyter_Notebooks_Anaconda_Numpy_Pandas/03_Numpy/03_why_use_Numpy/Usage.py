import numpy as np
import time

x = np.random.random(10000000)

start = time.time()
sum(x)/len(x)
print(time.time()-start)

start = time.time()
np.mean(x)
print(time.time()-start)