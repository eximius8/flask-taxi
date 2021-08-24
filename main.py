"""Запуск приложения для подбора такси."""
from flasktaxi import app


if __name__ == '__main__':
    app.run(debug=True)
