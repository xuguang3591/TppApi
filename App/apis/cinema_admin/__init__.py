from flask_restful import Api

from App.apis.cinema_admin.cinema_address_api import CinemaAddressesResource, CinemaAddressResource
from App.apis.cinema_admin.cinema_hall_api import CinemaHallsResource
from App.apis.cinema_admin.cinema_movie_api import CinemaMovieResource
from App.apis.cinema_admin.cinema_movie_hall_api import CinemaMovieHallResource
from App.apis.cinema_admin.cinema_user_api import CinemaUsersResource

cinema_client_api = Api(prefix='/cinema')

cinema_client_api.add_resource(CinemaUsersResource, '/users/')
cinema_client_api.add_resource(CinemaAddressesResource, '/addresses/')
cinema_client_api.add_resource(CinemaAddressResource, '/addresses/<int:id>/')
cinema_client_api.add_resource(CinemaMovieResource, '/movies/')
cinema_client_api.add_resource(CinemaHallsResource, '/halls/')
cinema_client_api.add_resource(CinemaMovieHallResource, '/cinemamoviehalls/')