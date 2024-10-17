-- Function to divide two number
DELIMITER $$

CREATE FUNCTION SafeDiv (
    num1 INT,
    num2 INT
)
RETURNS INT
DETERMINISTIC
BEGIN
    IF num2 = 0 THEN
       RETURN 0;
    ELSE
        RETURN num1 / num2;
    END IF;
END $$

DELIMITER ;
