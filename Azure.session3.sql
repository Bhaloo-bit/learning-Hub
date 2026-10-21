SELECT *
FROM product;
SELECT product_id,
    product_name AS p_name,
    -- product_name AS "Product Nmae",
    stock_quantity
FROM product;
SELECT *
From customers;


SELECT DISTINCT country
FROM customers;

SELECT * 
FROM product
WHERE price > 200;

-- Give me products having stock qty > 0 and price < 150:
SELECT * FROM product
where stock_quantity > 0 
AND price > 150


-- Give me products having 0 as stock -qty  or price < 150

SELECT * 
FROM product
WHERE stock_quantity = 0
OR price < 150

-- Give me products which are not active

SELECT * FROM product
Where NOT is_active;


-- Give me product having price > 120 

SELECT * FROM product
Where price > 120 and price < 120

SELECT * FROM product
WHERE price BETWEEN 120 AND 200;  -- both end are inclusive 

SELECT * FROM categories;

--Give me product from electronics as well as books
SELECT * from product
WHERE category_id = 1
OR category_id = 2
OR category_id = 3;


SELECT * FROM product
WHERE category_id IN(1,3,4,5);


-- ! Give me product havinf product name 
-- ! Starting wiht 'Wireless'
-- ! Wireless headphones
-- ! Wireless mouse

INSERT INTO product
(product_name, price, stock_quantity, category_id)
VALUES
('wireless keyboard', 100, 21,1),
('wireless light keyboard', 150, 31,1),
('wireless mouse', 130, 11,1)



SELECT * FROM product
WHERE product_name LIKE 'wireless%';


-- GIVE me customers who does not have phone number

SELECT * FROM customers
WHERE phone IS NULL;

SELECT
    first_name,
    last_name,
    COALESCE(phone, 'Phone number unavaible'),
    COALESCE(city,'No city')
FROM customers


-- Give me product from cheapeast to expensice

SELECT * FROM product
ORDER BY pirce ASC ;-- to arrannge product in asscending order
-- for descendin DESC;

-- Give me product from cheap to exp price for each category


SELECT * FROM product
ORDER BY category_id, price;


-- ! Give me most expensive product

SELECT * FROM product
ORDER BY price DESC
LIMIT 10;

-- ! Pagination 

SELECT COUNT(*) FROM product;

SELECT * FROM product
ORDER BY product_id
LIMIT 5 
OFFSET 5

FE : page: 0, 10, 20

p: 1 OFFSET : 0
p: 2 OFFSET : 10
p: 3 OFFSET : 20

offset = (page-1) * LIMIT -- conveting user readable form to sql readanle qry

