from pymongo import MongoClient


HOST = "db"
PORT = "27017"

client = MongoClient(f"mongodb://{HOST}:{PORT}/")
db = client["SystemMonitorReports"]
collections = db.AlarmReports
