from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.init.database import (
    s3_versioning_collection,
    iam_users_collection,
    ec2_collection,
    s3_bucket_users_collection,
    ec2_users_collection
)
from app.models.s3Versioning import S3VersioningModel
from app.models.iamUsers import IAMUserModel
from app.models.ec2 import EC2Model
from app.models.s3BucketUsers import S3BucketUserModel
from app.models.ec2Users import EC2UserModel

router = APIRouter()

# Mapping type → collection + model
collection_map = {
    "Storage": (s3_versioning_collection, S3VersioningModel),
    "IAM": (iam_users_collection, IAMUserModel),
    "Compute": (ec2_collection, EC2Model),
    "userss3": (s3_bucket_users_collection, S3BucketUserModel),
    "usersec2": (ec2_users_collection, EC2UserModel),
}

@router.get("/")
async def get_audit_report(type: str):
    collection_map = {
        "Storage": s3_versioning_collection,
        "IAM": iam_users_collection,
        "Compute": ec2_collection,
        "userss3": s3_bucket_users_collection,
        "usersec2": ec2_users_collection
    }

    collection = collection_map.get(type)
    if collection is None:
       return {"error": "Invalid type"}

    data = await collection.find().to_list(1000)

# Remove _id for JSON serialization
    for doc in data:
        doc.pop("_id", None)

    return data
