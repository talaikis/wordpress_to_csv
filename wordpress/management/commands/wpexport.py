from os.path import join, dirname
import csv

from django.core.management.base import BaseCommand
from django.conf import settings

from wordpress.models import Post
import wordpress


class Command(BaseCommand):

    def handle(self, *args, **options):
        BASE_DIR = dirname(dirname(dirname(dirname(__file__))))
        path_to_export = join(BASE_DIR, "exports")

        fieldnames = ['date', 'title', 'content', 'content_filtered']

        rows = []
        for post in Post.objects.published():
            val = {"title": post.title, "content": post.content,
                "content_filtered": post.content_filtered,
                "date": post.post_date}
            rows.append(val)

        file_name = join(path_to_export, settings.DATABASES["default"]["NAME"]+"_posts.csv")
        with open(file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            for row in rows:
                writer.writerow(row)
