from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

import logging

from airlines.models import Airline
from core.groups import Roles

GROUPS_PERMISSIONS = {}

# permissions inheritance
GROUPS_PERMISSIONS[Roles.USER] = {
}
GROUPS_PERMISSIONS[Roles.MANAGER] = {
    **GROUPS_PERMISSIONS[Roles.USER],
    Airline: ['add', 'change', 'delete', 'view']
}
GROUPS_PERMISSIONS[Roles.ADMIN] = {
    **GROUPS_PERMISSIONS[Roles.MANAGER],
}


class Command(BaseCommand):
    help = 'Init groups and permissions'

    def handle(self, *args, **kwargs):
        for group_name in GROUPS_PERMISSIONS:
            group, created = Group.objects.get_or_create(name=group_name)
            logging.info(f'Group {group_name} created')
            for model in GROUPS_PERMISSIONS[group_name]:
                for prefix in GROUPS_PERMISSIONS[group_name][model]:
                    codename = f'{prefix}_{model._meta.model_name}'
                    name = f'Can {prefix} {model._meta.model_name}'
                    content_type = ContentType.objects.get_for_model(model)
                    permission, created = Permission.objects.get_or_create(
                        defaults={
                            name: name,
                            content_type: content_type
                        },
                        codename=codename
                    )
                    group.permissions.add(permission)
                    logging.info(f'Permission {codename} created and added to group {group_name}')


