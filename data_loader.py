import yfinance as yf
import pandas as pd
from logger import log


def download_stock_history(
    stock_id: str,
    market: str,
    period: str = "max",
    interval: str = "1mo",
) -> pd.DataFrame:
    """
    下載股票歷史資料

    預設：
        period = "max"
        interval = "1mo"

    上市：2330.TW
    上櫃：5483.TWO
    """

    if market == "上市":
        symbol = f"{stock_id}.TW"
    elif market == "上櫃":
        symbol = f"{stock_id}.TWO"
    else:
        raise Exception(f"未知市場：{market}")

    log(f"下載 {symbol} ({interval})")

    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        auto_adjust=False,
        progress=False,
    )

    if df.empty:
        raise Exception(f"{stock_id} ({market}) 無資料")

    df.reset_index(inplace=True)

    # yfinance 新版可能回傳 MultiIndex 欄位
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]

    return df