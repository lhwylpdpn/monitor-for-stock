#coding:utf-8
import threading
import urllib
import urllib.request
import csv
import pymysql
import time
import os
import math
import scipy.stats
import time
import random

def load_sql():
	stockid=[]
	time_=[]
	close_=[]
	norm_open=[]
	norm_cha_open=[]
	close_time_=[]
	time_2=[]
	sql="SELECT a.stockid,UNIX_TIMESTAMP(DATE_FORMAT(CONCAT(a.date,' ',a.time),'%Y.%m.%d %H:%i')) AS time_,a.close,b.norm_open,b.norm_cha_open,!ISNULL(b.a) AS a , b.c FROM (SELECT * FROM `stock` WHERE stockid='GBPAUDpro') a LEFT JOIN (SELECT stockid,norm_open,norm_cha_open,DATE_FORMAT(order_time_send,'%Y.%m.%d') a ,  DATE_FORMAT(order_time_send,'%h:%i') b ,DATE_FORMAT(b.closeA_time,'%Y.%m.%d %h:%i') AS c FROM `order` a ,`order_result` b WHERE stockid='GBPAUDpro' AND a.`orderid`=b.`ln_e_close`) b ON a.stockid=b.stockid AND a.date=b.a AND a.time=b.b;"
	cur_stock.execute(sql)
	res=cur_stock.fetchall()
	for r in res:
		if len(res)>0:
			stockid.append(str(r[0]))
			time_.append(str(r[1])+"000")
			close_.append(str(r[2]))
			norm_open.append(str(r[3]))
			norm_cha_open.append(str(r[4]))
			close_time_.append(str(r[6]))
	write_json(time_,close_,"E:/BaiduYunDownload/phpStudy/WWW/EB3C3B239AFB8B62B7EC3451D269EB1E/MQL4/Files/json/test.json")
	for r in range(len(norm_open)):
		if norm_open[r]!="None":
			time_2.append(time_[r])
	write_json(time_2,time_2,"E:/BaiduYunDownload/phpStudy/WWW/EB3C3B239AFB8B62B7EC3451D269EB1E/MQL4/Files/json/test2.json")
def write_json(time_,value,path):
	file_object = open(path,'w')
	json=""

	file_object.write("[")
	for r in range(len(value)):

		if r<len(value)-1:
			json=json+"["+str(time_[r])+","+str(value[r])+"]\n,"
		else:
			json=json+"["+str(time_[r])+","+str(value[r])+"]\n"
	file_object.write(json)
	file_object.write("\n]")
	file_object.close()

							
if __name__ == "__main__":


	conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='fenxi',port=3306)
	cur_stock=conn.cursor()

	load_sql()

	cur_stock.close()

	conn.close()
		

	# conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='stock_foreign',port=3306)
	# cur_stock=conn.cursor()
	# cur_result=conn.cursor()
	# cur_d=conn.cursor()
	# cur_check=conn.cursor()
	# cur_result_DB=conn.cursor()
	# cur_stock_releation=conn.cursor()
	# releation_mid(100,"releation_mid")
	# cur_result.close()
	# cur_d.close()
	# cur_check.close()
	# cur_result_DB.close()
	# cur_stock_releation.close()
	# conn.commit()
	# conn.close()