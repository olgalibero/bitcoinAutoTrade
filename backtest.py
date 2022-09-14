import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-BTC", count=730)
df['range'] = (df['high'] - df['low']) * 0.6
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.001
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")