# Подготовка к запуску бота
необходимо в файл `tg_bot.py`, вставить **API-ключ** своего бота
и после этого запустить этот файл.

![Image](https://github.com/VasiliyMaletin/Python_DZ/blob/dz_seminar_9/api.PNG)

## Описание работы бота
Бот позволяет использовать встроенный калькулятор и играть в крестики-нолики 

При запуске бота командой *`/start`*, появляется меню с кнопками навигации.

![Image](https://github.com/VasiliyMaletin/Python_DZ/blob/dz_seminar_9/main_menu.PNG)

Меню содержит кнопки:
* `Привет` - *нажав её можно поздороваться с ботом*
* `Кто создал бота?` - *нажав её можно узнать о создателе бота*
* `Приложения` - *нажав её можно выбрать интересующее приложение*
  >![Image](https://github.com/VasiliyMaletin/Python_DZ/blob/dz_seminar_9/app.PNG)
  >
  >`Калькулятор` - *нажав её запуститься калькулятор*
  >>![Image](https://github.com/VasiliyMaletin/Python_DZ/blob/dz_seminar_9/calc.PNG)
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
  >>
  >>![Image](https://github.com/VasiliyMaletin/Python_DZ/blob/dz_seminar_9/log.PNG)
  >
  >`Крестики-нолики` - *нажав её запускается игра в крестики-нолики*
  >
  >>![Image](https://github.com/VasiliyMaletin/Python_DZ/blob/dz_seminar_9/tic_tak_toe.PNG)
  >>
  >>`Ещё раз` - *нажав её можно начать новую игру в крестики-нолики*
  >>
  >`Назад` - *нажав её можно вернуться в предидущее меню*
  >>![Image](https://github.com/VasiliyMaletin/Python_DZ/blob/dz_seminar_9/back.PNG)
  >
  >`В главное меню` - *нажав её можно вернуться в главное меню*
  >
Присутствует логирование событий телеграмм бота:

![Image](https://github.com/VasiliyMaletin/Python_DZ/blob/dz_seminar_9/bot_log.PNG)
