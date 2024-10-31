from flask import Blueprint, render_template, jsonify,redirect,url_for,session,request
import glb.ViewBase as vb
import bp.auth.sql as sql

bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        s_style="""
        <style>
        html,
body {
  height: 100%;
}

.form-signin {
  max-width: 330px;
  padding: 1rem;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

        </style>
        """
        html=f"""
        {s_style}
<main class="form-signin w-100 m-auto">
		<form  method="POST">
			<h1 class="h3 mb-3 fw-normal">用户登录</h1>
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="floatingInput">
				<label for="floatingInput">用户名</label>
			</div>
			<div class="form-floating">
				<input name="password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
				<label for="floatingPassword">密码</label>
			</div>

			<div class="form-check text-start my-3">
				<input name="s_re" class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
				<label class="form-check-label" for="flexCheckDefault">
					记住登录
				</label>
			</div>
			<button class="btn btn-primary w-100 py-2" type="submit">登录</button>

		</form>
	</main>
"""
        return vb.get_view(bp, html)
    elif request.method == "POST":
        s_username=request.form['username']
        s_password=request.form['password']
        s_re=request.form.get("s_re")
        if sql.get_login(str(s_username), s_password):
            session['user_id'] = s_username
            if s_re:
                session.permanent = True
            else:
                session.permanent = False
            return redirect("/")
        else:
            session.pop('user_id', None)
            return redirect(url_for('auth.login'))

        # if form.validate():
        #     email = form.email.data
        #     password = form.password.data
        #     user = UserModel.query.filter_by(email=email).first()
        #     if not user:
        #         print("邮箱在数据库中不存在！")
        #         return redirect(url_for('auth.login'))
        #     if not check_password_hash(user.password, password):
        #         print("密码错误！")
        #         return redirect(url_for('auth.login'))
        #     session['user_id'] = user.id
        #     return redirect("/")
        # else:
        #     print(form.errors)
        #     return redirect(url_for('auth.login'))




@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    # session.clear()
    return redirect(url_for('auth.login'))
