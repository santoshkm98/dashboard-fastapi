from bson import ObjectId
from app.init.database import get_db
from fastapi import HTTPException

class DashboardService:
    @staticmethod
    async def get_dashboard(client_id: str):
        db = get_db()
        try:
            obj_id = ObjectId(client_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid client_id format")
        
        doc = await db.dashboard.find_one({"_id": obj_id}, {"_id": 0})
        if not doc:
            raise HTTPException(status_code=404, detail="Dashboard not found")
        return doc
