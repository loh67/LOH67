from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QRadioButton, QGroupBox



#создание классаpip list
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


#создание функций
def ask(q: Question):
    #прячем GroupBox-ы
    RGB.hide()
    grup_ans.hide()
    
    #заполнение неотображаемых кнопок значениями
    btn_answer1.setText(q.right_answer)
    btn_answer2.setText(q.wrong1)
    btn_answer3.setText(q.wrong2)
    btn_answer4.setText(q.wrong3)

    #перемешивание значений
    shuffle(answers)  
    layoutV1.addWidget(answers[0])
    layoutV1.addWidget(answers[1])
    layoutV2.addWidget(answers[2])
    layoutV2.addWidget(answers[3])

    #сброс флагов с кнопок
    RadioGroup.setExclusive(False)  
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

    


    #отображение GroupBox-а
    question.setText(q.question)
    answear.setText(q.right_answer)
    RGB.show()
    btn_question.setText('Ответить')

   

def check_answer():
    #создание вариантов отображения ответа
    ans_correct = 'Правильно'
    ans_wrong = 'Неправильно'
    ans_miss = 'Необходимо выбрать вариант ответа'
    
    #проверка какая кнопка нажата и правильный ли это ответ
    if btn_answer1.isChecked():
        show_correct(ans_correct)
        main_win.number_right_questions += 1
        main_win.number_of_questions += 1
       
    elif btn_answer2.isChecked() or btn_answer3.isChecked() or btn_answer4.isChecked():
        show_correct(ans_wrong)  
        main_win.number_of_questions += 1
        
    else:
        show_correct(ans_miss)    
        main_win.number_of_questions += 1
        
       

def show_correct(res):
    #прячем GroupBox-ы
    RGB.hide()
    grup_ans.hide()
    
    #заполняем переменные
    rez_ans.setText(res)
    '''answer = btn_answer2.text'''
    
    #отображаем 
    grup_ans.show()
    btn_question.setText('Следующий вопрос')


def show_question():
    RGB.show()
    grup_ans.hide()
    question.setText('Какой национальности не существует?')
    btn_question.setText('Ответить')
    RadioGroup.setExclusive(False)    
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)   
    
def show_result():
    RGB.hide()
    grup_ans.show()
    question.setText('Самый сложный вопрос')
    btn_question.setText('Следующий вопрос') 
    

def start_test():
    if btn_question.text() == 'Ответить':
        show_result()
        
    else:
        show_question()

def next_question():
    '''задаёт случайный вопрос'''

    shuffle(questions_list)
    main_win.cur_question += 1                          #переход к следующему вопросу
    
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0                       #если список с вопросами закончился, то начинаем с начала
    q = questions_list[main_win.cur_question]           #выбор вопроса

    ask(q)                                                   #отображение этого вопроса
    
                              
    



def click_OK():        
    if btn_question.text() == 'Ответить':
        check_answer()
    else:
        next_question()
      
    

app = QApplication([])
main_win = QWidget()
main_win.resize(350, 270)

main_win.setWindowTitle('Memory Card')
question = QLabel('')

RGB = QGroupBox('Варианты ответов:')                                 #первый groupbox, добавление в него кнопок с вариантами ответов и создание лэйаутов
btn_answer1 = QRadioButton('Португальский')
btn_answer2 = QRadioButton('Японский')
btn_answer3 = QRadioButton('Питон')
btn_answer4 = QRadioButton('Итальянский')

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]       #список с кнопками

layoutH1 = QHBoxLayout()   
layoutV1 = QVBoxLayout() 
layoutV2 = QVBoxLayout()

#переменные для счётчика для статистки
main_win.number_of_questions = 0
main_win.number_right_questions = 0


#создание группы для кнопок
RadioGroup = QButtonGroup() 
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)


layoutV1.addWidget(btn_answer1) 
layoutV1.addWidget(btn_answer2)
layoutV2.addWidget(btn_answer3) 
layoutV2.addWidget(btn_answer4)
layoutH1.addLayout(layoutV1)
layoutH1.addLayout(layoutV2)
layoutV1.setSpacing(40)
layoutV2.setSpacing(40)
layoutH1.setSpacing(40)
RGB.setLayout(layoutH1)


btn_question = QPushButton('Ответить')                 #Создание кнопки ответа
layout_main_vertical = QVBoxLayout()
layout_main_horizon1 = QHBoxLayout()
layout_main_horizon3 = QHBoxLayout()



layout_main_horizon1.addWidget(question, alignment=Qt.AlignCenter)       #сбор виджетов и группы

layout_main_horizon3.addWidget(btn_question, alignment=Qt.AlignRight)

layout_main_vertical.addLayout(layout_main_horizon1)
layout_main_vertical.addWidget(RGB, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))




#оформление окна результата

grup_ans = QGroupBox('Результат ответа:')
rez_ans = QLabel('Прав/неправ')
answear = QLabel('Правильный ответ: ', )
boxline_vert = QVBoxLayout()
boxline_vert.addWidget(rez_ans, alignment=Qt.AlignHCenter )
boxline_vert.setSpacing(30)
boxline_vert.addWidget(answear, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))


grup_ans.setLayout(boxline_vert)


layout_main_vertical.addWidget(grup_ans, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))     #сбор виджетов и двух групп

layout_main_vertical.addLayout(layout_main_horizon3)    #сбор виджетов и двух групп
main_win.setLayout(layout_main_vertical)                #сбор виджетов и двух групп



#создание экземпляра класса и списка
main_win.cur_question = -1                              #переменная для счётчика в функции next_question
questions_list = list()

q1 = Question('Государственный язык Бразилии', 
'Португальский', 
'Японский', 'Питон', 'Итальянский')

q2 = Question('Столица России', 
'Москва',
'Пекин', 'Токио', 'Владивосток')

q3 = Question('Столица Японии', 
'Токио',
'Вашингтон', 'Новосибирск', 'Сидней')





questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)

btn_question.clicked.connect(click_OK)
next_question()


main_win.show()
app.exec_()

main_win.statistic_of_answers = main_win.number_right_questions/main_win.number_of_questions*100
main_win.statistic_of_answers = round(main_win.statistic_of_answers, 2)

print('Количество всех вопросов:', main_win.number_of_questions)
print('Количество правильных вопросов:', main_win.number_right_questions)
print('Статистика правильных ответов:',main_win.statistic_of_answers , '%')
