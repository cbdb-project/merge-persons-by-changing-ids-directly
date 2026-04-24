import pandas as pd
import math
import requests
import re


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


input_original_pd = pd.read_csv("input_original.txt", sep="\t", header=None, dtype=str)
input_original_pd = input_original_pd.apply(
    lambda x: x.str.strip() if x.dtype == "object" else x
)
print(input_original_pd.head())

element_pair_list = []
source_list = []
reason_list = []
element_pair_with_name_list = []
for i in range(len(input_original_pd)):
    # After pandas parses: col 0 is contributor, col 1 is date, col 2 is reason,
    # col 3 is empty separator, col 4 is first ID, col 5+ are additional IDs.
    reason = input_original_pd[2][i] if pd.notna(input_original_pd[2][i]) else ""
    reason = reason.replace("\r\n", "\\n").replace("\r", "\\n").replace("\n", "\\n")

    # Pair column 4 (first ID) with each subsequent ID column.
    for j in range(5, len(input_original_pd.columns)):
        try:
            id_source_list = re.sub(r"[）\)]", "", input_original_pd[j][i])
            id_source_list = re.sub(r"（", "(", id_source_list)
            id_source_list = id_source_list.split("(")
            input_original_pd.loc[i, j] = id_source_list[0]
        except TypeError:
            continue
        try:
            if is_int(input_original_pd[4][i]):
                input_original_pd.loc[i, 4] = int(input_original_pd[4][i])
            if is_int(input_original_pd[j][i]):
                input_original_pd.loc[i, j] = int(input_original_pd[j][i])
            else:
                continue
            if not math.isnan(input_original_pd[4][i]) and not math.isnan(
                input_original_pd[j][i]
            ):
                element_pair_list.append(
                    [input_original_pd[4][i], int(input_original_pd[j][i])]
                )
                if len(id_source_list) > 1:
                    source_list.append(id_source_list[1])
                else:
                    source_list.append("None")
                reason_list.append(reason)
        except TypeError:
            print(i)
            print(j)
            print(math.isnan(input_original_pd[4][i]))
            print("here")
            print(input_original_pd[j][i])
            print(type(input_original_pd[j][i]))
            print(math.isnan(input_original_pd[j][i]))
            raise
print(f"source_list: {source_list}")
# add each element in source_list and reason to the end of each list in element_pair_list
for i in range(len(element_pair_list)):
    element_pair_list[i].append(source_list[i])
    element_pair_list[i].append(reason_list[i])

# Append pairs from PKB projects duplicates (reason = "by PKB")
pkb_csv_path = "create_pairs_for_pkb_projects_duplicates/output.csv"
pkb_pd = pd.read_csv(pkb_csv_path, header=None, dtype=str)
for i in range(len(pkb_pd)):
    id_a = int(pkb_pd[0][i])
    id_b = int(pkb_pd[1][i])
    element_pair_list.append([id_a, id_b, "None", "by PKB"])

output_pd = pd.DataFrame(element_pair_list)
output_pd.to_csv("id_list.txt", sep="\t", header=None, index=False)

print("Create pair list done!")

# add source to the pair list output

read_name_api_url = "https://input.cbdb.fas.harvard.edu/cbdbapi/person.php?o=json&id="


def fetch_ch_name(person_id):
    resp = requests.get(read_name_api_url + str(person_id))
    if resp.status_code != 200:
        return "None"
    try:
        data = resp.json()
    except ValueError:
        return "None"
    try:
        return data["Package"]["PersonAuthority"]["PersonInfo"]["Person"]["BasicInfo"]["ChName"] or "None"
    except (KeyError, TypeError):
        return "None"


counter = 0
max_counter = len(element_pair_list)
for row in element_pair_list:
    counter += 1
    need_check_token = ""
    print(
        f"{counter/max_counter*100:.2f}% finished. Now working on: {row[0]}, {row[1]}"
    )
    person_a_name = fetch_ch_name(row[0])
    person_b_name = fetch_ch_name(row[1])
    if person_a_name != person_b_name:
        need_check_token = "need_check"
    element_pair_with_name_list.append(
        [row[0], person_a_name, row[1], person_b_name, need_check_token, row[2], row[3]]
    )

output_pd = pd.DataFrame(
    element_pair_with_name_list,
    columns=["c_personid", "name_A", "c_merged_from_personid", "name_B", "need_check", "source", "notes"],
)
output_pd.to_csv("id_list_with_name_for_check.csv", index=False, encoding="utf-8-sig")
print("Create pair list with name done!")

print("All done!")
