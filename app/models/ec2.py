from pydantic import BaseModel

class EC2Model(BaseModel):
    key: int
    type: str
    platform: str
    state: str
    subnetId: str
    vpcId: str
    securityGroupId: str
    securityGroupName: str
    ebsEncryption: str
