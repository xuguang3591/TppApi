from flask_restful import Resource, reqparse, abort, fields, marshal, marshal_with
from werkzeug.datastructures import FileStorage

from App.apis.admin.utils import login_required
from App.apis.api_constant import HTTP_CREATE_OK, HTTP_OK
from App.apis.common.utils import filename_transfer
from App.models.common.movie_model import Movie

parse = reqparse.RequestParser()
parse.add_argument("showname", required=True, help="must support showname")
parse.add_argument("shownameen", required=True, help="must support shownameen")
parse.add_argument("director", required=True, help="must support director")
parse.add_argument("leadingRole", required=True, help="must support leadingRole")
parse.add_argument("type", required=True, help="must support type")
parse.add_argument("language", required=True, help="must support language")
parse.add_argument("duration", required=True, help="must support duration")
parse.add_argument("screeningmodel", required=True, help="must support screeningmodel")
parse.add_argument("openday", required=True, help="must support openday")
parse.add_argument("backgroundpicture", type=FileStorage, help="must support backgroundpicture", location=["files"])


movie_fields = {
    "showname": fields.String,
    "shownameen": fields.String,
    "director": fields.String,
    "leadingRole": fields.String,
    "type": fields.String,
    "language": fields.String,
    "country": fields.String,
    "duration": fields.Integer,
    "screeningmodel": fields.String,
    "openday": fields.DateTime,
    "backgroundpicture": fields.String
}

multi_movie_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(movie_fields))
}


class MoviesResource(Resource):
    @marshal_with(multi_movie_fields)
    def get(self):
        movies = Movie.query.all()
        data = {
            "msg": "ok",
            "stutus": HTTP_OK,
            "data": movies
        }
        return data

    @login_required
    def post(self):
        args = parse.parse_args()
        showname = args.get("showname")
        shownameen = args.get("shownameen")
        director = args.get("director")
        leadingRole = args.get("leadingRole")
        type = args.get("type")
        language = args.get("language")
        country = args.get("country")
        duration = args.get("duration")
        screeningmodel = args.get("screeningmodel")
        openday = args.get("openday")
        backgroundpicture = args.get("backgroundpicture")

        movie = Movie()
        movie.showname = showname
        movie.shownameen = shownameen
        movie.director = director
        movie.leadingRole = leadingRole
        movie.type = type
        movie.language = language
        movie.country = country
        movie.duration = duration
        movie.screeningmodel = screeningmodel
        movie.openday = openday
        if backgroundpicture:
            fileinfo = filename_transfer(backgroundpicture.filename)
            filepath = fileinfo[0]
            backgroundpicture.save(filepath)
            movie.backgroundpicture = fileinfo[1]
        if not movie.save():
            abort(400, msg="can't create movie")

        data = {
            "msg": "create success",
            "status": HTTP_CREATE_OK,
            "data": marshal(movie, movie_fields)
        }
        return data


class MovieResource(Resource):
    def get(self, id):
        movie = Movie.query.get(id)
        if not movie:
            abort(404, msg="movie is not exist")
        data = {
            "meg": "ok",
            "status": HTTP_OK,
            "data": marshal(movie, movie_fields)
        }
        return data

    @login_required
    def patch(self):
        return {"msg": "ok"}

    @login_required
    def put(self):
        return {"msg": "ok"}

    @login_required
    def delete(self):
        return {"msg": "ok"}
