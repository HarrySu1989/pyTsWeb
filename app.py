from flask import Flask

import glb.ViewBase as vb
from bp.auth.auth import bp as bp_auth
from bp.bom.route import bp as bp_bom
from bp.flow.route import bp as bp_flow
from bp.purchase.route import bp as bp_purchase
from bp.station.route import bp as bp_station
import glb.log as log
# from bp.K3.route import bp as bp_k3
log.add_log_b(f"RunA-test")
app = Flask(__name__)
app.secret_key = 'mysecretkey'
vb.set_add(app, "工序", bp_station)
vb.set_add(app, "采购单", bp_purchase)
vb.set_add(app, "BOM", bp_bom)
vb.set_add(app, "流量仪", bp_flow)
# vb.set_add(app, "K3", bp_k3)
app.register_blueprint(bp_auth)
log.add_log_b(f"RunB")


#
# # before_request/ before_first_request/ after_request
# # hook
# @app.before_request
# def my_before_request():
#     usre_id = session.get("user_id")
#     print("用户登录" )
#     print(usre_id)
#     # if usre_id:
#     #     user = UserModel.query.get(usre_id)
#     #     setattr(g, 'user', user)
#     # else:
#     #     setattr(g, 'user', None)
@app.route('/')
def hello_world():  # put applicae
  res = vb.get_view()
  return res


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
