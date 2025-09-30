import csv

# Because of foreign key constraint, you can't update c_personid in BIOG_MAIN
update_sql_list = []
ALTNAME_DATA = "UPDATE IGNORE ALTNAME_DATA SET c_personid = %s WHERE c_personid = %s;"
ASSOC_DATA_1 = "UPDATE IGNORE ASSOC_DATA SET c_personid = %s WHERE c_personid = %s;"
ASSOC_DATA_2 = "UPDATE IGNORE ASSOC_DATA SET c_kin_id = %s WHERE c_kin_id = %s;"
ASSOC_DATA_3 = "UPDATE IGNORE ASSOC_DATA SET c_assoc_id = %s WHERE c_assoc_id = %s;"
ASSOC_DATA_4 = (
    "UPDATE IGNORE ASSOC_DATA SET c_assoc_kin_id = %s WHERE c_assoc_kin_id = %s;"
)
BIOG_ADDR_DATA = (
    "UPDATE IGNORE BIOG_ADDR_DATA SET c_personid = %s WHERE c_personid = %s;"
)
BIOG_INST_DATA = (
    "UPDATE IGNORE BIOG_INST_DATA SET c_personid = %s WHERE c_personid = %s;"
)
BIOG_SOURCE_DATA = (
    "UPDATE IGNORE BIOG_SOURCE_DATA SET c_personid = %s WHERE c_personid = %s;"
)
ENTRY_DATA = "UPDATE IGNORE ENTRY_DATA SET c_personid = %s WHERE c_personid = %s;"
KIN_DATA_1 = "UPDATE IGNORE KIN_DATA SET c_personid = %s WHERE c_personid = %s;"
KIN_DATA_2 = "UPDATE IGNORE KIN_DATA SET c_kin_id = %s WHERE c_kin_id = %s;"
POSTED_TO_ADDR_DATA = (
    "UPDATE IGNORE POSTED_TO_ADDR_DATA SET c_personid = %s WHERE c_personid = %s;"
)
POSTED_TO_ADDR_DATA_FOR_SOURCE_UPDATE = "UPDATE IGNORE POSTED_TO_ADDR_DATA INNER JOIN POSTED_TO_OFFICE_DATA ON POSTED_TO_ADDR_DATA.c_posting_id = POSTED_TO_OFFICE_DATA.c_posting_id SET POSTED_TO_ADDR_DATA.c_personid = %s WHERE POSTED_TO_OFFICE_DATA.c_personid = %s AND POSTED_TO_OFFICE_DATA.c_source = %s;"
POSTED_TO_OFFICE_DATA = (
    "UPDATE IGNORE POSTED_TO_OFFICE_DATA SET c_personid = %s WHERE c_personid = %s;"
)
POSTING_DATA = "UPDATE IGNORE POSTING_DATA SET c_personid = %s WHERE c_personid = %s;"
POSTING_DATA_FOR_SOURCE_UPDATE = "UPDATE IGNORE POSTING_DATA INNER JOIN POSTED_TO_OFFICE_DATA ON POSTING_DATA.c_posting_id = POSTED_TO_OFFICE_DATA.c_posting_id SET POSTING_DATA.c_personid = %s WHERE POSTED_TO_OFFICE_DATA.c_personid = %s AND POSTED_TO_OFFICE_DATA.c_source = %s;"
STATUS_DATA = "UPDATE IGNORE STATUS_DATA SET c_personid = %s WHERE c_personid = %s;"
TEXT_DATA = "UPDATE IGNORE BIOG_TEXT_DATA SET c_personid = %s WHERE c_personid = %s;"
EVENTS_DATA = "UPDATE IGNORE EVENTS_DATA SET c_personid = %s WHERE c_personid = %s;"
POSSESSION_DATA = "UPDATE IGNORE POSSESSION_DATA SET c_personid = %s WHERE c_personid = %s;"
# DATABASE_LINK_DATA intentionally excluded --
# this table maintains external database references and should preserve
# original IDs to ensure cross-platform data integrity and audit trails
# BIOG_MAIN = "UPDATE IGNORE BIOG_MAIN SET c_personid = %s WHERE c_personid = %s;"
update_sql_list = [
    ALTNAME_DATA,
    ASSOC_DATA_1,
    ASSOC_DATA_2,
    ASSOC_DATA_3,
    ASSOC_DATA_4,
    BIOG_ADDR_DATA,
    BIOG_INST_DATA,
    BIOG_SOURCE_DATA,
    ENTRY_DATA,
    KIN_DATA_1,
    KIN_DATA_2,
    POSTED_TO_ADDR_DATA,
    POSTING_DATA,
    POSTED_TO_OFFICE_DATA,
    STATUS_DATA,
    TEXT_DATA,
    EVENTS_DATA,
    POSSESSION_DATA,
    # DATABASE_LINK_DATA excluded - see comment above
]

# biog_main must be placed at the end of this list
delete_sql_list = []
ALTNAME_DATA = "DELETE FROM ALTNAME_DATA WHERE c_personid = %s;"
ASSOC_DATA_1 = "DELETE FROM ASSOC_DATA WHERE c_personid = %s;"
ASSOC_DATA_2 = "DELETE FROM ASSOC_DATA WHERE c_kin_id = %s;"
ASSOC_DATA_3 = "DELETE FROM ASSOC_DATA WHERE c_assoc_id = %s;"
ASSOC_DATA_4 = "DELETE FROM ASSOC_DATA WHERE c_assoc_kin_id = %s;"
BIOG_ADDR_DATA = "DELETE FROM BIOG_ADDR_DATA WHERE c_personid = %s;"
BIOG_INST_DATA = "DELETE FROM BIOG_INST_DATA WHERE c_personid = %s;"
BIOG_SOURCE_DATA = "DELETE FROM BIOG_SOURCE_DATA WHERE c_personid = %s;"
ENTRY_DATA = "DELETE FROM ENTRY_DATA WHERE c_personid = %s;"
KIN_DATA_1 = "DELETE FROM KIN_DATA WHERE c_personid = %s;"
KIN_DATA_2 = "DELETE FROM KIN_DATA WHERE c_kin_id = %s;"
POSTED_TO_ADDR_DATA = "DELETE FROM POSTED_TO_ADDR_DATA WHERE c_personid = %s;"
POSTED_TO_ADDR_DATA_FOR_SOURCE_DELTE = "DELETE POSTED_TO_ADDR_DATA FROM POSTED_TO_ADDR_DATA INNER JOIN POSTED_TO_OFFICE_DATA ON POSTED_TO_ADDR_DATA.c_posting_id = POSTED_TO_OFFICE_DATA.c_posting_id WHERE POSTED_TO_OFFICE_DATA.c_personid = %s AND POSTED_TO_OFFICE_DATA.c_source = %s;"
POSTED_TO_OFFICE_DATA = "DELETE FROM POSTED_TO_OFFICE_DATA WHERE c_personid = %s;"
POSTING_DATA = "DELETE FROM POSTING_DATA WHERE c_personid = %s;"
POSTING_DATA_FOR_SOURCE_DELTE = "DELETE POSTING_DATA FROM POSTING_DATA INNER JOIN POSTED_TO_OFFICE_DATA ON POSTING_DATA.c_posting_id = POSTED_TO_OFFICE_DATA.c_posting_id WHERE POSTED_TO_OFFICE_DATA.c_personid = %s AND POSTED_TO_OFFICE_DATA.c_source = %s;"
STATUS_DATA = "DELETE FROM STATUS_DATA WHERE c_personid = %s;"
TEXT_DATA = "DELETE FROM BIOG_TEXT_DATA WHERE c_personid = %s;"
EVENTS_DATA = "DELETE FROM EVENTS_DATA WHERE c_personid = %s;"
POSSESSION_DATA = "DELETE FROM POSSESSION_DATA WHERE c_personid = %s;"
# DATABASE_LINK_DATA intentionally excluded - see comment above
BIOG_MAIN = "DELETE FROM BIOG_MAIN WHERE c_personid = %s;"
delete_sql_list = [
    ALTNAME_DATA,
    ASSOC_DATA_1,
    ASSOC_DATA_2,
    ASSOC_DATA_3,
    ASSOC_DATA_4,
    BIOG_ADDR_DATA,
    BIOG_INST_DATA,
    BIOG_SOURCE_DATA,
    ENTRY_DATA,
    KIN_DATA_1,
    KIN_DATA_2,
    POSTED_TO_ADDR_DATA,
    POSTING_DATA,
    POSTED_TO_OFFICE_DATA,
    STATUS_DATA,
    TEXT_DATA,
    EVENTS_DATA,
    POSSESSION_DATA,
    # DATABASE_LINK_DATA excluded - see comment above
    BIOG_MAIN,
]

# Source sql
SOURCE_SQL = " AND c_source = %s;"


def get_list(id_list):
    output = []
    with open(id_list, "r", encoding="utf-8") as f:
        csv_handle = csv.reader(f, delimiter="\t")
        for row in csv_handle:
            output.append(row)
    return output


def generate_update_sqls(id_list):
    output = []
    for id_row in id_list:
        confirmed_id = id_row[0]
        to_remove_id = id_row[1]
        source_id = id_row[2]
        for sql_list_value in update_sql_list:
            # For splitting persons base on source id
            if source_id != "None":
                assert sql_list_value.endswith(";"), f"SQL statement must end with semicolon: {sql_list_value}"
                new_sql = sql_list_value[:-1] + SOURCE_SQL
                if "BIOG_SOURCE_DATA" in new_sql:
                    new_sql = new_sql.replace("c_source", "c_textid")
                # There is no c_source in POSTED_TO_ADDR_DATA, so I have to innner join POSTED_TO_OFFICE_DATA.c_source
                if "POSTED_TO_ADDR_DATA" in new_sql:
                    new_sql = POSTED_TO_ADDR_DATA_FOR_SOURCE_UPDATE
                if "POSTING_DATA" in new_sql:
                    new_sql = POSTING_DATA_FOR_SOURCE_UPDATE
                output.append(new_sql % (confirmed_id, to_remove_id, source_id))
            else:
                output.append(sql_list_value % (confirmed_id, to_remove_id))
    return output


def generate_delete_sqls(id_list):
    output = []
    for id_row in id_list:
        to_remove_id = id_row[1]
        source_id = id_row[2]
        for sql_list_value in delete_sql_list:
            if source_id != "None":
                assert sql_list_value.endswith(";"), f"SQL statement must end with semicolon: {sql_list_value}"
                new_sql = sql_list_value[:-1] + SOURCE_SQL
                if "BIOG_SOURCE_DATA" in new_sql:
                    new_sql = new_sql.replace("c_source", "c_textid")
                # if there is a source id, we don't need to delete, but split persons
                if "BIOG_MAIN" in new_sql:
                    continue
                if "POSTED_TO_ADDR_DATA" in new_sql:
                    new_sql = POSTED_TO_ADDR_DATA_FOR_SOURCE_DELTE
                if "POSTING_DATA" in new_sql:
                    new_sql = POSTING_DATA_FOR_SOURCE_DELTE
                output.append(new_sql % (to_remove_id, source_id))
            else:
                output.append(sql_list_value % (to_remove_id))
    return output


def output_data(output_file, update_sqls):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(update_sqls)


# list format [confirmed_id, to_remove_id]
id_list = get_list("id_list.txt")
update_sqls = generate_update_sqls(id_list)
output_data("output_update_sqls.txt", "\n".join(update_sqls))
delete_sqls = generate_delete_sqls(id_list)
output_data("output_delete_sqls.txt", "\n".join(delete_sqls))

print("Done!")
