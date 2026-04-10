import pandas as pd

output = []
temp_main_id = ""
temp_name_str = ""

with open("input.txt", "r", encoding="utf-8") as file:
    for row in file:
        row = [i.strip() for i in row.split("\t")]
        if row == ["", ""]:
            # for char in row:
            #     unicode_code_point = ord(char)
            #     print(f"The Unicode code point of '{char}' is {unicode_code_point}")
            #     raise
            temp_main_id = ""
            temp_name_str = ""

        if temp_main_id == "":
            temp_main_id = row[0]
            temp_name_str = row[1]
        else:
            if row[0] == "":
                print(row)
            output.append([min(int(temp_main_id), int(row[0])), max(int(temp_main_id), int(row[0])), f"{temp_name_str};{row[1]}"])

df = pd.DataFrame(output)
df.to_csv("output.csv", index=False, header=False, encoding="utf-8")
df.to_excel("output.xlsx", index=False, header=False)

print("Done!")
