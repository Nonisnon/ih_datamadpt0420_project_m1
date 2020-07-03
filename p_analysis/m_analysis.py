import pandas as pd
import re
import numpy as np

def data_grouped(group):
    grouped = group.groupby(['Country', 'Job_Title', 'Age_Group'], as_index=False).count()
    grouped['Percentage'] = grouped['Quantity'].apply(lambda qty: str((qty * 100 / grouped['Quantity'].sum()).round(2))+'%')
    grouped.to_csv(f'/Users/Nonis/desktop/ih_datamadpt0420_project_m1/data/results/data_grouped.csv', index=False)
    return grouped

