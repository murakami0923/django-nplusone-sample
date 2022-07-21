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
    help = "個人情報登録"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        for file_num in range(1, 11):
            csv_dir_abs_path = settings.ROOT_DIR
            csv_file_name = CSV_FILE＿NAME_HEAD.format(str(file_num).zfill(2))
            csv_file_abs_path = os.path.join(csv_dir_abs_path, 'data', csv_file_name,)
            print(csv_file_abs_path)
            
            csv_file = open(csv_file_abs_path, 'r', encoding='utf8', errors='', newline='')

            #リスト形式で読み取る
            f = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"', skipinitialspace=True)

            i = 0

            for row in f:
                if i < SKIP_ROWS:
                    i += 1
                    continue

                num, \
                name, \
                name_kana, \
                sex_name, \
                telephone, \
                telephone_mobile, \
                mail_address, \
                zip_code, \
                prefecture_name, \
                csv_address1, \
                csv_address2, \
                csv_address3, \
                csv_address4, \
                birthday \
                = row

                sex: Sex = Sex.objects.filter(name=sex_name).first()
                prefecture: Prefecture = Prefecture.objects.filter(name=prefecture_name).first()

                if prefecture is None:
                    print('[SKIP] prefecture is None (row : {}, name : {})'.format(i, prefecture_name))
                    continue

                now = util.now()

                person: Person = Person(
                    name = name,                            # name = models.CharField('氏名', max_length=128)
                    name_kana = name_kana,                  # name_kana = models.CharField('氏名（カタカナ）', max_length=128)
                    sex = sex,                              # sex = models.ForeignKey(Sex, on_delete=models.PROTECT)
                    telephone = telephone,                  # telephone = models.CharField('電話番号', max_length=128)
                    telephone_mobile = telephone_mobile,    # telephone_mobile = models.CharField('携帯電話', max_length=128)
                    mail_address = mail_address,            # mail_address = models.CharField('メールアドレス', max_length=255)
                    zip_code = zip_code,                    # zip_code = models.CharField('郵便番号', max_length=32)
                    prefecture = prefecture,                # prefecture = models.ForeignKey(Prefecture, on_delete=models.PROTECT)
                    address1 = '{}{}{}'.format(csv_address1, csv_address2, csv_address3,),  # address1 = models.CharField('住所1', max_length=255)
                    address2 = csv_address4,                # address2 = models.CharField('住所1', max_length=255)
                    birthday = util.convert_date_from_str(birthday),    # birthday = models.DateField('生年月日')
                    
                    created_at = now,                       # created_at = models.DateTimeField()
                    updated_at = now,                       # updated_at = models.DateTimeField()
                )

                person.save()

                i += 1

        print('個人情報を登録しました。')
