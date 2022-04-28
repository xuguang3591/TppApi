from flask_restful import Resource, fields, marshal, reqparse, abort

from App.apis.admin.utils import login_required
from App.apis.api_constant import HTTP_OK
from App.models.cinema_admin import CinemaUser

cinema_user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "phone": fields.String,
    'password': fields.String(attribute='_password'),
    'is_verify': fields.Boolean,
}

multi_cinema_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(cinema_user_fields))
}

signal_cinema_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(cinema_user_fields)
}


class AdminCinemaUsersResource(Resource):
    @login_required
    def get(self):
        cinema_users = CinemaUser.query.all()

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": cinema_users
        }
        return marshal(data, multi_cinema_user_fields)


parse = reqparse.RequestParser()
parse.add_argument("is_verify", type=bool, required=True, help="请点击激活")


class AdminCinemaUserResource(Resource):
    @login_required
    def get(self, id):
        cinema_user = CinemaUser.query.get(id)

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": cinema_user
        }
        return marshal(data, signal_cinema_user_fields)

    @login_required
    def patch(self, id):
        args = parse.parse_args()
        is_verify = args.get("is_verify")
        cinema_user = CinemaUser.query.get(id)
        cinema_user.is_verify = is_verify
        if not cinema_user.save():
            abort(400, msg="change fail")
        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": cinema_user
        }
        return marshal(data, signal_cinema_user_fields)
