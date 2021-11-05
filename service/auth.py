import calendar
import datetime

import jwt

from constants import JWT_SECRET,JWT_ALGORITHM
from service.user import UserService

class AuthService():
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def getstate_tokens(self, username, password, is_refresh = False ):
        user = self.user_service.get_by_username(username)

        if user is None:
            raise Exception()

        if not is_refresh:

