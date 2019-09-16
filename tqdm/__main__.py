import tqdm
from six import PY2

for i in tqdm.tqdm(range(10)):
    if PY2:
        print("py2")
