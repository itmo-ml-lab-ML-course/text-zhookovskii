from typing import List
from random import shuffle
import csv


def read_lines(filename: str) -> List[str]:
    f = open(filename, 'r', encoding='UTF-8')
    lines = f.readlines()
    f.close()
    return lines


prigov = read_lines('data/prigov_format.txt')
rizhiy = read_lines('data/rizhiy_format.txt')

prigov_lines = [["Дмитрий Пригов", l.strip()] for l in prigov]
rizhiy_lines = [["Борис Рыжий", l.strip()] for l in rizhiy]

rows = prigov_lines + rizhiy_lines
print(len(rows))
shuffle(rows)
print(len(rows))

with open('data/poems.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(
        ["Author", "Line"]
    )
    writer.writerows(rows)


