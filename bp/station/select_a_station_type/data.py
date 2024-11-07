from typing import Dict
from datetime import timedelta,datetime
import calendar

import SQL.SqlBase as Sql
import glb.cache as cache
import pandas as pd
import glb.log as log

class Data:
    def __init__(self,sql_a):
        self.sql_a = sql_a
        self.dict: Dict[int, list] = {}
        self.list_clm_head:list[str]=[]
        self.id_cur=0
        self.path=cache.get_path(__file__)
        #noinspection all
        self.dict_clm={
            "ID":"ID",
            "OrderNum":"工单",
            "PartNum":"型号",
            "FSN":"FSN",
            "OnDate":"日期",
            "bResult":"合格",
            "bNewest":"最新",
            "Operator":"操作员",
            "ID_MAC":"电脑",
            "TimeConsum":"上电",
            "TimeConsum2":"切换",
            "TestBoard":"测试版"
            }
        self.df=pd.DataFrame(columns=list(self.dict_clm.keys()))

    @property
    def clm_head(self)->list[str]:
        if len(self.list_clm_head)>0:
            # print(f"从字典加载1:{self.list_clm_head}")
            return self.list_clm_head
        #noinspection all
        s0 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{self.sql_a}'"
        res = Sql.get_list(s0)
        self.list_clm_head= res
        # print(f"从服务器加载1:{res}")
        return res

    def set_refresh(self):
        #noinspection all
        s0 = f"select {','.join(self.dict_clm.keys())} from {self.sql_a} WHERE ID>{self.id_cur} order by ID"
        df=Sql.get_table(s0)
        if len(df) == 0:
            log.add_log(f"工序更新：无需更新，当前共{len(self.df)}行")
            return
        len_a = len(self.df)
        if not len(self.df):
            self.df=df
        else:
            self.df = self.df._append(df, ignore_index=True)
        # print(df)
        log.add_log(f"工序更新：插入{len(df)}行,当前共{len(self.df)}行")
        self.id_cur=self.df.iloc[-1]["ID"]

    def get_list_order(self):
        res = self.df["OrderNum"].unique().tolist()
        return res

    def get_list_part_num(self):
        res = self.df["PartNum"].unique().tolist()
        return res
    def get_df_by_dict(self, df_fsn, dict_date):
        data = {"时间": [], "总数": [], "合格": [], "不合格": []}
        for day_name, date_range in dict_date.items():
            df_count = df_fsn[(df_fsn['OnDate'] >= date_range[0]) & (df_fsn['OnDate'] < date_range[1])]
            df_pass = df_count[(df_count["bResult"]) == True]
            data["时间"].append(day_name)
            data["总数"].append(df_count.shape[0])
            data["合格"].append(df_pass.shape[0])
            data["不合格"].append(df_count.shape[0] - df_pass.shape[0])
        df = pd.DataFrame(data)
        return df

    def get_dt_day(self,date_select):
        dict_date = {}
        for i in range(0, 24):
            dict_date[f"{i + 1}时"] = [date_select + timedelta(hours=i), date_select + timedelta(hours=i + 1)]
        df_fsn = self.df.drop_duplicates(subset=['FSN'], keep='last')
        return self.get_df_by_dict(df_fsn, dict_date)

    def get_dt_year(self, i_year):
        dict_date = {}
        for i_month in range(1, 13):
            if i_month == 12:
                dict_date[f"{i_month}月"] = [datetime(i_year, i_month, 1), datetime(i_year + 1, 1, 1)]
            else:
                dict_date[f"{i_month}月"] = [datetime(i_year, i_month, 1), datetime(i_year, i_month + 1, 1)]
        df_fsn = self.df.drop_duplicates(subset=['FSN'], keep='last')
        return self.get_df_by_dict(df_fsn, dict_date)

    def get_dt_month(self, i_year,i_month):
        dict_date = {}
        for i in range(calendar.monthrange(i_year, i_month)[1] + 1)[1:]:
            date = f"""{str(i_year)}-{str("%02d" % i_month)}-{str("%02d" % i)}"""
            day_begin = datetime.strptime(date, "%Y-%m-%d")
            day_end = day_begin + timedelta(days=1)
            dict_date[f"{i_month}.{i}"] = [day_begin, day_end]
        df_fsn = self.df.drop_duplicates(subset=['FSN'], keep='last')
        return self.get_df_by_dict(df_fsn, dict_date)

    def get_dt_week(self, i_year, i_month, i_week):
        dict_date = {}
        time = datetime(i_year, i_month, 1)
        day_num = time.isoweekday()  # 当前天是这周的第几天
        time = time - timedelta(days=day_num)
        offset = (i_week - 1) * 7
        time = time + timedelta(days=offset)
        for i in range(7):
            day_begin = time + timedelta(days=i)
            day_end = day_begin + timedelta(days=1)
            dict_date[f"{day_begin.month}.{day_begin.day}"] = [day_begin, day_end]
        df_fsn = self.df.drop_duplicates(subset=['FSN'], keep='last')
        return self.get_df_by_dict(df_fsn, dict_date)

    def get_dt_order(self, s_order):
        df_fsn=self.df[self.df["OrderNum"]==s_order]
        df_fsn = df_fsn.drop_duplicates(subset=['FSN'], keep='last')
        #https://www.imooc.com/wenda/detail/730258
        df_date = df_fsn.groupby(pd.DatetimeIndex(df_fsn.OnDate).to_period('D')).nth([0])
        list_date = df_date["OnDate"].tolist()
        dict_date= {}
        for i in list_date:
            dict_date[i.strftime("%Y-%m-%d")]=[i, i + timedelta(days=1)]
        return self.get_df_by_dict(df_fsn, dict_date)

    def get_dt_part_num(self, s_part_num):
        df_part_num=self.df[self.df["PartNum"]==s_part_num]
        df_fsn = df_part_num.drop_duplicates(subset=['FSN'], keep='last')
        list_date = df_fsn["OrderNum"].unique().tolist()
        # print(list_date)
        data = {"时间": [], "总数": [], "合格": [], "不合格": []}
        for i in list_date:
            df_count=df_fsn[df_fsn["OrderNum"]==f'{i}']
            df_pass = df_count[(df_count["bResult"]) == True]
            data["时间"].append(i)
            data["总数"].append(df_count.shape[0])
            data["合格"].append(df_pass.shape[0])
            data["不合格"].append(df_count.shape[0] - df_pass.shape[0])
        df = pd.DataFrame(data)
        return df

    def get_df(self, list_str_where):
        #noinspection all
        s0 = f"""select * from {self.sql_a} where {' and '.join(list_str_where)}"""
        print(s0)
        return Sql.get_table(s0)

























