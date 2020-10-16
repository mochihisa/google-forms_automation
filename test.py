import pandas as pd
import random
import numpy as np


def file_write(data_list):
    df = pd.DataFrame(data_list)
    df.to_csv(f'sample.csv', index=False,
              header=['タイムスタンプ', '名簿', '体温', '風邪症状', '具体的に'], sep=',', encoding='utf-8')


res = []
for s in random.sample(list(range(2101, 2141)), k=40):
    date = f'2020/10/16 {random.randint(3,8)}:{random.randint(00,59)}:{random.randint(00,59)} 午前 GMT+9'
    temperature = random.uniform(34.0, 37.5)
    condition = np.random.choice(['あり', 'なし'], p=[0.1, 0.9])
    res = res + [[date, s, f'{temperature:.1f}', condition, None]]
    print(res)
for s in random.sample(list(range(2201, 2241)), k=40):
    date = f'2020/10/16 {random.randint(3,8)}:{random.randint(00,59)}:{random.randint(00,59)} 午前 GMT+9'
    temperature = random.uniform(34.0, 37.5)
    condition = np.random.choice(['あり', 'なし'], p=[0.1, 0.9])
    res = res + [[date, s, f'{temperature:.1f}', condition, None]]
    print(res)
for s in random.sample(list(range(2301, 2341)), k=40):
    date = f'2020/10/16 {random.randint(3,8)}:{random.randint(00,59)}:{random.randint(00,59)} 午前 GMT+9'
    temperature = random.uniform(34.0, 37.5)
    condition = np.random.choice(['あり', 'なし'], p=[0.1, 0.9])
    res = res + [[date, s, f'{temperature:.1f}', condition, None]]
    print(res)
for s in random.sample(list(range(2401, 2441)), k=40):
    date = f'2020/10/16 {random.randint(3,8)}:{random.randint(00,59)}:{random.randint(00,59)} 午前 GMT+9'
    temperature = random.uniform(34.0, 37.5)
    condition = np.random.choice(['あり', 'なし'], p=[0.1, 0.9])
    res = res + [[date, s, f'{temperature:.1f}', condition, None]]
    print(res)
file_write(res)
