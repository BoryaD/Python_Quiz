# Quize
Quize application on Django. <br>
Language: **Python** <br>
Platforms and technologies: **Python 3.8**, **Docker**, **Postgresql**, **Redis**

# Описание
Данный проект представляет собой бесконечные квизы на каждые темы. 
В нашем проекте реалиизованны тематические квизы, которые происходят следующим образом: 
1) Пользователи выбирают тематический квиз, который им инетерен
2) Далее на страницке дропаются вопросы, на которые все пользователи, проходящие данный квиз, должны отвечать на один вопрос
3) Если один пользователей ответил правильно, то дропается следующий вопрос
4) Если никто из пользователей не может ответит на вопрос, затем автоматически (через минуту) дропается следующйи вопрос

Также в проекте реализован чат. Чат является едиственным для всех квизов. Только залогиненные пользователи моугт использовать чат. Также в данном проекте реализованне функиции регистрации, валидации, смены пароля через личный профиль, смена пароля через почту (если пользователь забыл пароль). Также реализована система баллов, которе отображатся в личном профиле пользователя. Личный профиль пользователя содержит в себе ник, фотографию, mail пользователя, а также количество набранных баллов (coins). Баллы начисляются за каждый правильный ответ. Реализована возможность просматривать профили других пользователей и редактировать свой. Также пользователь с правами админимтратора может добавлять квизы и вопросы в них (не через \admin)

# Реализация 
Данное приложение использует технологию docker для быстрого развертывания. В нашем проекте используются 3 контейнера:
1) Само приложение quiz
2) PostgesQL
3) Redis
В качестве базы данные использована PostgersQL.
Также для реализации чата была использована библиотека django channels которая позовлила нашему приложению получить функции асинхронного интерфейса. Для того, чтобы каналы имели связь друг с другом в качестве брокера мы использовали Redis. Для того, чтобы обновлять не всю страницу, а только её часть с вопросом и чат была использована технология ajax

