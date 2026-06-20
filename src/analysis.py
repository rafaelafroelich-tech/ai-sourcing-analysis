
import pandas as pd
df=pd.read_excel('data/mock_sourcing_dataset.xlsx')
print(df.groupby('source_channel')['hired'].mean())
