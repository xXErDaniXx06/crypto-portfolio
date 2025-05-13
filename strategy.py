def sma_strategy(df, short_window=10, long_window=50):
    df['SMA_short'] = df['close'].rolling(window=short_window).mean()
    df['SMA_long'] = df['close'].rolling(window=long_window).mean()
    df['signal'] = 0
    df.loc[df['SMA_short'] > df['SMA_long'], 'signal'] = 1
    df.loc[df['SMA_short'] < df['SMA_long'], 'signal'] = -1
    df['position'] = df['signal'].shift(1).fillna(0)
    df['strategy_returns'] = df['position'] * df['close'].pct_change()
    df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()
    return df
