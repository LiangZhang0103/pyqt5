from login_ui import LoginUi
from PyQt5.QtWidgets import QApplication, QLineEdit
import sys, sqlite3, hashlib, time, os

# 继承界面
class LoginLogical(LoginUi):
    def __init__(self):
        super(LoginLogical, self).__init__()

        # 此处盖面密码输入框lineEdit_password的属性，使其不实现密码
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.sqliteInit()

        self.conn = sqlite3.connect("user.db")

        # qt的洗脑槽机制，连接按钮的点击时间和相应的方法
        self.pushButton_signin.clicked.connect(self.sign_in)
        self.pushButton_signup.clicked.connect(self.sign_up)

    def sqliteInit(self):
        """
        在user.db数据库中创建含有id, name, password字段的表
        :return:
        """
        if not os.path.exists("user.db"):
            conn = sqlite3.connect('user.db')

            c = conn.cursor()      # 设置游标
            # 创建含有id, name, password字段的表
            c.execute("""CREATE TABLE user
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT NOT NULL, 
                        password TEXT NOT NULL)""")

            conn.commit()          # python 连接数据库默认开启事务
            conn.close()           # 关闭连接

    @staticmethod
    def hash(src):
        """
        哈希md5加密方法
        :param src: 字符串str
        :return:
        """
        src = (src + "请使用私钥加密").encode('utf-8')
        m = hashlib.md5()
        m.update(src)
        return m.hexdigest()

    def sign_in(self):
        """
        登陆方法
        :return:
        """
        c_sqlite = self.conn.cursor()
        user_name = self.lineEdit_user.text()
        user_password = self.lineEdit_password.text()
        if user_name == '' or user_password == "":
            self.lineEdit_user.setText("请输入用户和密码")
        else:
            c_sqlite.execute("""SELECT password FROM user WHERE name = ?""", (user_name,))
            password = c_sqlite.fetchall()
            if not password:
                self.lineEdit_user.setText("此用户没有注册")
            else:
                if user_password == password[0][0]:
                    self.lineEdit_user.setText("登陆成功")
                    time.sleep(1)
                    self.open_main_window()
                    self.close()
                else:
                    self.lineEdit_user.setText("密码不正确")

    def sign_up(self):
        """
        注册方法
        :return:
        """
        c_sqlite = self.conn.cursor()
        user_name = self.lineEdit_user.text()
        user_password = self.lineEdit_password.text()
        if user_name == "" or user_password == "":
            self.lineEdit_user.setText("请输入用户名和密码")
        else:
            user_password = user_password
            c_sqlite.execute("""SELECT password FROM user WHERE name = ?""", (user_name,))
            if not c_sqlite.fetchall():
                c_sqlite.execute("""INSERT INTO user VALUES (NULL, ?, ?)""", (user_name, user_password))
                self.conn.commit()
                self.lineEdit_user.setText("注册成功")
                self.conn.commit()
            else:
                self.lineEdit_user.setText("用户名重复")

    def open_main_window(self):
        """
        此处添加打开另一个窗口的程序
        :return:
        """
        # 下方这是的代码根据自己的情况修改
        # ui = Ui_Dialog()
        # ui.show()
        print("打开另一个窗口")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = LoginLogical()
    ui.show()
    sys.exit(app.exec_())


























