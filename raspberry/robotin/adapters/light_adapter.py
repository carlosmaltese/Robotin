from __future__ import annotations

from robotin.adapters.base import BaseAdapter
from robotin.protocol.messages import light_mode


class LightAdapter(BaseAdapter):
    def set_mode(self, name: str) -> None:
        self.send(light_mode(name))

