from tqdm import tqdm
from time import sleep

n = int(input())

for elem in tqdm(range(n)):

    sleep(1)
print(tqdm.__doc__)
