import os
from pathlib import Path

import colorama
import nest_asyncio

from .config import bm_dir, create_config
from .jungle import main

colorama.init()

os.chdir(Path(__file__).parent)

bm_dir().mkdir(0o755, exist_ok=True)

create_config()

nest_asyncio.apply()

__all__ = [
    "main",
]
