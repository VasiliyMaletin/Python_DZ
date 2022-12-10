# Подготовка к запуску бота
необходимо в файл `tg_bot.py`, вставить **API-ключ** своего бота
и после этого запустить этот файл.

![Image](api.png)

## Описание работы бота
Бот позволяет использовать встроенный калькулятор и ~~играть в крестики-нолики~~(**`в разработке`**) 

При запуске бота командой *`/start`*, появляется меню с кнопками навигации.

![Image](main_menu.png)

Меню содержит кнопки:
* `Привет` - *нажав её можно поздороваться с ботом*
* `Кто создал бота?` - *нажав её можно узнать о создателе бота*
* `Приложения` - *нажав её можно выбрать интересующее приложение*
  >![Image](app.png)
  >`Калькулятор` - *нажав её запуститься калькулятор*
  >>![Image](calc.png)
  >> ### Окно содержит:
  >>* кнопки всех цифр от `0` до `9`
  >>* кнопку мнимой единицы для комплексных вычислений `j`
  >>* кнопки всех основных операций `+`, `-`, `*`, `/`
  >>* кнопки скобок для возможности приоритезации операций `( )`
  >>* кнопку очистки поля `C`
  >>* кнопку для посимвольного удаления `<=`
  >>* кнопку для вещественных чисел `,`
  >>* кнопку для вычисления введенного выражения `=`
  >>
  >>Все строки для вычисления и результаты вычисления, а также ошибки вычисления (если возникали) фиксируются в лог-файле log.csv с указанием времени операции
  ![Image](log.png)
  >>
  >`Крестики-нолики` - **Кнопка в разработке 🛠**
  >>![Image](*.png)
  >>
  >`Назад` - *нажав её можно вернуться в предидущее меню*
  >>![Image](back.png)
  >`В главное меню` - *нажав её можно вернуться в главное меню*
