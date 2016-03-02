filenames_for_testing = """индексы цен производителей промышленных товаров.xlsm
индексы цен производителей на реализованную сельскохозяйственн продукцию.xls
индексы цен производителей cтроительной продукции.xlsx
индексы цен (тарифов) на грузовые перевозки.xls
цены на первичном и вторичном рынках жилья.xls"""

# must use 'sheet' if more than 1 sheet in Excel workbook

source_definitions = [
{   'varname':'PPI_PROM_ytd', 
     'folder':'11 цены производителей', 
   'filename':'индексы цен производителей промышленных товаров.xlsm',
      'sheet':'пром.товаров',
     'anchor':'B5', 'anchor_value': 96.6}
     
, { 'varname':'PPI_CONSTR_ytd', 
     'folder':'11 цены производителей', 
   'filename':'индексы цен производителей промышленных товаров.xlsm',
      'sheet':'строит.продукция',
     'anchor':'B5', 'anchor_value': 99.4}

#### MUST CHANGE
     
, { 'varname':'PPI_AGRO_ytd', 
     'folder':'11 цены производителей', 
   'filename':'индексы цен производителей на реализованную сельскохозяйственн продукцию.xls',
      'sheet':'пром.товаров',
     'anchor':'B5', 'anchor_value': 99.4}
     
, {   'varname':'PPI_rog', 
     'folder':'11 цены производителей', 
   'filename':'цены на первичном и вторичном рынках жилья.xls',
      'sheet':'пром.товаров',
     'anchor':'B5'
     
 , {'varname':'PPI_rog', 
     'folder':'11 цены производителей', 
   'filename':'цены на первичном и вторичном рынках жилья.xls',
      'sheet':'пром.товаров',
     'anchor':'B5'     
     }
     ]
     
#### END of MUST CHANGE

sidebar_doc = """Российская Федерация 1
Центральный федеральный округ
Белгородская область
Брянская область
Владимирская область
Воронежская область
Ивановская область
Калужская область
Костромская область
Курская область
Липецкая область
Московская область  2
Орловская область
Рязанская область
Смоленская область
Тамбовская область
Тверская область
Тульская область
Ярославская область
г.Москва  2
Северо-Западный федеральный округ
Республика Карелия
Республика Коми
Архангельская область
в том числе               Ненецкий авт.округ
Архангельская область без авт. округа 3
Вологодская область
Калининградская область
Ленинградская область
Мурманская область
Новгородская область
Псковская область
г.Санкт-Петербург
Южный                   федеральный округ 4
Республика Адыгея
Республика Калмыкия
Краснодарский край
Астраханская область
Волгоградская область
Ростовская область
Северо-Кавказский федеральный округ
Республика Дагестан
Республика Ингушетия
Кабардино-Балкарская Республика
Карачаево-Черкесская Республика
Республика Северная  Осетия - Алания
Чеченская Республика
Ставропольский край
Приволжский               федеральный округ
Республика Башкортостан
Республика Марий Эл
Республика Мордовия
Республика Татарстан
Удмуртская Республика
Чувашская Республика
Пермский край
Кировская область
Нижегородская область
Оренбургская область
Пензенская область 
Самарская область
Саратовская область
Ульяновская область
Уральский             федеральный округ
Курганская область
Свердловская область
Тюменская область
в том числе:                     Ханты-Мансийский       авт. округ - Югра
Ямало-Ненецкий             авт. округ
Тюменская область без авт. округов 3
Челябинская область
Сибирский           федеральный округ
Республика Алтай
Республика Бурятия
Республика Тыва
Республика Хакасия
Алтайский край
Забайкальский край
Красноярский край
Иркутская область
Кемеровская область
Новосибирская область  
Омская область
Томская область
Дальневосточный федеральный округ
Республика Саха (Якутия)
Камчатский край
Приморский край
Хабаровский край
Амурская область
Магаданская область
Сахалинская область
Еврейская авт.область
Чукотский авт.округ
Крымский федеральный округ
Республика Крым
г. Севастополь"""

# (1) truncated 'федеральный округ' and whitespace around it
# (2) truncated region name with whitespaces or many words
testable_sidebar_doc = """Российская Федерация
Центральный
Белгородская область
Брянская область
Владимирская область
Воронежская область
Ивановская область
Калужская область
Костромская область
Курская область
Липецкая область
Московская область
Орловская область
Рязанская область
Смоленская область
Тамбовская область
Тверская область
Тульская область
Ярославская область
г.Москва
Северо-Западный
Республика Карелия
Республика Коми
Архангельская область
Ненецкий
Архангельская область без авт. округа
Вологодская область
Калининградская область
Ленинградская область
Мурманская область
Новгородская область
Псковская область
г.Санкт-Петербург
Южный
Республика Адыгея
Республика Калмыкия
Краснодарский край
Астраханская область
Волгоградская область
Ростовская область
Северо-Кавказский
Республика Дагестан
Республика Ингушетия
Кабардино-Балкарская Республика
Карачаево-Черкесская Республика
Осетия - Алания
Чеченская Республика
Ставропольский край
Приволжский
Республика Башкортостан
Республика Марий Эл
Республика Мордовия
Республика Татарстан
Удмуртская Республика
Чувашская Республика
Пермский край
Кировская область
Нижегородская область
Оренбургская область
Пензенская область 
Самарская область
Саратовская область
Ульяновская область
Уральский
Курганская область
Свердловская область
Тюменская область
Ханты-Мансийский
Ямало-Ненецкий
Тюменская область
Челябинская область
Сибирский
Республика Алтай
Республика Бурятия
Республика Тыва
Республика Хакасия
Алтайский край
Забайкальский край
Красноярский край
Иркутская область
Кемеровская область
Новосибирская область
Омская область
Томская область
Дальневосточный
Республика Саха (Якутия)
Камчатский край
Приморский край
Хабаровский край
Амурская область
Магаданская область
Сахалинская область
Еврейская авт.область
Чукотский авт.округ
Крымский
Республика Крым
г. Севастополь"""

actual_sidebar_list = sidebar_doc.split("\n")
testable_region_names = testable_sidebar_doc.split("\n")


# important data check - may check as 'tr' in 'ar'
for ar, tr in zip(actual_sidebar_list, testable_region_names):
    # print(ar, "=", tr)
    assert tr in ar

testable_district_names  = ['Центральный', 'Северо-Западный', 'Южный', 'Северо-Кавказский', 
                            'Приволжский', 'Уральский', 'Сибирский', 'Дальневосточный', 'Крымский']
assert len(testable_district_names) == 9

RF = "Российская Федерация"