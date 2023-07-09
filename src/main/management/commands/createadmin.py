from django.core.management import BaseCommand

from main.models import User


class Command(BaseCommand):
    help = 'Create admin account if it does not exist'
    
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = 'admin'
            first_name = 'admin'
            last_name = 'admin'
            email = 'admin@gmail.com'
            password = 'admin'
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(email=email, first_name=first_name, last_name=last_name, username=username, password=password)
            admin.is_active = True
            admin.is_superuser = True
            admin.is_staff = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
