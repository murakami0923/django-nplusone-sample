from django.shortcuts import render

from typing import List

from django.views.generic import TemplateView

from app.person.models import Person


class PersonListView001(TemplateView):
    template_name = 'person/list-001.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # # 全件から先頭100件
        # person_list: List[Person] = \
        #     Person.objects.all()[:100]

        # # 都道府県に「京都」を含むだけ絞り込み（「東京都」と「京都府」がヒット）
        # # -> 先頭100件
        # person_list: List[Person] = \
        #     Person.objects.filter(prefecture__name__contains = '京都')[:100]
        # -> 1001行目～1100行目
        person_list: List[Person] = \
            Person.objects.filter(prefecture__name__contains = '京都')[1000:1100]
        
        # # 北海道だけ絞り込み
        # person_list: List[Person] = \
        #     Person.objects.filter(prefecture__name = '北海道')[:100]

        # # 東京都だけ絞り込み
        # person_list: List[Person] = \
        #     Person.objects.filter(prefecture__name = '東京都')[:100]
            

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

        # # 全件から先頭100件
        # person_list: List[Person] = \
        #     Person.objects \
        #         .select_related(*select_related_tables) \
        #         .all() \
        #         .values(*select_fields)[:100]

        # 都道府県に「京都」を含むだけ絞り込み（「東京都」と「京都府」がヒット）
        # # -> 先頭100件
        # person_list: List[Person] = \
        #     Person.objects \
        #         .select_related(*select_related_tables) \
        #         .filter(prefecture__name__contains = '京都') \
        #         .values(*select_fields)[:100]
        # -> 1001行目～1100行目
        person_list: List[Person] = \
            Person.objects \
                .select_related(*select_related_tables) \
                .filter(prefecture__name__contains = '京都') \
                .values(*select_fields)[1000:1100]
        
        # # 北海道だけ絞り込み
        # person_list: List[Person] = \
        #     Person.objects \
        #         .select_related(*select_related_tables) \
        #         .filter(prefecture__name = '北海道') \
        #         .values(*select_fields)[:100]

        # # 東京都だけ絞り込み
        # person_list: List[Person] = \
        #     Person.objects \
        #         .select_related(*select_related_tables) \
        #         .filter(prefecture__name = '東京都') \
        #         .values(*select_fields)[:100]
            

        context['person_list'] = person_list

        return context
