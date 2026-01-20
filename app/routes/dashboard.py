from fastapi import APIRouter, HTTPException
from app.service.dashboard import DashboardService
from app.schemas.dashboard import DashboardOverview

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)

@router.get("/{client_id}", response_model=DashboardOverview)
async def get_dashboard(client_id: str):
    dashboard = await DashboardService.get_dashboard(client_id)

    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")

    return dashboard
