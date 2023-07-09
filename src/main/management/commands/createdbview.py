from django.core.management import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Create an implicit view for the database'
    
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    """
                        CREATE OR REPLACE VIEW `Member Contributions` AS
                        SELECT
                            `m`.`id` AS `id`,
                            `m`.`first_name` AS `first_name`,
                            `m`.`last_name` AS `last_name`,
                            `m`.`email` AS `email`,
                            SUM(`bd`.`amount`) AS `Contribution`,
                            COUNT(`bd`.`id`) AS `Transaction_Number`
                        FROM
                            (`BalanceDetails` `bd` JOIN
                                ((`Member` `m` JOIN
                                `LinkedTransaction` `ltr` ON((`ltr`.`member_id_id` = `m`.`id`))) JOIN
                                `Transaction` `tr` ON((`tr`.`id` = `ltr`.`transaction_bank_reference_id`))))
                        WHERE
                            (`tr`.`balance_details_id_id` = `bd`.`id`)
                        GROUP BY
                            `m`.`id`
                        ;
                    """
                )
                
                print("View created successfully")
            except Exception as e:
                print(e)
                print("Error creating the view")
