from App.models.cinema_admin import CinemaUser


def get_cinema_user(user_ident):

    if not user_ident:
        return None

    user = CinemaUser.query.get(user_ident)
    if user:
        return user

    user = CinemaUser.query.filter(CinemaUser.phone == user_ident).first()
    if user:
        return user

    user = CinemaUser.query.filter(CinemaUser.username == user_ident).first()
    if user:
        return user

    return None
