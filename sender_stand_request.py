import configuration
import requests
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def get_log():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})


# Metodo obtener tabla
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


# Metodo Crear Nuevo Usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)


# Metodo buscar kits por sus productos
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=data.product_ids,  # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.


"""response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())"""

"""response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())"""

"""response = get_users_table()
print(response.status_code)
print(response.headers)"""
