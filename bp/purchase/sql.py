from datetime import date, timedelta

from flask import url_for

import SQL.ClsClms as Clm
import SQL.SqlBase as Sql


class tBom_PurchaseOrders(Clm.Calms):
  def __init__(self):
    super().__init__("tBom_PurchaseOrders")
    self.add(Clm.ClmID())
    self.add(Clm.ClmCreateDate())
    self.add(Clm.ClmStr("供应商_代码", only=True))
    self.add(Clm.ClmStr("供应商", only=True))
    self.add(Clm.ClmDate("日期", only=True))
    self.add(Clm.ClmStr("编号", only=True))
    self.add(Clm.ClmStr("业务员", only=True))
    self.add(Clm.ClmStr("物料代码", only=True))
    self.add(Clm.ClmStr("单位", only=True))
    self.add(Clm.ClmStr("数量", only=True))
    self.add(Clm.ClmDate("交货日期", only=True))
    Sql.set_check_create(self)

  def get_list_pn(self):
    s0 = f"SELECT DISTINCT([编号]) FROM tBom_PurchaseOrders"
    return Sql.get_list(s0)

  def __get_html_a(self, df):
    # http://192.168.8.145:5000/purchase/?q=%E7%BC%96%E5%8F%B7%E6%9F%A5%E8%AF%A2,PO-1805-0256%E9%92%A7%E6%81%92
    html = "<ul>"
    for idx, row in df.iterrows():
      id1 = row['编号']
      # test
      href = url_for('purchase.detail', id=id1)
      html += "<li>"
      html += f"<a href = {href} > {row['编号']} </a >"
      html += f"<div> 业务员: {row['业务员']} </div>"
      html += f"<div> 供应商代码: {row['供应商_代码']} </div>"
      html += f"<div> 供应商: {row['供应商']} </div>"
      html += f"<div> 物料代码: {row['物料代码']} </div>"
      html += f"<div> 单位: {row['单位']} </div>"
      html += f"<div> 数量: {row['数量']} </div>"
      html += f"<div> 交货日期: {row['交货日期']} </div>"
      html += "</li>"
    html += "</ul>"
    return html

  def get_html_date(self, selected_date):
    data_b = date(selected_date.year, selected_date.month, selected_date.day)
    data_b += timedelta(days=1)
    where = f"where [交货日期] >= N'{selected_date}' AND [交货日期] < N'{data_b}'"
    s0 = f"select * from tBom_PurchaseOrders {where} ORDER BY [物料代码]"
    df = Sql.get_table(s0)
    return self.__get_html_a(df)

  def get_html_pn(self, value):
    s0 = f"select * from tBom_PurchaseOrders where [编号]='{value}'"
    df = Sql.get_table(s0)
    return self.__get_html_a(df)


calms: tBom_PurchaseOrders = tBom_PurchaseOrders()


def insert(calms_name, calms_value):
  s0 = f"INSERT INTO {calms.tableName} ({','.join(calms_name)}) VALUES ({','.join(calms_value)})"
  res = Sql.get_server(s0)
  if res is False:
    print(s0)


def test():
  lista = []
  for i in calms.list_clm:
    lista.append(i.get_str())
  s0 = ','.join(lista)
  s_name = 'tBom_PurchaseOrders'
  s1 = f"IF object_id('{s_name}') IS NULL create table {s_name} ({s0})"
  return s1


def get_row_by_id(s_id):
  print(s_id)
  s0 = f"select * from tBom_PurchaseOrders where [编号] = '{s_id}'"
  rows = Sql.get_rows(s0)
  print(rows)
  return rows
