from flask import request, url_for
import glb.ViewBase as vb
from typing import List
import datetime
class Item:
    def __init__(self):
        self.value = ""
        self.list_child:List[Item] = []

    def set_init(self, s_value):
        return

    def get_html(self,s_q,i_offset):
        return ""

class ItemDate(Item):
    def __init__(self):
        super().__init__()

    def set_init(self, s_value):
        try:
            time=datetime.datetime.strptime(s_value,"%Y-%m-%d")
        except:
            self.value = datetime.datetime.now().strftime("%Y-%m-%d")

    def get_html(self,s_q,i_offset):
        res = f'<input id="date" type="date" value="{self.value}" onchange="flask_url(\'{s_q}\',{i_offset},this.value)">'
        return res

class ItemInputList(Item):
    def __init__(self):
        super().__init__()

        self.list_str=[]
    # def set_init(self, s_value):
    #     self.value = s_value

    def get_html(self,s_q,i_offset):

        html = f'<input list="aaa" onchange="flask_url(\'{s_q}\',{i_offset},this.value)" placeholder="{self.value}" style="width:300px" autocomplete="off">'
        html += f'<datalist id="aaa">'
        for a in self.list_str:
            html += f'<option >{a}</option>'
        html += '</datalist>'
        return html

class ItemOption(Item):
    def __init__(self, list_str):
        super().__init__()
        self.list_str = list_str
    def set_init(self, s_value):
        for i in self.list_str:
            if i == s_value:
                return
        self.value = self.list_str[0]

    def get_html(self,s_q,i_offset):
        html = f'<select onchange="flask_url(\'{s_q}\',{i_offset},this.value)">'
        for v in self.list_str:
            if v == self.value:
                html += f'<option selected="selected">{v}</option>'
            else:
                html += f"<option>{v}</option>"
        html += '</select>'
        return html


class Guide:
    def __init__(self):
        q = request.args.get('q')
        self.l_q = []
        self.l_item: List[Item] = []
        self.i_count = 0
        if q:
            self.l_q = q.split(',')

    def set_add(self, item: Item):

        if len(self.l_q) > 0:
            value = self.l_q.pop(0)
            item.value = value
        self.i_count += 1
        self.l_item.append(item)
        item.set_init(item.value)
        for item in item.list_child:
            self.set_add(item)

    @property
    def s_q(self):
        list_q = []
        for item in self.l_item:
            list_q.append(item.value)
        return ",".join(list_q)


    def get_html(self,html_end=""):
        s_q = self.s_q
        print(f"刷新工序界面,条件：{s_q}")
        html = ""
        i_offset = 0
        s_menu=""
        for item in self.l_item:
            s_menu += item.get_html(s_q,i_offset)
            i_offset+=1
        s_menu =f'''
<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <div class="btn-toolbar mb-2 mb-md-0">
        {s_menu}
    </div>
    {html_end}
</div>
        '''
        html += s_menu
        html += f'<script src="{url_for("static", filename="guide.js")}"></script>'
        return html


def get_html_df(df):
     # //http://192.168.124.22:5000/station/?q=%E6%8E%A5%E6%94%B6%E8%80%A6%E5%90%88,%E6%97%A5%E6%8A%A5%E8%A1%A8,2024-04-07
    # print(type(df))
    list = df.iloc[:, 0].values.tolist()
    s_head=""
    for i in df:
        s_head+=f'<th scope="col">{i}</th>'
    data_list = df.values.tolist()
    s_data=""
    for i in data_list:
        s_data+=f"<tr>"
        for j in i:
            s_data+=f"<td>{j}</td>"
        s_data+=f"</tr>"
        # print(i)
     # for row in df.rows:
    #     print(row)

    html=f"""<canvas class="my-4 w-100" id="myChart1" width="1170" height="494" style="display: block; box-sizing: border-box; height: 395px; width: 936px;"></canvas>"""
    html+=f"""<div class="table-responsive small">
     <table id="tb1" class="table table-striped table-sm">
        <thead>
        <tr>
            {s_head}
        </tr>
        {s_data}
        </tbody>
     </table>
 </div>
 
<script src="/static/chart.js"></script>
<script src="/static/dashboard.js"></script>
"""
    return html


def get_text(param,i=5,line=30):
    res= f"<h{i}>{param}</h{i}>"
    for i in range(line):
        res += "<br>"
    return res