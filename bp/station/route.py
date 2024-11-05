import glb.ViewBase as vb
import glb.uc as uc
import bp.station.select_a_station_type.glb as sel_a
import bp.station.download.glb as download_a
from datetime import datetime, timedelta
from flask import Blueprint, url_for

bp = Blueprint('station', __name__, url_prefix='/station')


class ItemOptionGx(uc.ItemOption):
  def __init__(self):
    super().__init__(sel_a.get_list())

  def set_init(self, s_value):
    if s_value not in sel_a.get_list():
      self.value = sel_a.get_list()[0]
    sel_a.dic_data[self.value].c_data.set_refresh()


class ItemYear(uc.ItemOption):
  def __init__(self):
    now = datetime.now().date()
    i_year_cur = now.year
    i_month_cur = now.month
    i_year_before = 2020
    r = range(i_year_before, i_year_cur + 1).__reversed__()
    self.list_year = []
    for i in r:
      self.list_year.append(str(i) + "年")
    super().__init__(self.list_year)


class ItemMonth(uc.ItemOption):
  def __init__(self):
    self.list_month = []
    for i in range(1, 13):
      self.list_month.append(str(i) + "月")
    super().__init__(self.list_month)

  def set_init(self, s_value):
    if s_value not in self.list_month:
      self.value = str(datetime.now().date().month) + "月"


class ItemOrder(uc.ItemInputList):
  def __init__(self, s_gx):
    super().__init__()
    self.list_str = sel_a.dic_data[s_gx].c_data.get_list_order()


class ItemPartNumber(uc.ItemInputList):
  def __init__(self, s_gx):
    super().__init__()
    self.list_str = sel_a.dic_data[s_gx].c_data.get_list_part_num()


class ItemWeek(uc.ItemOption):
  def __init__(self):
    self.list_week = []
    for i in range(1, 6):
      self.list_week.append(f"第{i}周")
    super().__init__(self.list_week)


class ItemSelect(uc.ItemOption):
  def __init__(self, s_gx):
    self.s_gx = s_gx
    super().__init__(["日报表", "周报表", "月报表", "年报表", "工单报表", "型号报表"])

  def set_init(self, s_value):

    if s_value == "年报表":
      self.list_child.append(ItemYear())
    elif s_value == "月报表":
      self.list_child.append(ItemYear())
      self.list_child.append(ItemMonth())
    elif s_value == "周报表":
      self.list_child.append(ItemYear())
      self.list_child.append(ItemMonth())
      self.list_child.append(ItemWeek())
    elif s_value == "工单报表":
      self.list_child.append(ItemOrder(self.s_gx))
    elif s_value == "型号报表":
      self.list_child.append(ItemPartNumber(self.s_gx))
    else:
      self.value = "日报表"
      self.list_child.append(uc.ItemDate())

  def get_html_body(self):
    df = None
    if self.value == "日报表":
      date_a = datetime.strptime(self.list_child[0].value, "%Y-%m-%d")
      df = sel_a.dic_data[self.s_gx].c_data.get_dt_day(date_a)
    elif self.value == "年报表":
      i_year = int(self.list_child[0].value.replace("年", ""))
      df = sel_a.dic_data[self.s_gx].c_data.get_dt_year(i_year)
    elif self.value == "月报表":
      i_year = int(self.list_child[0].value.replace("年", ""))
      i_month = int(self.list_child[1].value.replace("月", ""))
      df = sel_a.dic_data[self.s_gx].c_data.get_dt_month(i_year, i_month)
    elif self.value == "周报表":
      i_year = int(self.list_child[0].value.replace("年", ""))
      i_month = int(self.list_child[1].value.replace("月", ""))
      i_week = int(self.list_child[2].value.replace("第", "").replace("周", ""))
      df = sel_a.dic_data[self.s_gx].c_data.get_dt_week(i_year, i_month, i_week)
    elif self.value == "工单报表":
      s_order = self.list_child[0].value
      df = sel_a.dic_data[self.s_gx].c_data.get_dt_order(s_order)
    elif self.value == "型号报表":
      s_part_num = self.list_child[0].value
      df = sel_a.dic_data[self.s_gx].c_data.get_dt_part_num(s_part_num)
    return uc.get_html_df(df)

  def download_set_list_str_where(self, list_str_where):
    s_key = self.value
    if s_key not in ["日报表", "周报表", "月报表", "年报表"]:
      return
    day_begin = datetime.now()
    day_end = datetime.now()
    if s_key == "日报表":
      day_begin = datetime.strptime(self.list_child[0].value, "%Y-%m-%d")
      day_end = day_begin + timedelta(days=1)
    elif s_key == "周报表":
      i_year = int(self.list_child[0].value.replace("年", ""))
      i_month = int(self.list_child[1].value.replace("月", ""))
      i_week = int(self.list_child[2].value.replace("第", "").replace("周", ""))
      time = datetime(i_year, i_month, 1)
      day_num = time.isoweekday()  # 当前天是这周的第几天
      time = time - timedelta(days=day_num)
      offset = (i_week - 1) * 7
      day_begin = time + timedelta(days=offset)
      day_end = day_begin + timedelta(days=7)
    elif s_key == "月报表":
      i_year = int(self.list_child[0].value.replace("年", ""))
      i_month = int(self.list_child[1].value.replace("月", ""))
      day_begin = datetime(i_year, i_month, 1)
      i_month += 1
      if i_month > 12:
        i_month = 1
        i_year += 1
      day_end = datetime(i_year, i_month, 1)
    elif s_key == "年报表":
      i_year = int(self.list_child[0].value.replace("年", ""))
      day_begin = datetime(i_year, 1, 1)
      day_end = datetime(i_year + 1, 1, 1)
    s_begin = f"""{str(day_begin.year)}-{str("%02d" % day_begin.month)}-{str("%02d" % day_begin.day)}"""
    s_end = f"""{str(day_end.year)}-{str("%02d" % day_end.month)}-{str("%02d" % day_end.day)}"""
    list_str_where.append(f"OnDate>='{s_begin}'")
    list_str_where.append(f"OnDate<'{s_end}'")

  def get_list_str(self):
    list_str_where = []
    self.download_set_list_str_where(list_str_where)
    if self.value == "工单报表":
      list_str_where.append(f"OrderNum='{self.list_child[0].value}'")
    elif self.value == "型号报表":
      list_str_where.append(f"PartNum='{self.list_child[0].value}'")
    return list_str_where


class Guide(uc.Guide):
  def __init__(self):
    super().__init__()
    self.item_gx = ItemOptionGx()
    self.set_add(self.item_gx)
    self.item_select = ItemSelect(self.item_gx.value)
    self.set_add(self.item_select)


@bp.route('/download/')
def download():
  guide = Guide()
  list_str_where = guide.item_select.get_list_str()
  df = sel_a.dic_data[guide.item_select.s_gx].c_data.get_df(list_str_where)
  return download_a.send_file_excel(df, guide.s_q)


@bp.route('/')
def index():
  guide = Guide()
  html_end = f"""<a href="{url_for('station.download', q=guide.s_q)}" >下载</a>"""
  html = guide.get_html(html_end)
  html += guide.item_select.get_html_body()

  return vb.get_view(bp, html)
