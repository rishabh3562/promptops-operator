from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Dict, Optional

class BaseSkill(ABC):
    name: str = "base_skill"
    description: str = ""
    parameters: Dict = {}
    params_model: Optional[BaseModel] = None

    @abstractmethod
    async def run(self, **kwargs):
        pass
