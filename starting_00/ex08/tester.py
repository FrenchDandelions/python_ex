from tqdm import tqdm
from time import sleep
from Loading import ft_tqdm
n = int(input())
for elem in tqdm(range(n)):
    sleep(0.05)
for elem in ft_tqdm(range(n)):
    sleep(0.05)
# print(tqdm.__doc__)
