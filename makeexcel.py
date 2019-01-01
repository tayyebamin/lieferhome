import os
import glob
import csv
import io
from xlsxwriter.workbook import Workbook
workbook = Workbook('data.xlsx')
for csvfile in glob.glob(os.path.join('..//data//Late Night Darmstadt Nieder-Ramstädter-Str//', '*.csv')):   
    worksheet = workbook.add_worksheet()
    with io.open(csvfile, 'rt', encoding = "cp1252") as f:
        reader = csv.reader(f)
        print("Adding " + csvfile + " to " + workbook.filename)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
workbook.close() 