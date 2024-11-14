import datetime
import os

from flask import send_file

iCount = 1


def send_file_excel(df, s_filename):
  now = datetime.datetime.now()
  root = os.path.dirname(__file__)
  root = f'{root}/cache'
  if not os.path.exists(root):
    os.makedirs(root)
  global iCount
  filename = f"""{root}/{now.strftime('%Y%m%d%H%M%S')}-{iCount}.xlsx"""
  iCount = iCount + 1
  df.to_excel(filename, index_label='label', merge_cells=False, engine='xlsxwriter')
  # df.to_excel(filename, index_label='label', merge_cells=False)
  return send_file(filename, as_attachment=True, download_name=f'{s_filename}.xlsx')
