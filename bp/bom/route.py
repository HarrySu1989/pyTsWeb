from flask import Blueprint, request, render_template
import glb.ViewBase as vb
import SQL.SqlBase as Sql
import math
from decorators import login_required
bp = Blueprint('bom', __name__, url_prefix='/bom')

def GetSelect(q):
    if q is None:
        return None
    list = []
    if q:
        list = q.strip().split(' ')
    else:
        list.append(q)
    return list


def GetPage(page):
    if page is None:  # 默认设置页码为1
        page = 1
    else:
        page = int(page)
    return page

@bp.route('/')
@login_required
def index():
    page_size = 50  # 每页的数量
    select_size = 11
    page = GetPage(request.args.get('page'))
    html=""
    q = request.args.get('q')
    html_key=""
    if q is not None:
        html_key=f'value="{q}"'
    else:
        html_key=f'placeholder="关键字"'
    html_form=f"""	<form class="form-inline my-2 my-lg-0" method="GET">
		<div class="col-lg-6 col-xxl-6 my-5 mx-auto">
			<div class="d-grid gap-4">
				<input class="form-control mr-sm-2" type="search" {html_key} aria-label="Search" name="q">
			</div>
		</div>
	</form>"""
    list = GetSelect(q)

    # Selecting Some Data
    sWhere = ""
    if list is not None:
        sWhere = "where "
        listb = []
        for i in list:
            listb.append(f"([物料代码] like '%{i}%' or [物料名称] like '%{i}%')")
        sWhere += "and ".join(listb)

    df = Sql.get_table (f'select * from V_BOM_PnData {sWhere} ORDER BY 物料代码')
    iend = math.ceil(len(df) / page_size)
    iOffset = page - 5
    if iOffset <= 0:
        iOffset = 1
    sSearch = ''
    if q is not None:
        sSearch = f'q={q.replace(" ", "+")}&'
    listPage = {}
    if iOffset > 1:
        listPage['首页'] = f'/bom/?{sSearch}page=1'
    if page > 1:
        listPage['上一页'] = f'/bom/?{sSearch}page={page - 1}'

    bEnd = False
    for i in range(iOffset, iOffset + 11):
        if i > iend:
            bEnd = True
            break
        listPage[str(i)] = f'/bom/?{sSearch}page={i}'
    iNext = page + 1

    if iNext <= iend:
        listPage['下一页'] = f'/bom/?{sSearch}page={iNext}'
    if not bEnd:
        listPage['尾页'] = f'/bom/?{sSearch}page={iend}'

    start_index = (page - 1) * page_size
    end_index = page * page_size
    page_data = df[start_index:end_index]
    html_detail="<ul>"
    for idx, row in page_data.iterrows():
        html_detail+="<li>"
        html_detail+=f'<a href="#">{row["物料代码"]}</a>'
        html_detail+=f'<div>{row["物料名称"] }</div>'
        html_detail+="</li>"
    html_detail+="</ul>"
    html_page="""
<style>
ul.pagination {
    display: inline-block;
    padding: 0;
    margin: 0;
}
ul.pagination li {display: inline;}
ul.pagination li a {
    float: left;
    padding: 8px 16px;
    text-decoration: none;
    border-radius: 5px;
}
ul.pagination li a.active {
    background-color: #4CAF50;
    color: white;
    border-radius: 5px;
}
ul.pagination li a:hover:not(.active) {background-color: #ddd;}
</style>
"""
    html_page+=f'<ul class="pagination">'
    for key, value in listPage.items():
        if key == str(page):
            html_page+=f'<li><a href="{ value }" class="active">{ key }</a></li>'
        else:
            html_page+=f'<li><a href="{ value }">{ key }</a></li>'
    html_page+=f'</ul>'
    html_body=html_form+html_detail+html_page
    return vb.get_view(bp, html_body)
