import xlrd
import sys
import pandas as pd
import datetime
from pprint import pprint, pformat
import tkinter.filedialog
import os


"""
何を思ったのかxlsxで開発してた
csvつかうからこの部分いらんけど将来の拡張性のためにコメントアウトにしとく
def get_data(filename, sheet):
    wb = xlrd.open_workbook(filename)
    sheets = wb.sheet_names()
    if sheet == "":
        sheet = wb.sheet_by_name(sheets[0])
    else:
        if not sheet in sheets:
            print(f"{sheet} : sheet not found")
            print(f"You can select from {','.join(sheets)}")
            exit()
        else:
            sheet = wb.sheet_by_name(sheet)
    columns = sheet.ncols
    lines = sheet.nrows
    data = [sheet.row_values(x) for x in range(lines)]
    print(f'{sheets=}\n{columns=}\n{lines=}\n{data=}')
"""


def get_data(filename):
    res = pd.read_csv(filename).values.tolist()
    return res


def get_late(data):
    s = [s for s in data[0].split()]
    if s[2] == '午後':
        return True
    time = [int(i) for i in s[1].split(':')]
    time = datetime.time(time[0], time[1], time[2])
    if time > datetime.time(8, 0, 0):
        return True
    else:
        return False


def get_temperature(data):
    if data[2] >= 37.0:
        return True
    else:
        return False


def get_condition(data):
    if data[3] == 'あり':
        return True
    else:
        return False


def get_submission(data):
    if data[1] >= 2101 and data[1] <= 2140\
            or data[1] >= 2201 and data[1] <= 2240\
            or data[1] >= 2301 and data[1] <= 2340\
            or data[1] >= 2401 and data[1] <= 2440:
        return True
    else:
        return False


def get_info(data_list):
    late = []
    temperature = []
    condition = []
    submission = list(range(2101, 2141)) + list(range(2201, 2241)) + \
        list(range(2301, 2341)) + list(range(2401, 2441))
    error = []

    for data in data_list:
        if get_submission(data):
            if data[1] in submission:
                submission.remove(data[1])
                if get_late(data):
                    late.append(data)
                if get_temperature(data):
                    temperature.append(data)
                if get_condition(data):
                    condition.append(data)
        else:
            error.append(data)

    return late, temperature, condition, submission, error


def sort(data_list):
    res = sorted(data_list, key=lambda x: x[1])
    return res


def help():
    print("""\
usage: python3 main_CUI.py [filename]
       main_CUI.exe [filename]

if first argument is "help": show help\
""")


def file_read():

    fTyp = [("csv", "*.csv")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file_path = tkinter.filedialog.askopenfilename(
        filetypes=fTyp, initialdir=iDir)
    if len(file_path) != 0:
        dir = [s for s in file_path.split('/')]
        dir.pop(-1)
        dir = '/'.join(dir)
        return file_path, dir
    else:
        exit()


def file_write(data_list, dir='.'):
    dt_now = datetime.datetime.now()
    date = dt_now.date()
    df = pd.DataFrame(data_list)
    df.to_csv(f'{dir}/{date}.csv', index=False,
              header=False, sep=',', encoding='utf-8')


def main():
    args = sys.argv
    filename = args[1]

    if args[1] == 'help':
        help()

    else:
        data = get_data(filename)
        late, temperature, condition, submission, error = get_info(data)
        late, temperature, condition, submission, error = sort(late), sort(
            temperature), sort(condition), submission, sort(error)
        print(
            f'遅れ\n{pformat(late)}\n\n'
            f'体温\n{pformat(temperature)}\n\n'
            f'体調\n{pformat(condition)}\n\n'
            f'未提出\n{submission}\n\n'
            f'名簿に存在しない人\n{pformat(error)}'
        )


if __name__ == "__main__":
    main()
