import pandas as pd
import twstock


def get_stock_list():

    rows = []

    for info in twstock.codes.values():

        # 只保留普通股
        if info.type != "股票":
            continue

        # 只保留上市、上櫃
        if info.market not in ["上市", "上櫃"]:
            continue

        rows.append({
            "code": info.code,
            "name": info.name,
            "market": info.market,
            "industry": info.group
        })

    df = pd.DataFrame(rows)

    df = df.sort_values("code").reset_index(drop=True)

    return df