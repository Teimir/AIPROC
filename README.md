# AIPROC
AI in this project is Chat GPT
https://chat.openai.com/chat

Based on question
Стань эмулятором моего процессора. 
В нём есть регистры с именами "А","Б","В", в которые можно вносить информацию через команду "Загрузить в ИМЯ РЕГИСТРА ЗНАЧЕНИЕ в формате десятичного числа" 
АЛУ, которое может складывать два регистра по команде "Сложить ИМЯ РЕГИСТРА и ИМЯ РЕГИСТРА", вычитать по команде "Вычесть ИМЯ РЕГИСТРА и ИМЯ РЕГИСТРА" и всегда кладёт результат в регистр "А". 
Также мы можем переместить значение между регистрами при помощи команды "Переместить из ИМЯ РЕГИСТРА в ИМЯ РЕГИСТРА". 
Кроме этого у нас есть регистр "УКАЗАТЕЛЬ ИНСТРУКЦИИ", который показывает номер текущей инструкции, начиная с ноля, 
Мы можем поместить его значение в регистр "А" при помощи команды "Получить указатель", 
а также мы можем совершить переход на другую инструкцию, через изменение указателя инструкции при помощи команды "Прыжок", поместив в регистр "УКАЗАТЕЛЬ ИНСТРУКЦИИ" значение из регистра "А" 
или "Прыжок, если ноль в ИМЯ РЕГИСТРА", Эта команда означает, что мы меняем значение регистра "УКАЗАТЕЛЬ ИНСТРУКЦИИ" на значение из регистра "А" в том случае, 
если регистр с указанным в команде именем содержит ноль. 
Остановись, когда я напишу СТОП

Pull request if you want. Tag the author when using.
