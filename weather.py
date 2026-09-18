import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class Weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName('city_label')
        self.city_input.setObjectName('city_input')
        self.get_button.setObjectName('get_button')
        self.temperature_label.setObjectName('temperature_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')
    
        self.setStyleSheet("""
        QLabel, QPushButton{
        font-family: calibri;
        }
        QLabel#city_label{
        font-size: 40px;
        font-style: italic;
        }
        QLineEdit#city_input{
        font-size: 40px;
        padding: 5px;
        min-width: 250px;
        }
        QPushButton#get_button{
        font-size:30px;
        font-weight: bold;
        }
        QLabel#temperature_label{
        font-size: 75px;
        }
        QLabel#emoji_label{
        font-size: 100px;
        font-family: Apple Color Emoji;
        }
        QLabel#description_label{
        font-size: 50px;
        }
        """)

        self.get_button.clicked.connect(self.get_weather)

    @staticmethod
    def get_emoji(id):
        if 200 <= id <= 232:
            return " ⛈️ "
        elif 300 <= id <= 321:
            return " ☁️ "
        elif 500 <= id <= 531:
            return " 🌧️ "
        elif 600 <= id <= 622:
            return " 🌨️ "
        elif 701 <= id <= 741:
            return " 🌫️ "
        elif id == 762:
            return " 🌋 "
        elif id == 771:
            return ' 💨 '
        elif id == 781:
            return ' 🌪️ '
        elif id == 800:
            return " ☀️ "
        elif 801 <= id <= 804:
            return " ☁️ "
        else:
            return ''

    def get_weather(self):
        api_key = "44c910eb595b6ea7b674e9a2731c8e4a"
        city = self.city_input.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        
            if data['cod'] == 200:
                self.display_weather(data)


        except requests.exceptions.HTTPError as http_error:

            match response.status_code:
                case 400:
                    self.display_error("Bad Request \nPleae Check your input.")
                case 401:
                    self.display_error("Unauthorized \nInvalid API Key.")
                case 403:
                    self.display_error("Forbidden \nAccess Denied.")
                case 404:
                    self.display_error("Not Found \nCity Not Found!.")
                case 500:
                    self.display_error("Internal Server Error \nPlease Try Again Later.")
                case 502:
                    self.display_error("Bad Gateway \nInvalid Server Response.")
                case 503:
                    self.display_error("Service Unavailable \n Service is Down.")
                case 504:
                    self.display_error("Gateway Timeout \nNo response form server.")
                case _:
                    self.display_error(F"HTTP Error occured \n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your Internet Connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error!")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects")
        except requests.exceptions.RequestException as req_err:
            self.display_error(f"Request Error:\n{req_err}")





    def display_error(self, message):
        self.temperature_label.setStyleSheet("""
        font-size: 30px;
        """)
        self.temperature_label.setText(message)
        self.emoji_label.setText("")
        self.description_label.setText("")


    def display_weather(self, data):
        self.temperature_label.setStyleSheet("""
                font-size: 75px;
        """)
        temperatur_k = data['main']['temp']
        temperatur_c = temperatur_k - 273.15
        temperatur_f = temperatur_k * 9/5 - 459.67
        weather_id = data['weather'][0]['id']


        self.temperature_label.setText(f"{temperatur_c:.1f}℃ ")
        self.emoji_label.setText(self.get_emoji(weather_id))
        weather_description = data['weather'][0]['description']
        self.description_label.setText(f"{weather_description}")


        



if __name__ == "__main__":

    app = QApplication(sys.argv)
    weather_app = Weather_app()
    weather_app.show()
    sys.exit(app.exec_())
