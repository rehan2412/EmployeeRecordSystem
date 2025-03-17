### Client-Side (Async CSV Processing & API Calls)
import asyncio
import aiohttp
import csv

API_URL = "http://127.0.0.1:8000/api/employees/"  # Server Endpoint
CSV_FILE = "employees.csv"

async def send_employee(session, employee):
    async with session.post(API_URL, json=employee) as response:
        return await response.text()

async def process_csv():
    async with aiohttp.ClientSession() as session:
        tasks = []
        with open(CSV_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(send_employee(session, row))
        results = await asyncio.gather(*tasks)
        print(results)

if __name__ == "__main__":
    asyncio.run(process_csv())