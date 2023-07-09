from django.core.management import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Create an implicit stored procedure for the database'
    
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            try:
                # First drop the procedure if it exists
                cursor.execute(
                    """
                        DROP PROCEDURE IF EXISTS `UpdateDetailsInLinkedTransactions`;
                    """
                )
                # Then create the procedure
                cursor.execute(
                    """
                        -- DELIMITER $$
                        --
                        -- Procedures
                        --
                        CREATE DEFINER=`root`@`%` PROCEDURE `UpdateDetailsInLinkedTransactions` (IN `member_id` INT, IN `new_category_id` INT, IN `new_description` VARCHAR(255)) BEGIN
                            DECLARE tr_id_var INT;
                            DECLARE category_id_var INT DEFAULT 0;
                            DECLARE description_var VARCHAR(255) DEFAULT NULL;
                            
                                    -- Declare a bool to know when we reach the end of the cursor
                            DECLARE finished INT DEFAULT 0;
                         
                            -- Create a cursor to iterate throw all the transactions
                            DECLARE curs CURSOR FOR
                                    SELECT tr.`id`, tr.`category_id_id`, tr.`custom_description`
                                    FROM `Transaction` tr
                                    INNER JOIN `LinkedTransaction` ltr ON tr.`id` = ltr.`transaction_bank_reference_id`
                                    WHERE ltr.`member_id_id` = member_id
                                    ORDER BY tr.`custom_description`;
                           
                            DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
                            
                            
                            -- SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
                            SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
                            START TRANSACTION;
                                -- Open the cursor
                                OPEN curs;
                        
                                -- Get the first row of data
                                FETCH curs INTO tr_id_var, category_id_var, description_var;
                        
                                WHILE finished = 0 DO
                                    -- If there is a description
                                    IF new_description IS NOT NULL THEN
                                        UPDATE `Transaction`
                                        SET `custom_description` = new_description
                                        WHERE id = tr_id_var;
                                    END IF;
                        
                                    -- If there is a category
                                    IF new_category_id IS NOT NULL THEN
                                        UPDATE `Transaction`
                                        SET `category_id_id` = new_category_id
                                        WHERE id = tr_id_var;
                                    END IF;
                                
                                    -- Get the next row
                                    FETCH curs INTO tr_id_var, category_id_var, description_var;
                                END WHILE;
                              
                                -- Close the cursor
                                CLOSE curs;
                            COMMIT;
                         
                        END
                        -- $$
                        -- DELIMITER ;
                    """
                )
                print("Stored Procedure created successfully")
            except Exception as e:
                print(e)
                print("Error creating the stored procedure")
