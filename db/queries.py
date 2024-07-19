CREATE_ONLINE_STORE = """
CREATE TABLE IF NOT EXISTS online_store(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id INTEGER,
    photo TEXT
)
"""

INSERT_INTO_STORE = """
INSERT INTO online_store(name_product, size, price, product_id, photo)
VALUES(?, ?, ?, ?, ?)
"""

CREATE_TABLE_PRODUCTS_DETAILS = """
CREATE TABLE IF NOT EXISTS products_details(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    category VARCHAR(255),
    info_product VARCHAR(255),
    FOREIGN KEY(product_id) REFERENCES online_store(id)
)
"""

INSERT_INTO_PRODUCTS = """
INSERT INTO products_details (product_id, category, info_product)
VALUES(?, ?, ?)
"""

CREATE_TABLE_COLLECTION_PRODUCTS = """
CREATE TABLE IF NOT EXISTS collection_products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    collection VARCHAR(255),
    FOREIGN KEY(product_id) REFERENCES online_store(id)
)
"""

INSERT_INTO_COLLECTION_PRODUCTS = """
INSERT INTO collection_products (product_id, collection)
VALUES(?, ?)
"""
