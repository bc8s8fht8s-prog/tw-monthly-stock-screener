import pandas as pd


def calculate_macd(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["EMA12"] = df["Close"].ewm(span=12, adjust=False).mean()

    df["EMA26"] = df["Close"].ewm(span=26, adjust=False).mean()

    df["DIF"] = df["EMA12"] - df["EMA26"]

    df["MACD"] = df["DIF"].ewm(span=9, adjust=False).mean()

    df["OSC"] = df["DIF"] - df["MACD"]

    return df