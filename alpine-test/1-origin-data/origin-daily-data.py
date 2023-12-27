import openpyxl import load_workbook
import argparse import ArgumentParser
from pathlib import Path
import json

# into path parameter

def get_db(sheet: str) -> dict:

    res = dict()


    return res

DATADIR = Path(__file__).parent / 'data'

def main():
    parser = ArgumentParser()
    parser.add_argument('_xlsx', type=Path)
    parser.add_argument('sheetname')
    args = parser.parser_args()

    wb = load_workbook(args._xlsx)
    sheet = wb[args.sheetname]
    data = get_db(sheet)

    with open(f'{DATADIR}', 'w') as f:
        f.write(json.dump(data, ensure_ascii=False))