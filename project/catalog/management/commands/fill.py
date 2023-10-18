from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Вода', 'description': ' Вода без газа'},
            {'name': 'Сухофрукты', 'description': 'Сушоные фрукты'},
            {'name': 'Сладости', 'description': 'Сладости с добавлением сахара'},
            {'name': 'Фрукты', 'description': 'Фрукты полезны'},
        ]

        # for category_item in category_list:
        #     Category.objects.create(**category_item)


        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))
        Category.objects.bulk_create(category_for_create)
