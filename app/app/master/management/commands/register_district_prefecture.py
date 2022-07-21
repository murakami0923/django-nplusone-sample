from typing import Sequence
from django.core.management.base import BaseCommand

import csv
import os

from django.conf import settings

from app.master.models import District, Prefecture
from app.common import common_utils as util

CSV_FILE＿NAME = 'prefecture.csv'
SKIP_ROWS = 1

class Command(BaseCommand):
    help = "地方・都道府県マスタ登録"

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
        prev_district_name: str = None
        district: District = None

        for row in f:
            if i < SKIP_ROWS:
                i += 1
                continue

            district_sequence, district_name, prefecture_sequence, prefecture_name = row

            now = util.now()

            if prev_district_name != district_name:
                district: District = District(
                    sequence = district_sequence,
                    name = district_name,
                    created_at = now,
                    updated_at = now,
                )

                district.save()

                prev_district_name = district_name
            
            prefecture: Prefecture = Prefecture(
                district = district,
                sequence = prefecture_sequence,
                name = prefecture_name,
                created_at = now,
                updated_at = now,
            )

            prefecture.save()

            print('{} - {}'.format(district, prefecture))

            i += 1

        print('地方・都道府県マスタを登録しました。')
