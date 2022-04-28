from flask_restful import Resource, reqparse, abort, marshal, fields

from App.apis.admin.model_utils import get_admin_user
from App.apis.api_constant import USER_ACTION_REGISTER, HTTP_CREATE_OK, USER_ACTION_LOGIN, HTTP_OK
from App.ext import cache

from App.models.admin import AdminUser
from App.settings import ADMINS
from App.utils import generate_admin_user_token

parse = reqparse.RequestParser()
parse.add_argument("username", type=str, required=True, help="请输入用户名")
parse.add_argument("password", type=str, required=True, help="请输入密码")
parse.add_argument("action", type=str, required=True, help="请确认请求参数")

admin_user_fields = {
    "username": fields.String,
    'password': fields.String(attribute='_password')
}

single_admin_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(admin_user_fields)
}


class AdminUsersResource(Resource):
    def post(self):
        args = parse.parse_args()
        username = args.get("username")
        password = args.get("password")
        action = args.get("action")

        if action == USER_ACTION_REGISTER:
            if get_admin_user(username):
                abort(400, msg="用户已存在，请重新输入用户名")
            admin_user = AdminUser()
            admin_user.username = username
            admin_user.password = password
            if username in ADMINS:
                admin_user.is_super = True
            if not admin_user.save():
                abort(400, msg="create fail")
            data = {
                'status': HTTP_CREATE_OK,
                'msg': "用户创建成功",
                'data': admin_user
            }
            return marshal(data, single_admin_user_fields)

        if action == USER_ACTION_LOGIN:
            user = get_admin_user(username)
            if not user:
                abort(404, msg="用户名或密码错误")
            if not user.check_password(password):
                abort(401, msg="用户名或密码错误")
            if user.is_delete:
                abort(400, msg="用户名或密码错误")
            token = generate_admin_user_token()
            cache.set(token, user.id, timeout=60*60*24*1)
            data = {
                "msg": "login success",
                "status": HTTP_OK,
                "token": token
            }
            return data
        else:
            abort(400, msg="请提供正确的参数")
