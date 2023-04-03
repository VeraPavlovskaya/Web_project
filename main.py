from flask import Flask, url_for

app = Flask(__name__)


@app.route('/Geo_Core')
def Geo_Core():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" /> 
                    <title>Географические карты</title>
                  </head>
                  <body>
                    <h1>Полезные географические ресурсы</h1>
                    <img src="{url_for('static', filename='../images/subjects.jpg')}" 
                         alt="Здесь скоро появится множество функций">
                    <div class="alert alert-info" role="alert">
                      Контурные карты
                    </div>

                    <div class="alert alert-success" role="alert">
                      Географические определения
                    </div>

                    <div class="alert alert-warning" role="alert">
                      Определение города к субъекту
                    </div>

                    <div class="alert alert-danger" role="alert">
                      Информация об авторе сайта
                    </div>

                    <div class="alert alert-primary" role="alert">
                      Будущие доработки
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    print("http://127.0.0.1:8080/Geo_Core")
    app.run(port=8080, host='127.0.0.1')
