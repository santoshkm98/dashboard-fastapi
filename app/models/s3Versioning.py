from pydantic import BaseModel

class S3VersioningModel(BaseModel):
    key: str
    bucket: str
    versioning: str
    bucket_Encryption: str
    permission: str
    blockPublicAcls: str
    blockPublicPolicy: str
    restrictPublicBuckets: str
    bucket_location: str
