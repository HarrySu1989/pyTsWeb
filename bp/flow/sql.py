# tOdBd_flow
import SQL.SqlBase as Sql
import traceback
table = "tOdBd_flow"
# noinspection all
list_clm = Sql.get_list(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'")


def set_insert(df,s_operator,s_order_num):
  # list_clm_from=df.columns
  # for clm in list_clm_from:
  #   l_clm_name=[]
  #   if clm in list_clm:
  #     l_clm_name.append(clm)
  try:
    for index, row in df.iterrows():
      print("****************************************")
      dick_a={}
      dick_a[f"[Operator]"]=f"'{s_operator}'"
      dick_a["[OrderNum]"]=f"'{s_order_num}'"
      dick_a[f"[bNewest]"]=f"'True'"

      # list_clm_name.append("OrderNum")
      # list_clm_value.append(user)
      dict_row = row.to_dict()
      for key, value in dict_row.items():
        if key in list_clm:
          dick_a[f"[{key}]"]=f"'{value}'"
      fsn=dick_a["[FSN]"]
      dick_a["[OrCode]"]=fsn
      # noinspection all
      Sql.set_insert(f"""UPDATE {table} SET bNewest='False' where FSN={fsn} """)
      # noinspection all
      dick_a[f"[FsnCount]"]= str(Sql.get_int(f"""SELECT count(id) FROM {table} WHERE FSN = {fsn}"""))
      s_clm_name = ",".join(dick_a.keys())
      s_clm_value = ",".join(dick_a.values())
      # noinspection all
      Sql.set_insert(f"""INSERT INTO {table} ({s_clm_name}) values ({s_clm_value})""")
  except :
    trace = traceback.format_exc()
    print(trace)
    return

