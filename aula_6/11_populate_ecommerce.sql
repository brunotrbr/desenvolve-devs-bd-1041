DO $$
DECLARE 
-- single variables
row record;
prod products;
product_id int;
product_number int;
quantity int;
temp_amount int;
-- arrays
orders_to_add orders[] := '{}';
orders_to_update orders[] := '{}';
product_array products[] := '{}';
used_products INT[] := '{}';

BEGIN
SELECT ARRAY_AGG(pr) INTO product_array FROM products pr;
FOR row IN SELECT order_id FROM orders LOOP
	FOR i IN 1..(SELECT FLOOR(random() * 10 + 1)) LOOP
		SELECT FLOOR(random() * 1231 + 1) INTO product_id;
        WHILE product_id = ANY(used_products) LOOP
        	SELECT FLOOR(random() * 1231 + 1) INTO product_id;
       	END LOOP;
        used_products := ARRAY_APPEND(used_products, product_id);
    END LOOP;
	
	temp_amount := 0;
	FOREACH product_number IN ARRAY used_products LOOP
		prod := product_array[product_number];
		quantity := (SELECT FLOOR(random() * 10 + 1));
		INSERT INTO order_items (order_id, product_id, quantity, price) 
		VALUES(row.order_id, prod.product_id, quantity, prod.price);
		temp_amount := temp_amount + (prod.price * quantity);
	END LOOP;
	UPDATE orders SET total_amount = temp_amount WHERE order_id = row.order_id;
	used_products := '{}';
END LOOP;
END $$;