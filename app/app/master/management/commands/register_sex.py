from django.core.management.base import BaseCommand

import csv
import os

from django.conf import settings

from app.master.models import Sex
from app.common import common_utils as util

CSV_FILE＿NAME = 'sex.csv'
SKIP_ROWS = 1

class Command(BaseCommand):
    help = "性別マスタ登録"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        csv_dir_abs_path = settings.ROOT_DIR
        csv_file_abs_path = os.path.join(csv_dir_abs_path, 'data', CSV_FILE＿NAME,)

        csv_file = open(csv_file_abs_path, 'r', encoding='utf8', errors='', newline='')

        #リスト形式で読み取る
        f = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"', skipinitialspace=True)

        i = 0
        for row in f:
            if i < SKIP_ROWS:
                i += 1
                continue

            sequence, name = row

            now = util.now()

            sex: Sex = Sex(
                name = name,
                sequence = sequence,
                created_at = now,
                updated_at = now
            )

            sex.save()
            print(str(sex))

            i += 1

        print('性別マスタを登録しました。')