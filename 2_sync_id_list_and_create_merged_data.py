import csv
from datetime import datetime

INPUT = "id_list_with_name_for_check.csv"
ID_LIST_OUTPUT = "id_list.txt"
MERGED_CSV_OUTPUT = "MERGED_PERSON_DATA.csv"

# Column layout of id_list_with_name_for_check.csv (UTF-8 BOM, comma-separated, with header):
#   0: c_personid           (kept person)
#   1: name_A
#   2: c_merged_from_personid (merged-from person)
#   3: name_B
#   4: need_check
#   5: source
#   6: notes

MERGED_HEADER = [
    "c_personid",
    "c_merged_from_personid",
    "c_notes",
    "c_source",
    "c_pages",
    "c_created_by",
    "c_modified_by",
    "c_created_date",
    "c_modified_date",
]


def read_rows(path):
    rows = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            if not row or all(not c.strip() for c in row):
                continue
            rows.append(row)
    return rows


def write_id_list(rows, path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        for row in rows:
            writer.writerow([row[0], row[2], row[5], row[6]])


def write_merged_person_data(rows, path):
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(MERGED_HEADER)
        for row in rows:
            source = row[5].strip()
            c_source = source if source and source != "None" else ""
            writer.writerow([
                row[0],
                row[2],
                row[6],
                c_source,
                "",
                "load",
                "",
                today,
                "",
            ])


def main():
    rows = read_rows(INPUT)
    write_id_list(rows, ID_LIST_OUTPUT)
    write_merged_person_data(rows, MERGED_CSV_OUTPUT)
    print(f"Synced {ID_LIST_OUTPUT} and wrote {MERGED_CSV_OUTPUT} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
