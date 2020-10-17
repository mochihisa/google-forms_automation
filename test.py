import pandas as pd
import random
import numpy as np


def file_write(data_list):
    df = pd.DataFrame(data_list)
    df.to_csv(f'sample.csv', index=False,
              header=['タイムスタンプ', '名簿', '体温', '風邪症状', '具体的に'], sep=',', encoding='utf-8')


res = []
for s in random.sample(list(range(2101, 2141)), k=random.choice(list(range(35,41)))) + \
        random.sample(list(range(2201, 2241)), k=random.choice(list(range(35,41)))) + \
        random.sample(list(range(2301, 2341)), k=random.choice(list(range(35,41)))) + \
        random.sample(list(range(2401, 2441)), k=random.choice(list(range(35,41)))):
    h = np.random.choice([int(i) for i in np.random.choice([str(list(range(5,8))),str([8])],p=[0.95,0.05]).strip('[').strip(']').split(', ')])
    date = f'2020/10/16 {h}:{random.randint(00,59)}:{random.randint(00,59)} 午前 GMT+9'
    temperature = random.choice([float(f) for f in np.random.choice([str([round(i, 1) for i in np.arange(36, 37, 0.1)]), str([round(i, 1) for i in np.arange(37, 39, 0.1)])], p=[0.95, 0.05]).strip('[').strip(']').split(', ')])
    condition = np.random.choice(['あり', 'なし'], p=[0.05, 0.95])
    res = res + [[date, s, f'{temperature:.1f}', condition, None]]
    print(res)
file_write(res)
