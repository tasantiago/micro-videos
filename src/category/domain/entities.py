from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
import uuid

@dataclass(kw_only=True)
class Category:

  name:str
  description: Optional[str] = None
  is_active:Optional[bool] = True
  created_at:Optional[datetime] = field(default_factory=lambda: datetime.now())
