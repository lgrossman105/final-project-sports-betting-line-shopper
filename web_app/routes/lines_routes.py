
# this is the "web_app/routes/lines_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.odds_shopper import get_in_season_sports, get_sport_odds

lines_routes = Blueprint("lines_routes", __name__)

@lines_routes.route("/lines/form")
def lines_form():
    print("Betting Lines Form...")

    sports = get_in_season_sports()

    return render_template("lines_form.html", sports = sports)

# /lines/dashboard?sport=americanfootball_nfl
@lines_routes.route("/lines/dashboard", methods=["GET", "POST"])
def lines_dashboard():
    print("LINES DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    sports = get_in_season_sports()
    sport_name = request_data.get("symbol")
    print(sport_name)
    sport = next((s["key"] for s in sports if s["title"] == sport_name), None)

    try:
        df = get_sport_odds(sport)

        flash("Fetched Real-time Odds Data!", "success")
        return render_template("lines_dashboard.html",
            data=df,
            sport=sport_name
        )
    except Exception as err:
        print('OOPS', err)

        flash("Odds Data Error. Please try again!", "danger")
        return redirect("/lines/form")

#
# API ROUTES
#

# /api/stocks.json?symbol=SPOT
'''@lines_routes.route("/api/stocks.json")
def stocks_api():
    print("STOCKS DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    symbol = url_params.get("symbol") or "NFLX"

    try:
        df = fetch_stocks_csv(symbol=symbol)
        data = df.to_dict("records")
        return {"symbol": symbol, "data": data }
    except Exception as err:
        print('OOPS', err)
        return {"message":"Market Data Error. Please try again."}, 404'''