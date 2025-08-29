import requests


# ===================== USER TEST =====================
# register  and get date
# def post_items(username: str, email: str, password: str):
#     url = 'http://127.0.0.1:8000/register/'
#
#     data = {
#         "username": username,
#         "email": email,
#         "password": password
#     }
#     response = requests.post(url, json=data)
#     return response.status_code, response.json()
#
#
# def get_items():
#     url = "http://127.0.0.1:8000/data/"
#
#     response = requests.get(url)
#     return response.status_code, response.json()
#
# def delete_items(id: int):
#     url = f'http://127.0.0.1:8000/delete/{id}/'
#
#     response = requests.delete(url)
#     return response.status_code
#
#
# post_items("azizbekrahimjonov", "azizbekrahimjonov@weep.com", "1234567890")
# print(get_items())


# ===================== FREIGHT ORDER TEST =====================
# BASE_URL = "http://127.0.0.1:8000"
#
# def create_order():
#     url = f"{BASE_URL}/freight-orders/"
#     data = {
#         "cargo_description": "Electronics",
#         "origin": "Tashkent",
#         "destination": "Moscow",
#         "weight_kg": "1200.50",
#         "volume_m3": "10.25",
#         "pickup_date": "2025-09-05",
#         "delivery_date": "2025-09-10",
#         "vehicle_type": "standard",
#         "special_requirements": "Handle with care",
#         "incoterms": "CIF",
#         "additional_notes": "Urgent delivery",
#         "status": "draft"
#     }
#     response = requests.post(url, json=data)
#     return response.status_code, response.json()
#
#
# # 🔹 GET (barcha buyurtmalarni olish)
# def get_orders():
#     url = f"{BASE_URL}/freight-orders/"
#     response = requests.get(url)
#     return response.status_code, response.json()
#
#
# # 🔹 GET (bitta buyurtmani olish)
# def get_order(order_id: int):
#     url = f"{BASE_URL}/freight-orders/{order_id}/"
#     response = requests.get(url)
#     return response.status_code, response.json()
#
#
# # 🔹 PUT (buyurtmani yangilash)
# def update_order(order_id: int):
#     url = f"{BASE_URL}/freight-orders/{order_id}/"
#     data = {
#         "cargo_description": "Updated Electronics",
#         "origin": "Tashkent",
#         "destination": "Berlin",
#         "weight_kg": "1500.00",
#         "volume_m3": "12.00",
#         "pickup_date": "2025-09-06",
#         "delivery_date": "2025-09-12",
#         "vehicle_type": "refrigerated",
#         "special_requirements": "Keep cool",
#         "incoterms": "FOB",
#         "additional_notes": "Updated order",
#         "status": "in_progress"
#     }
#     response = requests.put(url, json=data)
#     return response.status_code, response.json()
#
#
# # 🔹 DELETE (buyurtmani o‘chirish)
# def delete_order(order_id: int):
#     url = f"{BASE_URL}/freight-orders/{order_id}/"
#     response = requests.delete(url)
#     return response.status_code
#
# if __name__ == "__main__":
#     # 1. Yangi order yaratish
#     status, created = create_order()
#     print("CREATE:", status, created)
#
#     order_id = created.get("id")  # yangi order ID sini olish
#
#     # 2. Barcha orderlarni olish
#     status, orders = get_orders()
#     print("GET ALL:", status, orders)
#
#     # 3. Bitta orderni olish
#     if order_id:
#         status, order = get_order(order_id)
#         print("GET ONE:", status, order)
#
#         # 4. Orderni yangilash
#         status, updated = update_order(order_id)
#         print("UPDATE:", status, updated)
#
#         # 5. Orderni o‘chirish
#         # status = delete_order(order_id)
#         # print("DELETE:", status)

