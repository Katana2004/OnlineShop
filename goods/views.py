from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'OnlineShop - Каталог',
        'goods': [
                {
                    'image': 'deps/images/goods/set of tea table and three chairs.jpg',
                    'name': 'Умный телевизор Samsung QE55QN85A',
                    'description': 'Телевизор с диагональю 55 дюймов и разрешением 4K. Он оснащен технологией QLED,'
                                   ' которая обеспечивает яркие и насыщенные цвета, а также HDR, что позволяет '
                                   'увидеть больше деталей на экране.',
                    'price': 1500.00
                },
                {
                    'image': 'deps/images/goods/set of tea table and two chairs.jpg',
                    'name': 'Кофемашина DeLonghi ECAM 23.460.S',
                    'description': 'Эта кофемашина настраивается на индивидуальные предпочтения пользователя и '
                                   'предлагает широкий выбор напитков на основе кофе, включая эспрессо, капучино '
                                   'и латте.',
                    'price': 93.00
                },
                {
                    'image': 'deps/images/goods/double bed.jpg',
                    'name': 'Чайник Bosch TWK8633P',
                    'description': 'Этот чайник имеет большой объем воды (1,5 литра), быстро кипятит воду и имеет '
                                   'множество дополнительных функций, таких как автоматическое отключение при '
                                   'достижении нужной температуры.',
                    'price': 670.00
                },
                {
                    'image': 'deps/images/goods/kitchen table.jpg',
                    'name': 'Ботинки Timberland 6-Inch Premium Waterproof Boots',
                    'description': 'Эти ботинки сделаны из прочной кожи, имеют водонепроницаемую мембрану и '
                                   'удобную подошву. Они идеально подходят для прогулок в любую погоду.',
                    'price': 365.00
                },
                {
                    'image': 'deps/images/goods/kitchen table 2.jpg',
                    'name': 'Куртка Columbia Pike Lake Hooded Jacket',
                    'description': 'Эта куртка имеет утеплитель Omni-Heat и водоотталкивающее покрытие, что '
                                   'обеспечивает тепло и комфорт в холодную и дождливую погоду',
                    'price': 430.00
                },
                {
                    'image': 'deps/images/goods/corner sofa.jpg',
                    'name': 'Джинсы Levis 501 Original Fit Jeans',
                    'description': 'Эти классические джинсы имеют прямой крой и удобную посадку. Они сделаны '
                                   'из высококачественного денима и идеально подходят для повседневного использования.',
                    'price': 610.00
                },
                {
                    'image': 'deps/images/goods/bedside table.jpg',
                    'name': 'Смартфон Apple iPhone 13 Pro Max',
                    'description': 'Этот флагманский смартфон оснащен A15 Bionic-чипом и системой тройной камеры,'
                                   ' включая широкоугольную, телеобъективную и сверхширокоугольную камеры. Он также '
                                   'имеет 6,7-дюймовый Super Retina XDR-экран, защиту от воды и пыли и работает '
                                   'на iOS 15.',
                    'price': 1300.00
                },
                {
                    'image': 'deps/images/goods/sofa.jpg',
                    'name': 'Смартфон Xiaomi Redmi Note 11 Pro',
                    'description': 'Смартфон Xiaomi Redmi Note 11 Pro - это высококачественный телефон '
                                   'с AMOLED дисплеем диагональю 6.67 дюймов и разрешением 1080x2400 пикселей. '
                                   'Он работает на операционной системе Android 11 и оснащен процессором Snapdragon '
                                   '870, 6 ГБ оперативной памяти и 128 ГБ встроенной памяти. Телефон также имеет '
                                   'потрясающую камеру с разрешением 108 МП и возможностью записи видео 4K.',
                    'price': 1000.00
                },
                {
                    'image': 'deps/images/goods/office chair.jpg',
                    'name': 'Ноутбук Lenovo IdeaPad 5',
                    'description': 'Ноутбук Lenovo IdeaPad 5 - это мощный компьютер с процессором Intel Core i5, 8 ГБ '
                                   'оперативной памяти и 512 ГБ SSD-накопителем. Он имеет 15.6-дюймовый дисплей с '
                                   'разрешением 1920x1080 пикселей, который обеспечивает яркое и четкое изображение. '
                                   'Также в комплекте идет встроенная видеокарта Intel Iris Xe, которая позволяет '
                                   'запускать большинство игр и приложений',
                    'price': 3000.00
                },
                {
                    'image': 'deps/images/goods/plants.jpg',
                    'name': 'Растение',
                    'description': 'Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.',
                    'price': 10.00
                },
                {
                    'image': 'deps/images/goods/flower.jpg',
                    'name': 'Цветок стилизированный',
                    'description': 'Дизайнерский цветок (возможно искусственный) для украшения интерьера.',
                    'price': 15.00
                },
                {
                    'image': 'deps/images/goods/strange table.jpg',
                    'name': 'Прикроватный столик',
                    'description': 'Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.',
                    'price': 25.00
                },
               ],
    }
    return render(request, 'goods/catalog.html')


def product(request):
    return render(request, 'goods/product.html')