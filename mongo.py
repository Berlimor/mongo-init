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
                "schema_id": "668bbf39213a4ce5b16e5e8e46849fc2",                          # ID схемы
                "schema_name": "Простая операция",                                        # Имя операции
                "schema_print_name": "Простая",                                           # Короткое имя для печати
                "schema_stages": [                                                        # Лист этапов. Постараемся избавиться от IDшников, работать с номерами стейджей.
                    {
                    "name": "Установка блока управления",                                 # Имя стейджа
                    "type": "long",                                                       # Тип. long - требует время (как завод), short - как весы.
                    "description": "Установить блок управления....",                      # Описание. Выводится сотруднику
                    "equipment": [
                        "Квадратные пресс-клещи для блока управления"                       # Оборудование. Тоже выводится. Потом решим, как и куда (в начале или на каждый этап)
                    ],
                    "workplace": "Сборочный стол",                                        # Рабочее место
                    "duration_seconds": 0                                                 # Длительность этапа. Пригодится потом.
                    },
                    {
                    "name": "Снятие блока управления",                                    # Имя стейджа
                    "type": "long",                                                       # Тип. long - требует время (как завод), short - как весы.
                    "description": "Снять блок управления....",                           # Описание. Выводится сотруднику
                    "equipment": [
                        "Квадратные пресс-клещи для блока управления"                       # Оборудование. Тоже выводится. Потом решим, как и куда (в начале или на каждый этап)
                    ],
                    "workplace": "Сборочный стол",                                        # Рабочее место
                    "duration_seconds": 0                                                 # Длительность этапа. Пригодится потом.
                    }
                ],
                "components_schema_ids": None,                                            # Если это родительская операция и под нее надо сканить компоненты
                "parent_schema_id": None,                   # Если она включена в какую-то схему
                "schema_type": "complex",                                                  # short - весы, long - завод, complex - эндо старс
                "erp_metadata": {"order_id": "00000", "water_id": "abc123"}
            })


if __name__ == '__main__':
    Mongo = _MongoWrapper()
    Mongo.fill_emp_db()
    Mongo.fill_schema_db()
    print('DONE')
