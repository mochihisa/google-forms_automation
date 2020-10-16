from main_CUI import *


def main():

    filename = file_read()
    data = get_data(filename)
    late, temperature, condition, submission, error = get_info(data)
    late, temperature, condition, submission, error = sort(late), sort(
        temperature), sort(condition), submission, sort(error)

    res = [['遅れ'], ['提出時刻', '名列番号', '体温', '体調不良の有無', '詳細']] + late + [[]] +\
        [['体温'], ['提出時刻', '名列番号', '体温', '体調不良の有無', '詳細']] + temperature + [[]] + \
        [['体調'], ['提出時刻', '名列番号', '体温', '体調不良の有無', '詳細']] + condition + [[]] + \
        [['未提出'], ['名列番号']] + [[s] for s in submission] + [[]] +\
        [['名簿に存在しない人'], ['提出時刻', '名列番号', '体温', '体調不良の有無', '詳細']] + error
    # pprint(res)
    file_write(res)


if __name__ == "__main__":
    main()
