# -*- coding: utf-8 -*-

import sys
import os

from .config import SRC_ROOT
sys.path.append(SRC_ROOT)

from server import create_app

app = create_app(
    config_object=os.environ.get('API_CONFIG', 'config.Development')
)
