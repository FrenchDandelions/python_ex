import shutil
from time import sleep


def getBar(totalsize, sizeperc, sizetime):
    return ""

def getTimeFormated(time):
    return time

def ft_tqdm(lst: range) -> None:
    size_terminal = shutil.get_terminal_size().columns
    size_iterable = len(lst)
    for index in range(len(lst)):
        num = round(((index+1)/size_iterable) * 100)
        perc = (str(num) + "%").rjust(4)
        
        print(f'\r{perc}{index}', end="")
        yield lst[index]

for i in ft_tqdm(range(50)):
    sleep(0.1)
print("HERE MATE", range(50)[-1])
print(len("100%|"), len("| 12/12 [00:06<00:00,  2.00it/s]"))