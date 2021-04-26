import asyncio
import os
import random
import re
from collections import defaultdict
from functools import wraps

import nonebot










class Service:
     """
    将一组功能包装为服务, 提供增强的触发条件与分群权限管理.

    支持的触发条件:
    `on_message`,
    `on_prefix`, `on_fullmatch`, `on_suffix`,
    `on_keyword`, `on_rex`,
    `on_command`, `on_natural_language`
    """
