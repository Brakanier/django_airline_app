from enum import Enum


class Roles(str, Enum):
    USER = 'Users'
    MANAGER = 'Managers'
    ADMIN = 'Admins'
