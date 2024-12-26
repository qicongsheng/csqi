#!/usr/bin/env python
# -*- coding:utf-8 -*-
import atexit as _atexit
import sys as _sys

from loguru import _defaults
from loguru._logger import Core as _Core
from loguru._logger import Logger as _Logger

logger = _Logger(
    core=_Core(),
    exception=None,
    depth=0,
    record=False,
    lazy=False,
    colors=False,
    raw=False,
    capture=True,
    patchers=[],
    extra={},
)

if _defaults.LOGURU_AUTOINIT and _sys.stderr:
    logger.add(_sys.stderr)

_atexit.register(logger.remove)
