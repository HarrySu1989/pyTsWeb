import pyodbc
import SQL.ClsClms
import socket
import pandas as pd
import urllib
from sqlalchemy import create_engine
sConnect = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.90;DATABASE=TestModuleResult;UID=xjs;PWD=Xia0601"
host_name=socket.gethostname()
if host_name in ('LAPTOP-57TK7AD9','Harry'):
    sConnect = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=TestModuleResult;UID=sa;PWD=123456'
print(f"数据库配置:{sConnect}")


def get_table(s0) -> pd.DataFrame:
    # 创建SQLAlchemy引擎
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % sConnect)
    # 使用pandas读取SQL查询结果到DataFrame
    df = pd.read_sql(s0, engine)
    # 关闭连接（SQLAlchemy引擎管理连接池，通常不需要手动关闭）
    engine.dispose()
    return df

def get_rows(s0):
    cn = pyodbc.connect(sConnect)
    # Create a cursor from the connection
    cursor = cn.cursor()
    cursor.execute(s0)
    rows = cursor.fetchall()
    cn.close()
    return rows
def get_int(s0):
    rows = get_rows(s0)
    if len(rows) == 0:
        return 0
    return rows[0][0]

def get_list(s0):
    rows = get_rows(s0)
    result = []
    for row in rows:
        result.append(row[0])
    return result

def get_server(s0):
    cn = pyodbc.connect(sConnect)
    cursor = cn.cursor()
    res = True
    # noinspection PyBroadException
    try:
        cursor.execute(s0)
        cursor.commit()
    except Exception as e:
        res=False
        print(e)
    cursor.close()
    cn.close()
    return res

def set_check_create(calms:SQL.ClsClms.Calms):
    table_name=calms.tableName
    s0 = f"SELECT table_name FROM information_schema.TABLES WHERE table_name ='{table_name}'"
    rows = get_rows(s0)
    if len(rows) != 0:
        s3 = f"Select name from syscolumns Where ID=OBJECT_ID('{table_name}')"
        rows = get_list(s3)
        for clm in calms.list_clm:
            if clm.name in rows:
                continue
            # print(clm.name)
            s1 = clm.get_str()
            s0 = f"alter table {table_name} add {s1}"
            # print(s0)
            get_server(s0)
        return

    lista = []
    for calm in calms.list_clm:
        lista.append(calm.get_str())
    # noinspection all
    s_with = "WITH(PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)"
    s_item = ','.join(lista)
    s_item += f" PRIMARY KEY CLUSTERED ([ID]){s_with}"
    lista = []
    for calm in calms.list_clm:
        if calm.name == "ID":
            continue
        if calm.only is True:
            lista.append(calm.name)
    if len(lista) != 0:
        s_item_name = lista[0]
        s_ia = f"{table_name}_{s_item_name}"
        s_ib = f"[{s_item_name}]"
        for i in lista[1:len(lista)]:
            s_item_name = i
            s_ia += f"_{s_item_name}"
            s_ib += f",[{s_item_name}]"
        #noinspection all
        s_item += f",CONSTRAINT [{s_ia}] UNIQUE NONCLUSTERED ({s_ib}){s_with}"

    s0 = f"CREATE TABLE {table_name}({s_item})ALTER TABLE {table_name} SET (LOCK_ESCALATION = TABLE)"
    # print(s0)
    get_server(s0)



