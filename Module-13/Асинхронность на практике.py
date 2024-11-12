import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")  # силач начал соревнования
    for i in range(1, 6):  # для каждого участника количество шаров одинаковое - 5.
        await asyncio.sleep(1 / power)  # задержка обратно пропорциональна силе
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования")  # когда все шары подняты, показываем завершение


async def start_tournament():  # асинхронная функция для турнира

    task1 = asyncio.create_task(start_strongman("Pasha", 3))
    task2 = asyncio.create_task(start_strongman("Denis", 4))
    task3 = asyncio.create_task(start_strongman("Apollon", 5))

    await task1
    await task2
    await task3


asyncio.run(start_tournament())
