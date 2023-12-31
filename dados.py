import pandas as pd
import numpy as np

dict_data = {'Data':np.array(pd.date_range(start='1/1/2023', periods=365, freq='D', )).tolist(),
             'Pgmto':np.array(np.random.randint(100, 500, size=365)).tolist()}

df = pd.DataFrame.from_dict(dict_data)
df['Data'] = pd.to_datetime(df['Data'])
df['EmpresaID'] = [np.random.randint(1,10) for i in df['Data']]

faturamento = df.set_index('Data').groupby(pd.Grouper(freq='M'))['Pgmto'].sum()

topBuyers = df.groupby('EmpresaID')['Data'].count().reset_index(drop=False).sort_values(by='Data', ascending=False)

