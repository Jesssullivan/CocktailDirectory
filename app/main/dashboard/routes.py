from flask import Blueprint, render_template, url_for, request
from flask import current_app as app
from flask import redirect

dashboard_blueprint = Blueprint("dashboard", __name__)


""" demo data """
demo_drinks = dict()

demo_drinks['astoria'] = {"title": "Astoria",
                          "author": "Shed",
                          "step": ["2 dashes Orange Bitters",
                                   "1.5oz Gin",
                                   "0.75oz Dry Vermouth",
                                   "0.5oz Iced Water"],
                          "form": {
                              "Small Rock Glass": "Small Spritz of Lemon on the Prince Cube",
                              "Nick and Nora Glass": "Small spritz of Lemon in the Glass"
                          },
                          "onWeb": False
                          }


""" routing """


# Index Routes:
@dashboard_blueprint.route("/")
def dash_index():
    return redirect("/dashboard/home", code=302)


@dashboard_blueprint.route('/home', methods=['GET'])
def dash_home():
    return render_template('home.j2')


@dashboard_blueprint.route("/drink/<string:drink_id>", methods=["GET", "POST"])
def render_drink_id(drink_id):

    drink = demo_drinks[drink_id]

    return render_template('drink_template.j2',
                           title=drink["title"],
                           author=drink["author"],
                           steps=drink["step"],
                           forms=drink["form"],
                           onWeb=drink["onWeb"])


@dashboard_blueprint.route('/moose/<int:moose>', methods=['GET'])
def success(moose):
    return 'Here: %s' % moose


""" fetch static """


@dashboard_blueprint.route("<file>", methods=["GET", "POST"])
def dash_filex(file):
    return app.send_static_file(file)
