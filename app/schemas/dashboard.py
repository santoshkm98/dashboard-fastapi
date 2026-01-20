from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class PenetrationResult(BaseModel):
    id: int
    name: str
    cvss: float
    severity: str
    url: str

class Insight(BaseModel):
    id: int
    title: str
    category: str
    severity: str

class News(BaseModel):
    id: int
    image: str
    title: str
    releasedOn: datetime
    affectedAssets: Optional[int]
    status: Optional[str]

class AttackPath(BaseModel):
    id: int
    count: int
    heading: str
    description: str

class Notification(BaseModel):
    id: int
    type: str
    title: str
    description: str
    severity: str
    createdAt: datetime

class Ticket(BaseModel):
    id: int
    type: Optional[str] = None
    name: str
    priority: str
    createdAt: Optional[datetime] = None  # matches frontend


class DashboardOverview(BaseModel):
    penetrationResults: List[PenetrationResult]
    charts: Dict[str, dict]
    insights: List[Insight]
    news: List[News]
    attackPaths: List[AttackPath]
    notifications: List[Notification]
    tickets: List[Ticket]
