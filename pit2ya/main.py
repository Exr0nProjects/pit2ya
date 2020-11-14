import asyncio
from api import user_start, user_modify

def entry_start():
    asyncio.run(user_start())

def entry_modify():
    asyncio.run(user_modify())

if __name__ == '__main__':
    entry_start()
