import xlrd
import sys
import pandas as pd
import datetime
from pprint import pprint, pformat


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
    if data[1] >= 2100 and data[1] <= 2105:
        return True
    else:
        return False


def get_info(data_list):
    late = []
    temperature = []
    condition = []
    submission = list(range(2101, 2106))

    for data in data_list:
        if get_late(data):
            late.append(data)
        if get_temperature(data):
            temperature.append(data)
        if get_condition(data):
            condition.append(data)
        if get_submission(data):
            submission.remove(data[1])

    return late, temperature, condition, submission


def help():
    print("""\
usage: python3 main-CUI.py [filename]
       main-CUI.exe [filename]

if first argument is "help": show helps

filename: indispensable\
""")


def main():
    args = sys.argv
    filename = args[1]

    if args[1] == 'help':
        help()

    else:
        data = get_data(filename)
        late, temperature, condition, submission = get_info(data)
        print(
            f'raw=\n{pformat(data)}\n\n'
            f'late=\n{pformat(late)}\n\n'
            f'temperature=\n{pformat(temperature)}\n\n'
            f'condition=\n{pformat(condition)}\n\n'
            f'submission=\n{pformat(submission)}'
        )


if __name__ == "__main__":
    main()
