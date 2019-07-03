import numpy as np
import pandas as pd

from pyxlsb import open_workbook as open_xlsb
df = []

with open_xlsb('AVS Dashboard - 2019.xlsb') as wb:
    with wb.get_sheet("Raw Data") as sheet:
        for row in sheet.rows():
            df.append([item.v for item in row])

df1 = pd.DataFrame(df[1:], columns=df[0])


    


