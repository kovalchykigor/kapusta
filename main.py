import json

import requests

# email = "fixed_email@gmail.com"  # empty parameter for random email, or pass str for fixed email
# password = "Qwerty123"
# data = {"email": email, "password": password}
#
# response = requests.post('https://kapusta-backend.goit.global/auth/login', json=data)
#
# print(response.text)


json_string = '{"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI2NTgxNzBhOGViMDNiYjNkOTg3ZTUzMGUiLCJzaWQiOiI2NTk2ZGU1Y2ViMDNiYjNkOTg4MDM3MDUiLCJpYXQiOjE3MDQzODYxNDAsImV4cCI6MTcwNDM4OTc0MH0.wRKzGgKZOwA7XCZC8ufo5DHCbHH7-S4-OhhHvZwJ5Vk","refreshToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI2NTgxNzBhOGViMDNiYjNkOTg3ZTUzMGUiLCJzaWQiOiI2NTk2ZGU1Y2ViMDNiYjNkOTg4MDM3MDUiLCJpYXQiOjE3MDQzODYxNDAsImV4cCI6MTcwNzAxNDE0MH0.bRaI5vsIaF2gFjBswn6ZuvgNvvyR3smPWyRVCspYOz4","sid":"6596de5ceb03bb3d98803705","userData":{"email":"fixed_email@gmail.com","balance":1900,"id":"658170a8eb03bb3d987e530e","transactions":[{"_id":"65946f04eb03bb3d98803539","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65946f35eb03bb3d98803543","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65946f97eb03bb3d9880354b","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65946fa3eb03bb3d98803553","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6594703aeb03bb3d9880355b","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947049eb03bb3d98803564","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947063eb03bb3d9880356d","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6594716deb03bb3d98803577","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947290eb03bb3d98803580","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6594730deb03bb3d9880358b","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6594730eeb03bb3d9880358e","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65947501eb03bb3d98803596","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947502eb03bb3d98803599","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65947573eb03bb3d988035a2","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947574eb03bb3d988035a5","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"659475b7eb03bb3d988035ae","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"659475b8eb03bb3d988035b1","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65947783eb03bb3d988035ba","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947784eb03bb3d988035bd","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"659477deeb03bb3d988035c7","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"659477dfeb03bb3d988035ca","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"6594780eeb03bb3d988035d4","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947810eb03bb3d988035d7","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"659478afeb03bb3d988035e4","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"659479f1eb03bb3d988035ee","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"659479f3eb03bb3d988035f1","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65947d41eb03bb3d9880360d","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947d42eb03bb3d98803610","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65947df3eb03bb3d9880361a","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947df4eb03bb3d9880361d","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65947f74eb03bb3d98803628","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65947f75eb03bb3d9880362b","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65948017eb03bb3d98803635","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65948018eb03bb3d98803638","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65948104eb03bb3d98803642","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65948105eb03bb3d98803645","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65948128eb03bb3d9880364f","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65948129eb03bb3d98803652","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65948270eb03bb3d9880365c","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65948271eb03bb3d9880365f","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65952d4deb03bb3d98803664","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65952d4eeb03bb3d98803667","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65953927eb03bb3d9880367b","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6595393aeb03bb3d9880367d","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65953a5eeb03bb3d9880367f","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65953e6beb03bb3d98803681","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65953e7ceb03bb3d98803683","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6595400ceb03bb3d98803685","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6595408deb03bb3d98803687","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6595408eeb03bb3d9880368a","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65954277eb03bb3d9880368e","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"659542fceb03bb3d98803690","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6595430deb03bb3d98803692","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6595449aeb03bb3d98803699","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65954df7eb03bb3d988036a6","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6595552ceb03bb3d988036ad","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65955c0beb03bb3d988036b1","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65955c90eb03bb3d988036b3","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65955d33eb03bb3d988036b6","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65955e9deb03bb3d988036bb","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65955e9feb03bb3d988036be","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65955f40eb03bb3d988036c3","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65955f42eb03bb3d988036c6","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"6595b419eb03bb3d988036cc","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"6595b41ceb03bb3d988036cf","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65966ef3eb03bb3d988036e5","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65966ef6eb03bb3d988036e8","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"},{"_id":"65969980eb03bb3d988036f9","description":"Income description","amount":100,"date":"2020-12-31","category":"З/П"},{"_id":"65969982eb03bb3d988036fc","description":"Expense description","amount":100,"date":"2020-12-31","category":"Продукты"}]}}'
data = json.loads(json_string)
print(data)