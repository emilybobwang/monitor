# -*- coding: utf-8 -*-
import os


root_path = os.path.dirname(__file__)
configs = dict(
    debug = True,
    template_path=os.path.join(root_path,'templates'),
    static_path = os.path.join(root_path,'static')

)