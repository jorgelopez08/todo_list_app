import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://jlo:iEaGAPPln90FWW3m@todos.m5mqudb.mongodb.net/?retryWrites=true&w=majority')

db = client.todos