-- 2.1. Сумма заказов по каждому клиенту
SELECT c.name, SUM(oi.quantity * p.price) AS total
FROM clients c
JOIN orders o ON c.id = o.client_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY c.name;


-- 2.2. Количество дочерних категорий первого уровня
SELECT parent_id, COUNT(*) AS child_count
FROM categories
WHERE parent_id IS NOT NULL
GROUP BY parent_id;


-- 2.3.1. Топ-5 самых покупаемых товаров за последний месяц
SELECT p.name AS product_name,
       c2.name AS top_category,
       SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.id
JOIN orders o ON oi.order_id = o.id
JOIN categories c ON c.id = p.category_id
LEFT JOIN categories c2 ON c2.id = c.id AND c2.parent_id IS NULL
WHERE o.created_at >= date('now', '-1 month')
GROUP BY p.id, c2.name
ORDER BY total_sold DESC
LIMIT 5;
-- Для оптимизации с данной схемой БД, я бы предложил использовать индексы.
-- Да, индексы при каждой новой вставке или обновлении данных будут перезаписываться
-- У нас будет немного дольше выполняться запрос на вставку или обновление данных, но гораздо быстрее
-- будут выполняться запросы по аналитике
-- А так же использовать Партиционирование в базе данных, например по таблице orders
-- на каждый месяц к примеру, таким образом это резко снижает объём данных, которые нужно просмотреть.
-- Таким образом: индексы дают быстрый доступ внутри партиции,
-- А партиционирование гарантирует, что при отчётах обрабатывается только актуальная часть данных, а не вся таблица за годы.