import requests
import json
from pprint import pprint
import pytz
import datetime


def request_temperature(city):
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city)
	r = json.loads(r.text)
	pprint(r)
	return r

def pull_temp_from_json(weather_dict):
	k_temp = weather_dict["main"]["temp"]
	return k_temp

def convert_k_to_c(k_temp):
	# Subtract 273.15
	c_temp = k_temp - 273.15
	return c_temp

def convert_c_to_f(c_temp):
# 	Multiply by 9, then divide by 5, then add 32
	f_temp = (c_temp * 9/5) + 32
	return f_temp

def human_readable_temp_dict(city):
	weather_dict = request_temperature(city)
	weather = weather_dict["weather"][0]["description"].capitalize()
	k_temp = pull_temp_from_json(weather_dict)
	c_temp = convert_k_to_c(k_temp)
	f_temp = convert_c_to_f(c_temp)
	c_temp = int(round(c_temp))
	f_temp = int(round(f_temp))
	temp_dict = {"f": f_temp, "c": c_temp, "weather": weather}
	return temp_dict	

def get_nathan_temp():
	temp_dict = human_readable_temp_dict("wurtulla")
	return temp_dict


def get_tory_temp():
	temp_dict = human_readable_temp_dict("sanfrancisco")
	return temp_dict

def create_time_dict(time):
	time_dict = {"day": time.strftime("%A"), "date": time.strftime("%d %B"), "hour": time.strftime("%I:%M %p")}
	return time_dict


def get_nathan_time():
	nathan_time = datetime.datetime.now(pytz.timezone('Australia/Brisbane'))
	nathan_time = create_time_dict(nathan_time)
	return nathan_time

def get_tory_time():
	tory_time = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
	tory_time = create_time_dict(tory_time)
	return tory_time

