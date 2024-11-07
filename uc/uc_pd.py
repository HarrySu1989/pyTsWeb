import pandas as pd
def get_df(value):
  if isinstance(value, list):
    v_list:list = value
    if isinstance(v_list[0], dict):
      df = pd.DataFrame(value)
      return df
  return None