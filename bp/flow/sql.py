# tOdBd_flow
import SQL.SqlBase as Sql
table = "tOdBd_flow"
list_clm = Sql.get_list(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'")


def set_insert(df,user):
  # list_clm_from=df.columns
  # for clm in list_clm_from:
  #   l_clm_name=[]
  #   if clm in list_clm:
  #     l_clm_name.append(clm)
  for index, row in df.iterrows():
    print("****************************************")
    dick_a={}
    dick_a[f"[Operator]"]=f"'{user}'"
    dick_a[f"[bNewest]"]=f"'True'"

    # list_clm_name.append("OrderNum")
    # list_clm_value.append(user)
    dict_row = row.to_dict()
    for key, value in dict_row.items():
      if key in list_clm:
        dick_a[f"[{key}]"]=f"'{value}'"
    print(type(row))
    print(dict_row)
    s_clm_name = ",".join(dick_a.keys())
    s_clm_value = ",".join(dick_a.values())
    fsn=dick_a["[FSN]"]
    Sql.set_insert(f"""UPDATE {table} SET bNewest='False' where FSN={fsn} """)
    b_ok=Sql.set_insert(f"""INSERT INTO {table} ({s_clm_name}) values ({s_clm_value})""")
    print(f"插入数据状态：{b_ok}")
