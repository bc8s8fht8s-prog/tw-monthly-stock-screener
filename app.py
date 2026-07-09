from exporter import save_result
from scanner import scan_market

from config import TEST_MODE, TEST_LIMIT


def main():

    if TEST_MODE:
        scan_data = scan_market(limit=TEST_LIMIT)
    else:
        scan_data = scan_market()

    save_result(
        scan_data["results"],
        scan_data["scan_count"]
    )


if __name__ == "__main__":
    main()