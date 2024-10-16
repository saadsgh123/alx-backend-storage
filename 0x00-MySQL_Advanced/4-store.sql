-- Change the delimiter to $$
DELIMITER $$

-- Create the trigger
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END; $$

-- Reset the delimiter back to semicolon
DELIMITER ;
