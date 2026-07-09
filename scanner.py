import time

from stock_list import get_stock_list
from data_loader import download_stock_history
from indicators import calculate_macd
from screener import check_strategy


def scan_market(limit=None):
    """
    掃描股票
    limit=None 表示掃描全部股票
    """

    start_time = time.time()

    stocks = get_stock_list()

    if limit:
        stocks = stocks.head(limit)

    results = []

    total = len(stocks)

    for index, row in stocks.iterrows():

        code = row["code"]
        name = row["name"]
        market = row["market"]
        industry = row["industry"]

        progress = f"[{index + 1:4d}/{total}]"

        print(f"{progress} {code} {name} ({market})")

        try:

            # 使用全部歷史月K資料
            df = download_stock_history(
                code,
                market,
            )

            # 計算 MACD
            df = calculate_macd(df)

            # 月K策略
            result = check_strategy(df)

            if result and result["pass"]:

                last_month_close = float(df.iloc[-2]["Close"])

                change_percent = (
                    (result["close"] - last_month_close)
                    / last_month_close
                    * 100
                )

                results.append({
                    "code": code,
                    "name": name,
                    "market": market,
                    "industry": industry,
                    "close": round(result["close"], 2),
                    "high": round(result["high"], 2),
                    "change_percent": round(change_percent, 2),
                    "osc": round(result["osc"], 3),
                })

                print("    ✅ 符合")

            else:

                print("    ❌ 不符合")

        except Exception as e:

            print(f"    ⚠️ {e}")

    # 依股號由小到大排序
    results.sort(
        key=lambda x: int(x["code"]),
    )

    elapsed = time.time() - start_time

    print("\n==============================")
    print("掃描完成")
    print("==============================")
    print(f"掃描股票：{total} 檔")
    print(f"符合條件：{len(results)} 檔")
    print(f"耗時：{elapsed:.1f} 秒")
    print("==============================")

    return {
        "scan_count": total,
        "results": results,
    }