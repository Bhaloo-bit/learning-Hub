-- ! College : 5 students
-- ! 5 LPA, 10, 5, 10, 15
-- ! what is an average CTC of the colleges
-- ! total CTC across students / number of students
-- !  5 + 10 + 5 + 10 + 15 / 5
-- !  9 LPA -> Average CTA of my college
-- ! totalCTC - 45 LPA

-- ! I had 5 entires on student level
-- ? I reduced those 5 entires in a single collge level entry

-------------------------------------

-- give me total count customere on our paltform
-- SQL Aggregate funciton


SELECT * FROM customers;
SELECT COUNT(*) AS customer_Count
COUNT(phone) as cust_with_phone_numbers -- count only not null entry 
 FROM customers;


SELECT COUNT(DISTINCT country) from customers;

---!  give me total revenue across all the orders

SELECT
    order_item_id,
    quantity,
    unit_price,
    quantity * unit_price as total_selling_value
FROM order_items;

SELECT SUM(quantity*unit_price) as total_revenue from order_items;

-- ! give average price of product across product

SELECT
    ROUND(AVG(price),2) as avg_price
from product;

-- ! Give me min price and max price across all product 

SELECT * FROM product ORDER BY PRICE ASC;
SELECT * FROM product ORDER BY PRICE DESC;
SELECT MIN(price ) as minimun_price , MAX(price) as maximun price
from product;


-- used most of the time

SELECT 
    COUNT(*) as toatal_product,
    ROUND(AVG(price),2) as average_price
    MIN(pirce) as minimun_price
    MAX(pirce) as maximum_price
    SUm(Stock_quantity) as total_stock
FROM product;



-- ! give me total number of products in each catogery

SELECT * FROM product;


SELECT COUNT(*) FROM product;

SELECT category_id, COUNT(*)
FROM product
GROUP BY category_id


-- ! give me total number of active and inactive 
-- ! proudcts in each category
--  including catogory name in the result
SELECT category_id, is_active, COUNT(*)
FROM product
GROUP BY category_id, is_active;

SELECT
    p.category_id,
    c.category_name,
    COUNT(*)
FROM product as p
LEFT JOIN catogeries as c on c.category_id = p.category_id
GROUP BY p.category_id, c.category_name

-- Give me total numebr of product in each category
-- ! and give me categories having > 5 products

SELECT category_id, count(*)
FROM product
GROUP BY category_id
having count(*) > 5;


-- ! Find departments having more than one employee
-- ! where their combined salary of whole department exceeds 200000 rupees

SELECT * FROM employees;

SELECT 
    department_id,
    COUNT(*)
FROM employee
GROUP BY department_id;



-- ! Give me all the customer having at least one cancelled order
SELECT * FROM customers;

SELECT * FROM orders;

-- ! subquery is nothing but nested query 
SELECT * FROM customers
WHERE customer_id IN (
    SELECT customer_id FROM orders WHERE status = 'cancelled'

);


-- Give all the product which are having 
-- price > average price across all products

-- ! pi-100, p2-200, p3= 10000 , p3 = 200