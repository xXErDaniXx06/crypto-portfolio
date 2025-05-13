import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from strategy import sma_strategy
from metrics import evaluate_strategy

def load_csv_files(data_folder):
    files = list(Path(data_folder).glob("*.csv"))
    data = {}
    for f in files:
        df = pd.read_csv(f)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)
        data[f.stem] = df
    return data

if __name__ == "__main__":
    print("📥 Cargando datos...")
    data = load_csv_files("data")

    for name, df in data.items():
        print(f"📊 Ejecutando estrategia para {name}")
        df = sma_strategy(df, short_window=10, long_window=50)
        total_return, sharpe = evaluate_strategy(df)
        print(f"✅ {name} - Retorno total: {total_return:.2%}, Sharpe: {sharpe:.2f}")

        df[['close', 'SMA_short', 'SMA_long']].plot(figsize=(14,6), title=name)
        plt.show()
        df['cumulative_returns'].plot(figsize=(14,4), title=f'{name} - Cumulative Returns')
        plt.show()
