from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Blog


@receiver(post_save, sender=Blog)
def create_blog(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    update_fields = kwargs['update_fields']
    print(update_fields)
    if created:
        print('Blog created')
    else:
        print('Blog updated')

