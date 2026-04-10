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
    # Extract reason from column 0
    reason = input_original_pd[0][i] if pd.notna(input_original_pd[0][i]) else ""
    
    # Process ID columns starting from index 3 to compare with column 2 (column 0 is reason, column 1 is empty, column 2 is first ID)
    for j in range(3, len(input_original_pd.columns)):
        try:
            id_source_list = re.sub(r"[）\)]", "", input_original_pd[j][i])
            id_source_list = re.sub(r"（", "(", id_source_list)
            id_source_list = id_source_list.split("(")
            input_original_pd.loc[i, j] = id_source_list[0]
        except TypeError:
            continue
        try:
            # Column 2 is now the first ID column
            if is_int(input_original_pd[2][i]):
                input_original_pd.loc[i, 2] = int(input_original_pd[2][i])
            if is_int(input_original_pd[j][i]):
                input_original_pd.loc[i, j] = int(input_original_pd[j][i])
            else:
                continue
            if not math.isnan(input_original_pd[2][i]) and not math.isnan(
                input_original_pd[j][i]
            ):
                element_pair_list.append(
                    [input_original_pd[2][i], int(input_original_pd[j][i])]
                )
                if len(id_source_list) > 1:
                    source_list.append(id_source_list[1])
                else:
                    source_list.append("None")
                reason_list.append(reason)
        except TypeError:
            print(i)
            print(j)
            print(math.isnan(input_original_pd[2][i]))
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

output_pd = pd.DataFrame(element_pair_list)
output_pd.to_csv("id_list.txt", sep="\t", header=None, index=False)

print("Create pair list done!")

# add source to the pair list output

read_name_api_url = "https://input.cbdb.fas.harvard.edu/basicinformation/"
counter = 0
max_counter = len(element_pair_list)
for row in element_pair_list:
    counter += 1
    need_check_token = ""
    # print(
    #     f"{counter/max_counter*100:.2f}% finished. Now working on: {row[0]}, {row[1]}"
    # )
    person_a_name = ""
    person_b_name = ""
    # person_a_query_url = read_name_api_url + str(row[0])
    # person_b_query_url = read_name_api_url + str(row[1])
    # person_a_query = requests.get(person_a_query_url)
    # person_b_query = requests.get(person_b_query_url)
    # if person_a_query.status_code == 200:
    #     person_a_query_json = person_a_query.json()
    #     if "c_name_chn" in person_a_query_json:
    #         person_a_name = person_a_query_json["c_name_chn"]
    #     else:
    #         person_a_name = "None"
    # else:
    #     person_a_name = "None"
    # if person_b_query.status_code == 200:
    #     person_b_query_json = person_b_query.json()
    #     if "c_name_chn" in person_b_query_json:
    #         person_b_name = person_b_query_json["c_name_chn"]
    #     else:
    #         person_b_name = "None"
    # if person_a_name != person_b_name:
    #     need_check_token = "need_check"
    element_pair_with_name_list.append(
        [row[0], person_a_name, row[1], person_b_name, need_check_token, row[2], row[3]]
    )

output_pd = pd.DataFrame(element_pair_with_name_list)
output_pd.to_csv("id_list_with_name_for_check.txt", sep="\t", header=None, index=False)
print("Create pair list with name done!")

print("All done!")
