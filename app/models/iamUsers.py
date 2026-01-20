from pydantic import BaseModel

class IAMUserModel(BaseModel):
    key: str
    name: str
    date: str
    mfa: str
    Policies: str
    uppercasechar: str
    lowercasechar: str
    changepass: str
    expass: str
    groups: str
    consolepass: str
    Tags: str
    AccessKeys: str
    lastusedak: str
    lastusedregionak: str
    servivenameak: str
