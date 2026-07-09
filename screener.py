import pandas as pd


def check_strategy(df: pd.DataFrame):

    # 至少需要 35 根月K，避免 MACD 因歷史資料不足而不穩定
    if len(df) < 35:
        return None

    this_month = df.iloc[-1]
    last_month = df.iloc[-2]

    close_this_month = float(this_month["Close"])
    high_last_month = float(last_month["High"])

    osc_this_month = float(this_month["OSC"])
    osc_last_month = float(last_month["OSC"])

    # 條件一：本月收盤 > 上月最高（含上影線）
    condition1 = close_this_month > high_last_month

    # 條件二：本月 OSC > 上月 OSC（嚴格大於）
    condition2 = osc_this_month > osc_last_month

    return {
        "close": close_this_month,
        "high": high_last_month,
        "osc": osc_this_month,
        "osc_prev": osc_last_month,
        "condition1": condition1,
        "condition2": condition2,
        "pass": condition1 and condition2,
    }