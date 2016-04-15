from .base import BaseList
from .response import response
from server import VERSION


class About(BaseList):

    @response
    def get(self):
        return {
            'version': '.'.join(map(str, VERSION))
        }
