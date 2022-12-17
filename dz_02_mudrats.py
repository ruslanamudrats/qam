import requests
server = "https://qauto.forstudy.space/api"
endpoint_auth = "/auth/signin"
endpoint_users = "/users/current"

# сервер та ендпоінт задають урл який ми тестимо
# далі данні що ми шлемо методом пост
example_value = {
  "email": "test578@test.com",
  "password": "Qwerty12345",
  "remember": False
}
# викликаємо метод пост і json= вказує що ми шлем як ДЖСОН
r = requests.post(server+endpoint_auth, json=example_value)
# сервер присилає нм теж ДЖСОН що ми перетворюємол в словник і записуєм у зм. 
server_says = r.json()
# використовуємо методи словника
#  Якщо ключ "status" у словнику то
if "status" in server_says:
    #  Якщо значення клюса статус == ок
    if server_says["status"] == "ok":
        print("all ok")
    #  інакше
    else:
        print(server_says['message'])

r = requests.get(server+endpoint_users, json=example_value)
server_says = r.json()
if "status_code" in server_says:
    if server_says ["status_code"] == 200:
        print("all ok")
    else:
     print(server_says['message'])

