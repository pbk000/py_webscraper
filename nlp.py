import sys
import numpy as np
import pandas as pd

csv = sys.argv[1]
nlp_df = pd.read_csv(csv)

print("DO RAD NLP THINGS HERE")
print(nlp_df.head())