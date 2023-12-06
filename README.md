# Restaurant
<h1>Задача :
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:</h1>
<H2>1) Меню реализовано через template tag</H2>
Меню выпонено черз template tag, а именно в таких местах как наследование от base.html {% extends "menu/base.html" %} а так же блоков contenta {% block content %}

```

</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="admin/">Ресторан</a></li>
                <li>
                    <ul>
                        <li><a href="{% url 'index' %}">Ресторане</a></li>
                        <li><a href="{% url 'menu:menu' %}">Меню</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>

```


<h2>2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.</h2>

![image](https://github.com/bgbisdbg/Restaurant/assets/136889642/20b52b78-62f6-490d-a876-872c24282be5)


<h2>3) Хранится в БД.</h2>
Во время создания проекта были созданы модели а так же были выполнены миграции 

![image](https://github.com/bgbisdbg/Restaurant/assets/136889642/0f907e02-7acf-4de7-b4b2-f6b562f7540a)


<h2>4) Редактируется в стандартной админке Django</h2>
В вход в django admin был реалезован через главную кнопу ``` <ul>
                <li><a href="admin/">Ресторан</a></li>
                <li>```
После создание и миграции моделей они были зарегистрированны в приложение admin для взаимодействия с ними в панели admin
```
from django.contrib import admin
from menu.models import DishModel, DescriptionModel


@admin.register(DishModel)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ('name',)


@admin.register(DescriptionModel)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'dish')
    fields = ('dish', 'description', 'link')
```

                
<h2>5) Активный пункт меню определяется исходя из URL текущей страницы</h2>
 Были выполнены исходя из URL текущей страницы

![image](https://github.com/bgbisdbg/Restaurant/assets/136889642/23e57719-2d1e-43c6-bf7c-5bbefa62998f)


![image](https://github.com/bgbisdbg/Restaurant/assets/136889642/8ca8cfd5-989c-4e68-9f91-3aaf8394c9e4)


<h2>6 )Меню на одной странице может быть несколько. Они определяются по названию.</h2>
На странице меню есть блюда с раскрывающимся кратким описанием и ссылкой на него

![image](https://github.com/bgbisdbg/Restaurant/assets/136889642/9d265927-9f03-4234-9ae3-4c83db8dbf82)


<h2>7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.</h2>
Переходы по ссылками реалезованы в urls.py
```
from django.urls import path
from menu.views import DescriptionListView, IndexView

app_name = 'menu'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu/', DescriptionListView.as_view(), name='menu')
]
```
Так же и в шаблонах 

![image](https://github.com/bgbisdbg/Restaurant/assets/136889642/641e6d22-cdac-409c-b99d-13c15d954738)

8)На отрисовку каждого меню требуется ровно 1 запрос к БД
Страница "О ресторане"

![image](https://github.com/bgbisdbg/Restaurant/assets/136889642/4cca7b00-427d-42ba-9954-84966f9af023)

Формирует 2 запроса SQL косаемые пользователей

![image](https://github.com/bgbisdbg/Restaurant/assets/136889642/c7dec8d1-36c6-4d68-a652-9193b46e9019)


А страница меню формирует 6 запросов 2 запроса к пользователю и 3 к элеменат выводящим объекты БД 

![image](https://github.com/bgbisdbg/Restaurant/assets/136889642/132d840b-25e7-431a-adc6-9f37c85984da)


![Uploading image.png…]()


 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
При решении тестового задания у вас не должно возникнуть вопросов. Если появляются вопросы, вероятнее всего, у вас недостаточно знаний.
