import sys
import pandas as pd

print(sys.argv)

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

print(df)

print("Pipeline script executed successfully.")

