-- ! Give me all orders icluding empoyrr details of the employee who procseed 
-- ! that orders
-- ! only  include orders punched by the employees
-- ! Alieas - AS 
SELECT * 
FROM orders AS o
INNER JOIN employees AS e ON e.employee_id = o.employee_id;



-- give me all orders and include employee details of employee who procesed
-- !  that order aand if it is directly coming form customer keep employee
-- ! details empty

-- left join

SELECT 
o.status, o.order_id,
e.email, e.first_name
FROM orders as o
    LEFT JOIN employees as e ON o.employee_id = e.employee_id