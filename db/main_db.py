import sqlite3
from db import queries

db = sqlite3.connect("db/products_details.sqlite3")
cursor = db.cursor()

async def sql_create():
    if db:
        cursor.execute(queries.CREATE_ONLINE_STORE)
        cursor.execute(queries.CREATE_TABLE_PRODUCTS_DETAILS)
        cursor.execute(queries.CREATE_TABLE_COLLECTION_PRODUCTS)
        print("база данных подключена")

    db.commit()


async def sql_insert_oline_store(name_product, size, price, product_id, photo):
    cursor.execute(queries.CREATE_ONLINE_STORE, (name_product, size, price, product_id, photo))
    db.commit()
async def sql_insert_products_details(product_id, category, info_product):
    cursor.execute(queries.INSERT_INTO_PRODUCTS, (product_id, category, info_product))
    db.commit()

async def sql_insert_collection_products(product_id, collection):
    cursor.execute(queries.INSERT_INTO_COLLECTION_PRODUCTS, (product_id, collection))
    db.commit()