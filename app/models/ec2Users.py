from pydantic import BaseModel

class EC2UserModel(BaseModel):
    key: int
    name: str
    created_at: str
    resourceactions: str
    resourceactionappliedto: str
    actionpermission: str
    sourcepolicyId: str
    sourcepolicyType: str
