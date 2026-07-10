import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo


def save_result(results, scan_count):
    """
    同時輸出：
    1. data/result.json（GitHub Pages 使用）
    2. docs/data/result.json（備份）
    """

    output = {
        "update_time": datetime.now(
            ZoneInfo("Asia/Taipei")
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "scan_count": scan_count,
        "count": len(results),
        "stocks": results
    }

    # 建立資料夾
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs/data", exist_ok=True)

    # 同時輸出兩份
    output_paths = [
        "data/result.json",
        "docs/data/result.json"
    ]

    for path in output_paths:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                output,
                f,
                ensure_ascii=False,
                indent=4
            )

    print("✅ 已輸出 data/result.json")
    print("✅ 已輸出 docs/data/result.json")