import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo


def save_result(results, scan_count):

    os.makedirs("docs/data", exist_ok=True)

    output = {
        "update_time": datetime.now(
            ZoneInfo("Asia/Taipei")
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "scan_count": scan_count,
        "count": len(results),
        "stocks": results
    }

    with open(
        "docs/data/result.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            output,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("✅ 已輸出 docs/data/result.json")