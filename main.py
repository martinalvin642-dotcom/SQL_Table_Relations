# CodeGrade step0
# Run this cell without changes

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# CodeGrade step1
# Replace None with your code
 # CodeGrade step1
df_boston = pd.read_sql("""SELECT employees.firstname, employees.lastname
                            FROM employees
                            JOIN offices ON employees.officecode = offices.officecode
                            WHERE offices.city = 'Boston'""", conn)


# CodeGrade step2
# Replace None with your code
df_zero_emp = pd.read_sql("""SELECT offices.officecode, offices.city, offices.country
                           FROM offices
                           LEFT JOIN employees ON offices.officecode = employees.officecode
                           WHERE employees.officecode IS NULL;""", conn)

# CodeGrade step3
# Replace None with your code
# CodeGrade step3
df_employee = pd.read_sql("""SELECT employees.firstname, employees.lastname, offices.city, offices.state
                              FROM employees
                              LEFT JOIN offices ON employees.officecode = offices.officecode
                              ORDER BY employees.firstname, employees.lastname;""", conn)


# CodeGrade step4
# Replace None with your code
df_contacts =pd.read_sql("""SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber
FROM customers c
LEFT JOIN orders o ON c.customerNumber = o.customerNumber
WHERE o.customerNumber IS NULL
ORDER BY c.contactLastName ASC;""",conn)

# CodeGrade step5
# Replace None with your code
df_payment =pd.read_sql("""SELECT c.contactFirstName, c.contactLastName, p.amount, p.paymentDate
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
ORDER BY CAST(p.amount AS DECIMAL) DESC;

""",conn)

# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql("""SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) AS number_of_customers
FROM employees e
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY e.employeeNumber, e.firstName, e.lastName
HAVING AVG(c.creditLimit) > 90000
ORDER BY number_of_customers DESC;""",conn)

# CodeGrade step7
# Replace None with your code
df_product_sold = pd.read_sql("""SELECT p.productName, 
       COUNT(o.orderNumber) AS numorders,
       SUM(od.quantityOrdered) AS totalunits
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
JOIN orders o ON od.orderNumber = o.orderNumber
GROUP BY p.productName
ORDER BY totalunits DESC;""",conn)

# CodeGrade step8
# Replace None with your code
df_total_customers =pd.read_sql("""SELECT p.productName, 
       p.productCode,
       COUNT(DISTINCT o.customerNumber) AS numpurchasers
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
JOIN orders o ON od.orderNumber = o.orderNumber
GROUP BY p.productName, p.productCode
ORDER BY numpurchasers DESC;;""",conn)

# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql("""SELECT o.officeCode, o.city,
       COUNT(c.customerNumber) AS n_customers
FROM offices o
JOIN employees e ON o.officeCode = e.officeCode
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY o.officeCode, o.city
ORDER BY n_customers DESC;""",conn)

# CodeGrade step10
# Replace None with your code
df_under_20 = pd.read_sql("""WITH low_reach_products AS (
    SELECT p.productCode
    FROM products p
    JOIN orderdetails od ON p.productCode = od.productCode
    JOIN orders o ON od.orderNumber = o.orderNumber
    GROUP BY p.productCode
    HAVING COUNT(DISTINCT o.customerNumber) < 20
)
SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, 
       of.city, of.officeCode
FROM employees e
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN low_reach_products lrp ON od.productCode = lrp.productCode
JOIN offices of ON e.officeCode = of.officeCode;
                          """,conn)

# Run this cell without changes

conn.close()
