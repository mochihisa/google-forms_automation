import tkinter.filedialog
import os
from main_CUI import *


def file_read():

    fTyp = [("csv", "*.csv")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file_path = tkinter.filedialog.askopenfilename(
        filetypes=fTyp, initialdir=iDir)
    if len(file_path) != 0:
        return file_path
    else:
        exit()


def file_write(data_list):
    dt_now = datetime.datetime.now()
    date = dt_now.date()
    df = pd.DataFrame(data_list)
    df.to_csv(f'{date}.csv', index=False,
              header=False, sep=',', encoding='utf-8')


def main():

    filename = file_read()
    data = get_data(filename)
    late, temperature, condition, submission, error = get_info(data)

    res = [['遅れ'], ['提出時刻', '名列番号', '体温', '体調不良の有無', '詳細']] + late + [[]] +\
        [['体温'], ['提出時刻', '名列番号', '体温', '体調不良の有無', '詳細']] + temperature + [[]] + \
        [['体調'], ['提出時刻', '名列番号', '体温', '体調不良の有無', '詳細']] + condition + [[]] + \
        [['未提出'], ['名列番号']] + [[s] for s in submission] + [[]] +\
        [['名簿に存在しない人'], ['提出時刻', '名列番号', '体温', '体調不良の有無', '詳細']] + error
    # pprint(res)
    file_write(res)


if __name__ == "__main__":
    main()
