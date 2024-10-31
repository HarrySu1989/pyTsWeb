
import typing
from bp.station.select_a_station_type.data import Data as DataGxs
class ClsDate:
    def __init__(self,id1,sql_a):
        self.id1=id1
        self.sql_a=sql_a
        self.c_data: DataGxs =DataGxs(sql_a)

dic_clm_hand={}
dic_id_max={}
list_gx=[]
dic_data:typing.Dict[str,ClsDate]={}
def add(id1, text, sql_a):
    list_gx.append(text)
    dic_data[text] = ClsDate(id1,sql_a)

def init():
    add(16, "贴片", "tOdB3_ChipMounter")
    add(14, "固件下载", "tOdB3_FirmWare")
    add(17, "固件烧录", "tOdB3_Fw")
    add(18, "固件升级", "tOdB3_FwIIC")
    add(44, "发射耦合", "tOdB6_Coupling")
    add(46, "接收耦合", "tOdB6_CouplingRx")
    add(48, "收发耦合", "tOdB6_CouplingTxRx")
    add(47, "耦合测试", "tOdB6_CouplingTest")
    add(49, "温循后测试", "tOdB6_CouplingTemp")
    # noinspection all
    add(11, "自动调试", "tOdB1_Tunn")
    # noinspection all
    add(15, "恢复FSN", "tOdB1_TunnFSN")
    add(21, "常温测试", "tOdB0_Test")
    add(22, "高温测试", "tOdB0_Test_TempH")
    add(23, "低温测试", "tOdB0_Test_TempL")
    add(27, "传纤测试", "tOdB0_Test_CQ")
    add(31, "写码1", "tOdB2_Code")
    add(32, "写码2", "tOdB2_CodeB")
    # noinspection all
    add(71, "AocQsfp测试", "tOdB0_Test_AocQsfp")
    add(33, "交换机测试", "tOdB0_Test_AocSwitchBoard")
    add(34, "模块交换机测试1", "tOdB0_Test_Switch")
    add(35, "模块交换机测试2", "tOdB0_Test_SwitchB")
    add(36, "模块交换机测试3", "tOdB0_Test_SwitchC")
    add(37, "模块交换机测试4", "tOdB0_Test_SwitchD")
    add(38, "模块交换机测试5", "tOdB0_Test_SwitchE")
    add(39, "模块交换机测试6", "tOdB0_Test_SwitchF")
    add(40, "模块交换机测试7", "tOdB0_Test_SwitchG")
    # noinspection all
    add(12, "研发调试", "tOdB1_TunnRD"),
    add(26, "OQC", "tOdBa_OqcPd"),
    add(68, "数据检测", "tOdBa_OqcDataCheck"),
    add(61, "AOC校准", "tOdB8_AocCal"),
    add(63, "AOC点胶", "tOdBc_BertD"),
    add(67, "AOC初测", "tOdBc_BertT"),
    add(62, "AOC测试", "tOdBc_Bert"),
    add(64, "AOC测试低温", "tOdBc_BertL"),
    add(65, "AOC测试高温", "tOdBc_BertH"),
    add(66, "模块老化A", "tOdBc_BurnIn")

init()


def get_list():
    return list_gx
