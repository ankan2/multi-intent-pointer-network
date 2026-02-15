import pandas as pd
import random
import sys

dataset = sys.argv[1]
df = pd.read_csv(dataset)
df = df.sample(frac=1, random_state=random.seed())
df.to_csv(dataset, index = False)