import numpy as np

def evaluate_strategy(df):
    total_return = df['cumulative_returns'].iloc[-1] - 1
    sharpe = df['strategy_returns'].mean() / df['strategy_returns'].std() * np.sqrt(252)
    return total_return, sharpe
