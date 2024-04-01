import os
from bson import ObjectId
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection


class _MongoWrapper:
    def __init__(self) -> None:
        uri = "mongodb://mongo:27017"
        self.sync_db: Database = MongoClient(uri)["feeccProdTest"]

        self.emp_collection: Collection = self.sync_db["employeeData"]
        self.schemas_collection: Collection = self.sync_db["productionSchemas"]
        self.stages_collection: Collection = self.sync_db["productionStagesData"]
        self.unit_collection: Collection = self.sync_db["unitData"]

    def fill_emp_db(self) -> None:
        if self.emp_collection.count_documents({}) == 0:
            self.emp_collection.insert_one({
                "rfid_card_id": "111111",
                "name": "test_name 1",
                "position": "Operator",
                "username": "operator",
                "hashed_password": "$2b$12$TQImawJuX53TxiPwBkkwRepNhkPVgVP6CEcqup7tfvC5R8AU0caMy",
                "passport_code": "abc123"
            })

    def fill_schema_db(self) -> None:
        if self.schemas_collection.count_documents({}) == 0:
            self.schemas_collection.insert_one({
                "unit_name": "Single Vehicle",
                "schema_id": "2d31e86160d74c6cb6ce83bf249bc853",
                "production_stages": [
                    {
                        "name": "Weight the vehicle",
                        "type": "Weighting",
                        "stage_id": "319419766d5a4e42b45577d008597191",
                    }
                ],
                "erp_metadata": {"order_id": "00000", "water_id": "abc123"}
            })


if __name__ == '__main__':
    Mongo = _MongoWrapper()
    Mongo.fill_emp_db()
    Mongo.fill_schema_db()
    print('DONE')
