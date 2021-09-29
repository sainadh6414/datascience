
use orders;

-- 7. Write a query to display carton id, (len*width*height) as carton_vol and identify the optimum 
-- carton (carton with the least volume whose volume is 
-- greater than the total volume of all items (len * width * height * product_quantity)) 
-- for a given order whose order id is 10006, Assume all items of an order are 
-- packed into one single cart OI9KIRTMEDFS,on (box). (1 ROW) 
-- [NOTE: CARTON TABLE]

SELECT 
    CARTON_ID,
    MIN(CARTON.LEN * CARTON.WIDTH * CARTON.HEIGHT) AS CARTON_VOLUME
FROM
    CARTON
WHERE
    (CARTON.LEN * CARTON.WIDTH * CARTON.HEIGHT) > (SELECT 
            SUM(PRODUCT.LEN * PRODUCT.WIDTH * PRODUCT.HEIGHT * ORDER_ITEMS.PRODUCT_QUANTITY)
        FROM
            ORDER_ITEMS,
            PRODUCT
        WHERE
            ORDER_ITEMS.ORDER_ID = 10006
                AND ORDER_ITEMS.PRODUCT_ID = PRODUCT.PRODUCT_ID);

-- 8. Write a query to display details (customer id,customer fullname,order id,product quantity) 
-- of customers who bought more than ten (i.e. total order qty) products per shipped order. 
-- (11 ROWS) [NOTE: TABLES TO BE USED - online_customer, order_header, order_items,]

SELECT 
    ONLINE_CUSTOMER.CUSTOMER_ID,
    CONCAT(ONLINE_CUSTOMER.CUSTOMER_FNAME,
            ' ',
            ONLINE_CUSTOMER.CUSTOMER_LNAME) CUSTOMER_NAME,
    ORDER_HEADER.ORDER_ID,
    SUM(ORDER_ITEMS.PRODUCT_QUANTITY) TOTAL_ORDER_QUANTITY
FROM
    ONLINE_CUSTOMER,
    ORDER_HEADER,
    ORDER_ITEMS
WHERE
    ONLINE_CUSTOMER.CUSTOMER_ID = ORDER_HEADER.CUSTOMER_ID
        AND ORDER_ITEMS.ORDER_ID = ORDER_HEADER.ORDER_ID
        AND ORDER_HEADER.ORDER_STATUS = 'Shipped'
GROUP BY ORDER_ITEMS.ORDER_ID
HAVING TOTAL_ORDER_QUANTITY > 10
ORDER BY TOTAL_ORDER_QUANTITY DESC;

-- 9. Write a query to display the order_id, customer id and customer 
-- full name of customers along with (product_quantity) as total quantity of products shipped 
-- for order ids > 10060. (6 ROWS) [NOTE: TABLES TO BE USED - online_customer, order_header, order_items]

SELECT 
    ORDER_HEADER.ORDER_ID,
    ONLINE_CUSTOMER.CUSTOMER_ID,
    CONCAT(ONLINE_CUSTOMER.CUSTOMER_FNAME,
            ' ',
            ONLINE_CUSTOMER.CUSTOMER_LNAME) CUSTOMER_NAME,
    SUM(ORDER_ITEMS.PRODUCT_QUANTITY) TOTAL_ORDER_QUANTITY
FROM
    ONLINE_CUSTOMER,
    ORDER_HEADER,
    ORDER_ITEMS
WHERE
    ONLINE_CUSTOMER.CUSTOMER_ID = ORDER_HEADER.CUSTOMER_ID
        AND ORDER_ITEMS.ORDER_ID = ORDER_HEADER.ORDER_ID
        AND ORDER_HEADER.ORDER_STATUS = 'Shipped'
        AND ORDER_HEADER.ORDER_ID > 10060
GROUP BY ORDER_ITEMS.ORDER_ID
ORDER BY TOTAL_ORDER_QUANTITY DESC;


-- 10. Write a query to display product class description ,total quantity (sum(product_quantity),Total 
-- value (product_quantity * product price) and 
-- show which class of products have been shipped highest(Quantity) to countries outside India other than USA? Also show the total value of those items. 
-- (1 ROWS)
-- [NOTE:PRODUCT TABLE,ADDRESS TABLE,ONLINE_CUSTOMER TABLE,ORDER_HEADER TABLE,ORDER_ITEMS TABLE,PRODUCT_CLASS TABLE]

SELECT 
    PRODUCT_CLASS.PRODUCT_CLASS_DESC,
    SUM(ORDER_ITEMS.PRODUCT_QUANTITY) TOTAL_QUANTITY,
    (ORDER_ITEMS.PRODUCT_QUANTITY * PRODUCT.PRODUCT_PRICE) TOTAL_VALUE
FROM
    PRODUCT,
    PRODUCT_CLASS,
    ORDER_HEADER,
    ORDER_ITEMS,
    ONLINE_CUSTOMER,
    ADDRESS
WHERE
    PRODUCT.PRODUCT_ID = ORDER_ITEMS.PRODUCT_ID
        AND ORDER_ITEMS.ORDER_ID = ORDER_HEADER.ORDER_ID
        AND ORDER_HEADER.CUSTOMER_ID = ONLINE_CUSTOMER.CUSTOMER_ID
        AND ADDRESS.ADDRESS_ID = ONLINE_CUSTOMER.ADDRESS_ID
        AND PRODUCT.PRODUCT_CLASS_CODE = PRODUCT_CLASS.PRODUCT_CLASS_CODE
        AND ORDER_HEADER.ORDER_STATUS = 'Shipped'
        AND ADDRESS.COUNTRY NOT IN ('India' , 'USA')
GROUP BY PRODUCT_CLASS_DESC
ORDER BY TOTAL_QUANTITY DESC
LIMIT 1;