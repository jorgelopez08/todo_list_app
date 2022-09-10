import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://jlo:iEaGAPPln90FWW3m@todos.m5mqudb.mongodb.net/?retryWrites=true&w=majority')
#client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://api:091008@127.0.0.1:27017/')

db = client.todos