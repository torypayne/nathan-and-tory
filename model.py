import requests
import json
from pprint import pprint
import config




def request_temperature(city):
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city)
	r = json.loads(r.text)
	# pprint(r)
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


def get_nathan_temp():
	weather_dict = request_temperature("wurtulla")
	k_temp = pull_temp_from_json(weather_dict)
	c_temp = convert_k_to_c(k_temp)
	f_temp = convert_c_to_f(c_temp)
	c_temp = round(c_temp)
	f_temp = round(f_temp)
	temp_dict = {"f": f_temp, "c": c_temp}
	return temp_dict


def get_tory_temp():
	weather_dict = request_temperature("sanfrancisco")
	k_temp = pull_temp_from_json(weather_dict)
	c_temp = convert_k_to_c(k_temp)
	f_temp = convert_c_to_f(c_temp)
	c_temp = round(c_temp)
	f_temp = round(f_temp)
	temp_dict = {"f": f_temp, "c": c_temp}
	return temp_dict