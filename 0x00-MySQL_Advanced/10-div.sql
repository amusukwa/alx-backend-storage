-- SafeDiv function
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    DECLARE result INT;

    -- Check if b is equal to 0
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END;
//

DELIMITER ;
