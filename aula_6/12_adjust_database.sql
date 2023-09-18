-- Adiciona coluna supplier_id na tabela products
ALTER TABLE IF EXISTS products
    ADD COLUMN supplier_id integer;
    
-- Cria FK entre products.supplier_id e supplier.supplier_id
ALTER TABLE IF EXISTS products
    ADD CONSTRAINT supplier_id_fk FOREIGN KEY (supplier_id)
    REFERENCES suppliers (supplier_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

-- Remove registros da tabela suppliers
DELETE FROM suppliers WHERE supplier_id > 19;

-- Adiciona suppliers nos produtos
DO $$
DECLARE 
row record;
BEGIN
FOR row IN SELECT product_id FROM products LOOP
	UPDATE products 
	SET supplier_id = (SELECT FLOOR(random() * 19 + 1)) 
	WHERE product_id = row.product_id;
END LOOP;
END $$;