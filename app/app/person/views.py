from django.shortcuts import render

from typing import List

from django.views.generic import TemplateView

from app.person.models import Person


class PersonListView001(TemplateView):
    template_name = 'person/list-001.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 全件
        person_list: List[Person] = \
            Person.objects.all()[:10]

        # 大阪府だけ絞り込み
        person_list: List[Person] = \
            Person.objects.filter(prefecture__name = '大阪府')[:10]
        
        # # 北海道だけ絞り込み
        # person_list: List[Person] = \
        #     Person.objects.filter(prefecture__name = '北海道')[:10]

        # # 東京都だけ絞り込み
        # person_list: List[Person] = \
        #     Person.objects.filter(prefecture__name = '東京都')[:10]
            

        context['person_list'] = person_list

        return context

class PersonListView002(TemplateView):
    template_name = 'person/list-002.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        select_related_tables = [
            'prefecture',
            'prefecture__district',
            'sex',
        ]

        select_fields = [
            'id',
            'name',
            'name_kana',
            'sex__name',
            'telephone',
            'telephone_mobile',
            'mail_address',
            'zip_code',
            'prefecture__district__name',
            'prefecture__name',
            'address1',
            'address2',
            'birthday',
            
            'created_at',
            'updated_at',
        ]

        # # 全件
        # person_list: List[Person] = \
        #     Person.objects \
        #         .select_related(*select_related_tables) \
        #         .all() \
        #         .values(*select_fields)[:10]

        # 大阪府だけ絞り込み
        person_list: List[Person] = \
            Person.objects \
                .select_related(*select_related_tables) \
                .filter(prefecture__name = '大阪府') \
                .values(*select_fields)[:10]
        
        # # 北海道だけ絞り込み
        # person_list: List[Person] = \
        #     Person.objects \
        #         .select_related(*select_related_tables) \
        #         .filter(prefecture__name = '北海道') \
        #         .values(*select_fields)[:10]

        # # 東京都だけ絞り込み
        # person_list: List[Person] = \
        #     Person.objects \
        #         .select_related(*select_related_tables) \
        #         .filter(prefecture__name = '東京都') \
        #         .values(*select_fields)[:10]
            

        context['person_list'] = person_list

        return context
