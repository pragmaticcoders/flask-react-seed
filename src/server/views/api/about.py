from .base import Base
from .response import response
from api import VERSION


class About(Base):

    @response
    def get(self):
        return {
            'version': '.'.join(map(str, VERSION))
        }
