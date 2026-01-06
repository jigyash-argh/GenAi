from motor.motor_asyncio import AsyncIOMotorClient
mongoUrl = "mongodb+srv://shukla"
client= AsyncIOMotorClient(mongoUrl)
db=client.PFDChatbotDatabase
