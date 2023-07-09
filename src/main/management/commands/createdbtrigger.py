from django.core.management import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Create an implicit trigger for the database'
    
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            try:
                # First drop the trigger if it exists
                cursor.execute(" DROP TRIGGER IF EXISTS `UpdatedLinkedTransactionsDetails`; ")
                cursor.execute(
                    """
                    CREATE TRIGGER `UpdatedLinkedTransactionsDetails`
                    AFTER UPDATE ON `Transaction`
                    FOR EACH ROW
                    BEGIN
                        IF NEW.category_id_id <> OLD.category_id_id OR NEW.custom_description <> OLD.custom_description THEN
                              -- Update the corresponding linked transactions
                              CALL `UpdateDetailsInLinkedTransactions`(NEW.id, NEW.category_id_id, NEW.custom_description);
                        END IF;
                    END
                    """
                )
                print("Trigger created successfully")
            except Exception as e:
                print(e)
                print("Error creating the trigger")
