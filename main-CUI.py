import xlrd
import sys


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


def help():
    print("""\
usage: python3 main-CUI.py [filename] [sheet_namep]
       main-CUI.exe [filename] [sheet_name]

if first argument is "help": show helps

filename: indispensable
sheet_name: default value is sheet[0]\
""")


def main():
    args = sys.argv
    filename = args[1]
    sheet = args[2] if len(args) >= 3 else ""
    if args[1] == 'help':
        help()
    else:
        get_data(filename, sheet)


if __name__ == "__main__":
    main()
