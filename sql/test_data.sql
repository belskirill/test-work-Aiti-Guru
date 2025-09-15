-- Тестовые данные


INSERT INTO categories (name) VALUES ('Electronics');
INSERT INTO categories (name, parent_id) VALUES ('Phones', 1);
INSERT INTO categories (name, parent_id) VALUES ('Laptops', 1);


INSERT INTO products (name, quantity, price, category_id) VALUES ('iPhone 14', 10, 999.99, 2);
INSERT INTO products (name, quantity, price, category_id) VALUES ('MacBook Air', 5, 1299.00, 3);


INSERT INTO clients (name, address) VALUES ('Alice', 'New York');
INSERT INTO clients (name, address) VALUES ('Bob', 'Los Angeles');


INSERT INTO orders (client_id) VALUES (1);
INSERT INTO orders (client_id) VALUES (2);


INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 1, 2);
INSERT INTO order_items (order_id, product_id, quantity) VALUES (2, 2, 1);
