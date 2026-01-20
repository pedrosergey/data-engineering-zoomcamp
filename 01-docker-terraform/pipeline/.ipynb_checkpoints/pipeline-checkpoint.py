import sys
import pandas as pd

print(sys.argv)

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

print(df)

# df.to_parquet('../external/output.parquet')

df.to_parquet('../external/output.parquet')

print(f"Pipeline script executed successfully. Arguments: {sys.argv}")

