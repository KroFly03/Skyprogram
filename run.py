from flask import Flask
from main.view import main_blueprint
from api.view import api_blueprint
import logging


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)

log_format = '%(asctime)s [%(levelname)s]Запрос %(message)s'

# Отключение стандартного логирования
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

logging.basicConfig(filename='api.log', level=logging.INFO, encoding='utf-8', format=log_format)


# Обработка ошибки 404
@app.errorhandler(404)
def not_found(e):
    return 'Сервер не найден'


# Обработка ошибки 500
@app.errorhandler(500)
def internal_server_error(e):
    return 'Ошибка сервера'


if __name__ == '__main__':
    app.run(debug=False)
