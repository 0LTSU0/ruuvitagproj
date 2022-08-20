#from dbreader import *
import time
import datetime
from flask import Flask, render_template, jsonify
import random
import dbreader
import threading

app = Flask(__name__)
RUN_RUUVIREADER_THREAD = False

@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/update_data', methods = ['GET'])
def update_data_main():
    #living room datas
    data = dbreader.get_last_row("olohuone")
    o_temp = str(data[0][1]) + "°C"
    o_humi = str(data[0][0]) + "%"
    o_pressure = str(data[0][2]) + "hPa"
    o_battery = str(data[0][3])
    o_updatet_temp = int(data[0][4])
    o_updatet = datetime.datetime.fromtimestamp(o_updatet_temp)

    #bedroom datas
    data = dbreader.get_last_row("makkari")
    print(data)
    m_temp = str(data[0][1]) + "°C"
    m_humi = str(data[0][0]) + "%"
    m_pressure = str(data[0][2]) + "hPa"
    m_battery = str(data[0][3])
    m_updatet_temp = int(data[0][4])
    m_updatet = datetime.datetime.fromtimestamp(m_updatet_temp)

    return jsonify(o_temp=o_temp, o_humi=o_humi, o_pressure=o_pressure, o_battery=o_battery, o_updatet=o_updatet, m_temp=m_temp, m_humi=m_humi, m_pressure=m_pressure, m_battery=m_battery, m_updatet=m_updatet)


@app.route('/o_olddata')
def view_o_olddata():
    history_data = dbreader.get_history("olohuone")
    return render_template("o_history.html", len=len(history_data), history_data=history_data)


@app.route('/m_olddata')
def view_m_olddata():
    history_data = dbreader.get_history("makkari")
    return render_template("o_history.html", len=len(history_data), history_data=history_data)


if __name__ == '__main__':
    if RUN_RUUVIREADER_THREAD:
        print("TODO")
    app.run(debug=True, host="0.0.0.0")
