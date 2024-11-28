from .base import *

env_name = 'local'

if env_name == 'local':
    from .local import *
elif env_name == 'stage':
    from .stage import *
elif env_name == 'prod':
    from .prod import *
