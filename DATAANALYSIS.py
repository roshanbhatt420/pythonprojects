import csv as file
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
with open('earthquake_data_nepal.csv') as f:
    reader = file.reader(f)
    data = list(reader)
    data = np.array(data)
    print(data)
