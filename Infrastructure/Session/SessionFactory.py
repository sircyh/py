from .CacheSession import CacheSession

class SessionFactory:
    __session = CacheSession()
    @staticmethod
    def get_session():
        return SessionFactory.__session

    @staticmethod
    def set_session(session):
        SessionFactory.__session = session
