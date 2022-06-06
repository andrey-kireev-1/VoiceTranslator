import sys
import speech_recognition as sr
from googletrans import Translator
from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow

class Translating_program(QMainWindow):
    def __init__(self):
        super(Translating_program, self).__init__()
        self.ui = Ui_MainWindow() #объект графического интерфейса
        self.ui.setupUi(self)
        self.ui.btn_trans.clicked.connect(self.record_volume) #кнопка микрофона
        self.ui.btn_lang.clicked.connect(self.change_lang) #кнопка смены языка
        self.l_t = self.ui.left_text #левая TextArea
        self.r_t = self.ui.right_text #правая TextArea
        self.l_l = self.ui.left_label #левый лейбл
        self.r_l = self.ui.right_label #правый лейбл
        self.lang_flag = True #True - английский, False - русский

    def change_lang(self) -> None:
        l_label = self.l_l.text()
        r_label = self.r_l.text()
        self.l_l.setText(r_label) #Сменить местами лейблы языков
        self.r_l.setText(l_label)
        if self.lang_flag == True: self.lang_flag = False #сменить "флаг" языка
        else: self.lang_flag = True
        

    def record_volume(self) -> None:
        r = sr.Recognizer()
        try:
            with sr.Microphone(device_index=1) as source: #вызов рабочего микрофона из всех подключенных аудиозаписывающих устройств
                print("start listen")
                audio = r.listen(source,timeout=10) #запись с микрофона
            if self.lang_flag == True:
                query = r.recognize_google(audio, language="en-EN") #распознавание английского языка
                text = query.lower() #перевод в нижний регистр
                self.l_t.setText(text) #вывод в правую TextArea
                trans = Translator()
                self.r_t.setText(trans.translate(text, dest='ru').text) #перевод на русский
            else:
                query = r.recognize_google(audio, language="ru-RU") #распознавание русского языка
                text = query.lower() #перевод в нижний регистр
                self.l_t.setText(text) #вывод в левую TextArea
                trans = Translator()
                self.r_t.setText(trans.translate(text, dest='en').text) #перевод на английский
        except:
            self.l_t.setText("")
            self.r_t.setText("")
            self.l_t.setText("Попробуйте еще раз")  

            print("Повторите еще раз")
        finally:
            print("stop listen") 
            

if __name__ == "__main__":
    app = QApplication(sys.argv) #создание объекта QtWidget

    window = Translating_program()
    window.show() #вывод окна Переводчика

    sys.exit(app.exec())