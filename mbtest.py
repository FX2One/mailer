from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib, ssl

class Ui_Login(object):
    def openMailerDaemon(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_MailerDaemon()
        self.ui.setupUi(self.window)
        self.window.show()
        '''
        get method sender_line from Ui_MailerDaemon class that is responsible for opening new window
        get method log_me_mail from Ui_Login class responsible for passing email to email_input QlineEdit,
        pass it to newly opened window to sender_line QLineEdit which is used also as login to email services
        '''
        self.ui.sender_line.setText(Ui_Login.log_me_mail(self))
        self.ui.sender_line.setReadOnly(True) #prevent from changing and using another credentials

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(498, 584)
        Login.setStyleSheet("background-color: rgb(139, 139, 139)")
        self.login_label = QtWidgets.QLabel(Login)
        self.login_label.setGeometry(QtCore.QRect(150, 70, 231, 61))
        self.login_label.setStyleSheet("font-size:28pt; color: rgb(161, 79, 157);")
        self.login_label.setObjectName("login_label")
        self.pass_label = QtWidgets.QLabel(Login)
        self.pass_label.setGeometry(QtCore.QRect(20, 240, 101, 61))
        self.pass_label.setStyleSheet("font-size:18pt; color: rgb(161, 79, 157)")
        self.pass_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pass_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pass_label.setObjectName("pass_label")
        self.email_label = QtWidgets.QLabel(Login)
        self.email_label.setGeometry(QtCore.QRect(20, 190, 61, 31))
        self.email_label.setStyleSheet("font-size:18pt; color: rgb(161, 79, 157)")
        self.email_label.setObjectName("email_label")
        self.email_input = QtWidgets.QLineEdit(Login)
        self.email_input.setGeometry(QtCore.QRect(150, 190, 311, 31))
        self.email_input.setStyleSheet(
            "background-color: rgb(181, 181, 181); color: rgb(245, 245, 245); font-size: 12pt")
        self.email_input.setFrame(True)
        self.email_input.setObjectName("email_input")
        self.pass_input = QtWidgets.QLineEdit(Login)
        self.pass_input.setGeometry(QtCore.QRect(150, 250, 311, 31))
        self.pass_input.setStyleSheet(
            "background-color: rgb(181, 181, 181); color: rgb(245, 245, 245); font-size: 12pt")
        self.pass_input.setObjectName("pass_input")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)  # dotted password
        self.sign_in_btn = QtWidgets.QPushButton(Login)
        self.sign_in_btn.setGeometry(QtCore.QRect(190, 350, 111, 41))
        self.sign_in_btn.setStyleSheet("font-size:18pt; background-color: rgb(161, 79, 157);color: rgb(181, 181, 181)")
        self.sign_in_btn.setObjectName("sign_in_btn")
        self.sign_in_btn.clicked.connect(self.log_me)
        self.sign_in_btn.clicked.connect(self.openMailerDaemon) #open new MailerDaemon window
        self.sign_in_btn.clicked.connect(Login.close) #close current window after succesfully logged in

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)


    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.login_label.setText(_translate("Login", "Login Page"))
        self.pass_label.setText(_translate("Login", "Password"))
        self.email_label.setText(_translate("Login", "Email"))
        self.sign_in_btn.setText(_translate("Login", "Sign In"))

    #login signal to email input QlineEdit
    def log_me_mail(self):
        lmm = self.email_input.text()
        return lmm

    # login signal to password input QlineEdit
    def pass_me_mail(self):
        pmm = self.pass_input.text()
        return pmm

    #login to gmail mail services
    def log_me(self):
        pass_input = self.pass_me_mail()
        email_input = self.log_me_mail() #take email.input.text from log_me_mail method and pass it to email_input variable
        context = ssl.create_default_context()
        smtp_server = "smtp.gmail.com"
        port = 465
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(email_input, pass_input)
        print('logged in succesfully')


class Ui_MailerDaemon(object):
    def selectFile(self):
        file_dialog = QtWidgets.QFileDialog.getOpenFileName()
        fd_path = file_dialog[0]  # take first element of tuple
        file_set_text = self.file_line.setText(fd_path)  # pass path name to file_line when file is selected

        my_file = open(fd_path)
        read_file = my_file.read()
        bcc_file = read_file.replace(',', ', ')

        '''read opened file, replace all commas with blank spaces, loop through it ,append to list and return list'''
        '''creates list of future recipients from the file'''
        def func_read():
            rd = read_file
            x = []
            s = rd.replace(',', ' ')
            for word in s.split():
                x.append(word)
            return x

        file_set_read = self.bcc_line.setText(bcc_file) # pass contents of the file to bcc_line

        list_transformer = func_read() # list of ready recipients to be passed in
        return list_transformer

    '''return typed in contents of the email'''
    def msg_content(self):
        mc = self.msg_box.text()
        return mc

    def subject(self):
        sbj = self.subject_line.text()
        return sbj

    def selectAttachment(self):
        attach_dialog = QtWidgets.QFileDialog.getOpenFileName()
        ad_path = attach_dialog[0]  # take first element of tuple
        attach_set_text = self.attach_line.setText(ad_path)  # pass path name to file_line when file is selected

    

    def setupUi(self, MailerDaemon):
        MailerDaemon.setObjectName("MailerDaemon")
        MailerDaemon.resize(674, 767)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MailerDaemon.setFont(font)
        MailerDaemon.setStyleSheet("background-color: rgb(139, 139, 139); font-size:10pt")
        self.mailer_label = QtWidgets.QLabel(MailerDaemon)
        self.mailer_label.setGeometry(QtCore.QRect(240, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.mailer_label.setFont(font)
        self.mailer_label.setStyleSheet("font-size:28pt; color: rgb(161, 79, 157)")
        self.mailer_label.setObjectName("mailer_label")
        self.subject_label = QtWidgets.QLabel(MailerDaemon)
        self.subject_label.setGeometry(QtCore.QRect(10, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.subject_label.setFont(font)
        self.subject_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.subject_label.setObjectName("subject_label")
        self.sender_label = QtWidgets.QLabel(MailerDaemon)
        self.sender_label.setGeometry(QtCore.QRect(10, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sender_label.setFont(font)
        self.sender_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sender_label.setObjectName("sender_label")
        self.bcc_label = QtWidgets.QLabel(MailerDaemon)
        self.bcc_label.setGeometry(QtCore.QRect(10, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bcc_label.setFont(font)
        self.bcc_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.bcc_label.setObjectName("bcc_label")
        self.subject_line = QtWidgets.QLineEdit(MailerDaemon)
        self.subject_line.setGeometry(QtCore.QRect(90, 70, 521, 20))
        self.subject_line.setStyleSheet("background-color: rgb(231, 231, 231)")
        self.subject_line.setObjectName("subject_line")
        self.sender_line = QtWidgets.QLineEdit(MailerDaemon)
        self.sender_line.setGeometry(QtCore.QRect(90, 100, 521, 20))
        self.sender_line.setStyleSheet("background-color: rgb(231, 231, 231)")
        self.sender_line.setObjectName("sender_line")
        self.bcc_line = QtWidgets.QLineEdit(MailerDaemon)
        self.bcc_line.setGeometry(QtCore.QRect(90, 130, 521, 20))
        self.bcc_line.setStyleSheet("background-color: rgb(231, 231, 231)")
        self.bcc_line.setObjectName("bcc_line")
        self.msg_box = QtWidgets.QTextEdit(MailerDaemon)
        self.msg_box.setGeometry(QtCore.QRect(90, 220, 521, 411))
        self.msg_box.setStyleSheet("background-color: rgb(231, 231, 231)")
        self.msg_box.setObjectName("msg_box")
        self.msg_label = QtWidgets.QLabel(MailerDaemon)
        self.msg_label.setGeometry(QtCore.QRect(10, 220, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label.setFont(font)
        self.msg_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.msg_label.setObjectName("msg_label")
        self.attach_btn = QtWidgets.QPushButton(MailerDaemon)
        self.attach_btn.setGeometry(QtCore.QRect(500, 640, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.attach_btn.setFont(font)
        self.attach_btn.setStyleSheet("background-color: rgb(231, 231, 231)")
        self.attach_btn.setObjectName("attach_btn")
        self.send_msg_btn = QtWidgets.QPushButton(MailerDaemon)
        self.send_msg_btn.setGeometry(QtCore.QRect(500, 730, 111, 23))
        self.send_msg_btn.setStyleSheet("background-color: rgb(231, 231, 231)")
        self.send_msg_btn.setObjectName("send_msg_btn")
        self.file_btn = QtWidgets.QPushButton(MailerDaemon)
        self.file_btn.setGeometry(QtCore.QRect(550, 160, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.file_btn.setFont(font)
        self.file_btn.setStyleSheet("background-color: rgb(231, 231, 231)")
        self.file_btn.setObjectName("file_btn")
        self.upload_label = QtWidgets.QLabel(MailerDaemon)
        self.upload_label.setGeometry(QtCore.QRect(460, 190, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.upload_label.setFont(font)
        self.upload_label.setStyleSheet("color: rgb(231, 231, 231)")
        self.upload_label.setObjectName("upload_label")
        self.file_line = QtWidgets.QLineEdit(MailerDaemon)
        self.file_line.setGeometry(QtCore.QRect(90, 160, 451, 20))
        self.file_line.setStyleSheet("background-color: rgb(231, 231, 231)")
        self.file_line.setObjectName("file_line")
        self.attach_line = QtWidgets.QLineEdit(MailerDaemon)
        self.attach_line.setGeometry(QtCore.QRect(90, 640, 401, 21))
        self.attach_line.setStyleSheet("background-color: rgb(231, 231, 231)")
        self.attach_line.setText("")
        self.attach_line.setObjectName("attach_line")
        self.up_att_label = QtWidgets.QLabel(MailerDaemon)
        self.up_att_label.setGeometry(QtCore.QRect(500, 670, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.up_att_label.setFont(font)
        self.up_att_label.setStyleSheet("color: rgb(231, 231, 231)")
        self.up_att_label.setObjectName("up_att_label")
        self.mutli_label = QtWidgets.QLabel(MailerDaemon)
        self.mutli_label.setGeometry(QtCore.QRect(90, 660, 161, 21))
        self.mutli_label.setStyleSheet("color: rgb(231, 231, 231)")
        self.mutli_label.setObjectName("mutli_label")
        self.ziprar_label = QtWidgets.QLabel(MailerDaemon)
        self.ziprar_label.setGeometry(QtCore.QRect(90, 680, 221, 16))
        self.ziprar_label.setStyleSheet("color: rgb(231, 231, 231)")
        self.ziprar_label.setObjectName("ziprar_label")
        self.file_btn.clicked.connect(self.selectFile)
        self.attach_btn.clicked.connect(self.selectAttachment)

        self.retranslateUi(MailerDaemon)
        QtCore.QMetaObject.connectSlotsByName(MailerDaemon)

    def retranslateUi(self, MailerDaemon):
        _translate = QtCore.QCoreApplication.translate
        MailerDaemon.setWindowTitle(_translate("MailerDaemon", "Dialog"))
        self.mailer_label.setText(_translate("MailerDaemon", "MailerDaemon"))
        self.subject_label.setText(_translate("MailerDaemon", "Subject"))
        self.sender_label.setText(_translate("MailerDaemon", "Sender"))
        self.bcc_label.setText(_translate("MailerDaemon", "To Bcc"))
        self.msg_label.setText(_translate("MailerDaemon", "Message"))
        self.attach_btn.setText(_translate("MailerDaemon", "Add Attachment"))
        self.send_msg_btn.setText(_translate("MailerDaemon", "Send Message"))
        self.file_btn.setText(_translate("MailerDaemon", "File"))
        self.upload_label.setText(_translate("MailerDaemon", "Upload recipients from file"))
        self.up_att_label.setText(_translate("MailerDaemon", "Upload attachment"))
        self.mutli_label.setText(_translate("MailerDaemon", "For multiple attachements"))
        self.ziprar_label.setText(_translate("MailerDaemon", "please upload archived in any .zip/.rar format"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) #create new instance of QApplication
    Login = QtWidgets.QDialog() #create new instance of created UI
    ui = Ui_Login() #create an instace of QDialog
    ui.setupUi(Login) #create widgets inside the windows holding widgets
    Login.show() #show the window with all it's contents
    sys.exit(app.exec_()) #close the program when close the application gets clicked
