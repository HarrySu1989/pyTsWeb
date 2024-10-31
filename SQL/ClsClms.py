
class ClsClm:
    def __init__(self, name, name_sql='', only=False):
        self.name = name
        self.nameSql = name_sql
        self.only=only

    def get_str(self):
        return ""

class ClmID(ClsClm):
    def __init__(self):
        ClsClm.__init__(self,"ID",only=True)

    def get_str(self):
        res = f"{self.name} bigint IDENTITY(1,1) NOT NULL"
        return res

class ClmBool(ClsClm):
    def __init__(self,name):
        ClsClm.__init__(self,name)

    def get_str(self):
        return f"bit"

class ClmCreateDate(ClsClm):
    def __init__(self):
        ClsClm.__init__(self,name="CreateDate")

    def get_str(self):
        res = f"[{self.name}] datetime DEFAULT (getdate())"
        return res

class ClmDate(ClsClm):
    def __init__(self,name,only=False):
        ClsClm.__init__(self,name=name,only=only)

    def get_str(self):
        res = f"[{self.name}] datetime"
        return res

class ClmStr(ClsClm):
    def __init__(self,name,i_len = 100,only=False):
        self.i_len = i_len
        ClsClm.__init__(self,name=name,only=only)

    def get_str(self):
        res = f"[{self.name}] varchar({self.i_len})"
        if self.only:
            res += " NOT NULL"
        return res

class Calms:
    def __init__(self,s_table_name):
        self.tableName=s_table_name
        self.list_clm:list[ClsClm]=[]

    def add(self, calm):
        self.list_clm.append(calm)

    def contain(self, value):
        for calm in self.list_clm:
            if calm.name == value:
                return True
        return False

    def get_str_column_select(self):
        list_res = []
        for calm in self.list_clm:
            if calm.nameSql == '':
                list_res.append(f'[{calm.name}]')
            else:
                list_res.append(f'[{calm.nameSql}] as [{calm.name}]')
        return ','.join(list_res)