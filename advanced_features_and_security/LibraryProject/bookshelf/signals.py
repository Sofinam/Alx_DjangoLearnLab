from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Book

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name == "relationship_app":  # Ensuring it only runs for this app
        content_type = ContentType.objects.get_for_model(Book)

        # Define groups
        groups_permissions = {
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Viewers": ["can_view"],
        }

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)

            for perm in permissions:
                permission = Permission.objects.get(codename=perm, content_type=content_type)
                group.permissions.add(permission)
