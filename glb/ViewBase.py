from typing import Dict

from flask import Flask, render_template, Blueprint, session, url_for

dict: Dict[str, Blueprint] = {}


def get_view(bp=None, s_body=""):
  list_a = []
  s_title = "主页"
  if bp:
    list_a.append(f'<li><a href="/" class="nav-link px-2 link-body-emphasis">{s_title}</a></li>')
  else:
    list_a.append(f'<li><a href="/" class="nav-link px-2 link-secondary">{s_title}</a></li>')

  for k, l in dict.items():
    if bp and bp.url_prefix == l.url_prefix:
      s_title = k
      list_a.append(f'<li><a href="{l.url_prefix}" class="nav-link px-2 link-secondary">{k}</a></li>')
    else:
      list_a.append(f'<li><a href="{l.url_prefix}" class="nav-link px-2 link-body-emphasis">{k}</a></li>')
  s_username = session.get("user_id")
  html_login = f"""<a class="nav-link" href="{url_for('auth.login')}">登录</a>"""
  if s_username:
    html_login = f"""<ul class="nav">
        <li class="nav-item"><a href="#" class="nav-link link-body-emphasis px-2">{s_username}</a></li>
        <li class="nav-item"><a href="{url_for('auth.logout')}" class="nav-link link-body-emphasis px-2">{"退出登录"}</a></li>
      </ul>"""

    #   f""" <li class="nav-item">
    #   <span class="nav-link">{ s_username }</span>
    # </li>
    # <li class="nav-item">
    #   <a class="nav-link" href="{ url_for('auth.logout') }">退出登录</a>
    # </li>"""

  return render_template('base.html', s_title=s_title, html_login=html_login, s_menu="".join(list_a), s_body=s_body)


def set_add(app: Flask, s_key, route):
  dict[s_key] = route
  app.register_blueprint(route)
