import asyncio
import aiosqlite


async def async_fetch_users():
    async with aiosqlite.connect("alx_prodev") as db:
        cursor = await db.execute("SELECT * FROM users")
        rows = await cursor.fetchall()
        print("All Users:")
        for row in rows:
            print(row)


async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        rows = await cursor.fetchall()
        print("\n Users older than 40:")
        for row in rows:
            print(row)

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

def main():
    await fetch_concurrently()

asyncio.run(main())