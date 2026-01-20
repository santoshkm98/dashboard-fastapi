from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB_NAME")

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

def get_db():
    return database
# Collections
s3_versioning_collection = database.get_collection("s3Versioning")
iam_users_collection = database.get_collection("iamUsers")
ec2_collection = database.get_collection("ec2")
s3_bucket_users_collection = database.get_collection("s3BucketUsers")
ec2_users_collection = database.get_collection("ec2Users")