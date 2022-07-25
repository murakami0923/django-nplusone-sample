from typing import Sequence
from django.core.management.base import BaseCommand

import csv
import os

from django.conf import settings

from app.master.models import Sex, Prefecture
from app.person.models import Person
from app.common import common_utils as util

CSV_FILE＿NAME_HEAD = 'personal_infomation-{}.csv'
SKIP_ROWS = 1

class Command(BaseCommand):
    help = "全データ削除(TRUNCATE)を開始"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        Person.objects.all().delete()
        Prefecture.objects.all().delete()
        Sex.objects.all().delete()

        print('全データを削除しました。')
