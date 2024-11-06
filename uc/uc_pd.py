import pandas as pd
def get_df(value):
  print(type(value))
  if isinstance(value, list):
    print("这是个列表")
    v_list:list = value
    if isinstance(v_list[0], dict):
      df = pd.DataFrame(value)
      return df
  return None