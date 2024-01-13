import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',charset="utf8")
if mycon.is_connected()==False:
    print('ERROR')
cursor=mycon.cursor()

cursor.execute("create database if not exists ONLINE_MOBILE_SHOPPING ")
cursor.execute("use ONLINE_MOBILE_SHOPPING")
cursor.execute("create table if not exists phone(MOBILE_ID integer primary key,\
                                   MOBILE_NAME char(20),\
                                   OS char(20),\
                                   RAM char(20),\
                                   STORAGE char(20),\
                                   EXPANDABLE_STORAGE char(20),\
                                   MANUFACTURER char(20),\
                                   PRODUCT_DIMENSIONS char(20),\
                                   COLOUR char(20),\
                                   WIRELESS_COMMUNICATIONS_TECHNOLOGY char(50),\
                                   SPECIAL_FEATURES varchar(200),\
                                   DEVICE_INTERFACE char(20),\
                                   RESOLUTION char(20),\
                                   REAR_CAMERA_IN_MP integer,\
                                   FRONT_CAMERA_IN_MP integer,\
                                   WEIGHT_IN_GRAMS integer,\
                                   BATTERY_In_MAH integer,\
                                   IN_BOX BLOB,\
                                   STOCK integer,\
                                   RATINGS_OUT_OF_5 float (3,2),\
                                   PRICE float(8,2),\
                                   SHIPPING char(20))")

cursor.execute("insert into phone values(100,\
'MI_10',\
'Android',\
'8GB',\
'128GB',\
'NULL',\
'Xiaomi',\
'16.3*0.9*7.5cm',\
'coral_green',\
'Bluetooth;WiFi_Hotspot',\
'dual_SIM,GPS,Music_player,video_player,gyroscope,infrared,proximity_sensor,accelerometer,ambient_light_sensor',\
'touchscreen',\
'2340*1080',\
108,\
20,\
208,\
4780,\
'handset,power_adapter,USB_cable,SIM_eject_tool,warranty_card,user_guide_and_clear_soft_case',\
100,\
3.4,\
49999.00,\
'free_delievery')")
mycon.commit()

            
cursor.execute("insert into phone values(101,\
'REDMI_NOTE_8',\
'Android',\
'4GB',\
'128GB',\
'null',\
'Xiaomi',\
'15.3*0.8*7.5cm',\
'BLACK',\
'Bluetooth;WiFi_Hotspot',\
'dual_SIM,GPS,Music_player,video_player,gyroscope,infrared,proximity_sensor,accelerometer,ambient_light_sensor',\
'touchscreen',\
'2240*1080',\
48,\
13,\
190,\
4000,\
'handset,power_adapter,USB_cable,SIM_eject_tool,warranty_card,user_guide_and_clear_soft_case',\
120,\
4.5,\
12999.00,\
'free_delievery')")
mycon.commit()





cursor.execute("insert into phone values(102,\
'POCO F1',\
'Android',\
'8GB',\
'128GB',\
'512GB',\
'Xiaomi',\
'15.3*0.95*7.5cm',\
'graphite  black',\
'Bluetooth;WiFi_Hotspot',\
'dual SIM,GPS, Music player,video player,gyroscope,infrared,proximity sensor,accelerometer,ambient light sensor,e compass,phone talktime 32 hrs',\
'touchscreen',\
'2340*1080',\
108,\
20,\
208,\
4780,\
'handset,power adapter,USB cable,SIM eject tool,warranty card,user guide,tool and back case',\
100,\
3.4,\
49999.00,\
'free_delievery')")
mycon.commit()

cursor.execute("insert into phone values(103,\
'GALAXY A-30',\
'Android',\
'4GB',\
'64GB',\
'512GB',\
'Samsung',\
'15.8*0.8*7.5 cm',\
'prism crush white',\
'Bluetooth;WiFi Hotspot',\
'dual SIM,GPS, Music player,video player,proximity sensor,accelerometer,virtual light sensor',\
'touchscreen ',\
'720*1560',\
30,\
16,\
169,\
4000,\
'handset,earphones,travel adapter,USB cable,SIM eject tool,user guide',\
100,\
4.1,\
15896.00,\
'free dilevery')")
mycon.commit()

cursor.execute("insert into phone values(104,\
'GALAXY A51',\
'Android',\
'6GB',\
'128GB',\
'512GB',\
'Samsung',\
'15.9*0.8*7.4 cm',\
'blue',\
'Bluetooth;WiFi Hotspot',\
'dual SIM,GPS, Music player,video player,proximity sensor,accelerometer,virtual light sensor,e mail',\
'touchscreen,',\
'2400*1080',\
23,\
32,\
187,\
4000,\
'handset,earphones,travel adapter,USB cable,SIM eject tool,user guide',\
270,\
4.2,\
24999.00,\
'free dilevery')")
mycon.commit()

cursor.execute("insert into phone values(105,\
'GALAXY S20 Ultra',\
'Android',\
'12GB',\
'128GB',\
'1TB',\
'Samsung',\
'16.7*0.9*7.6 cm',\
'cosmic grey',\
'Bluetooth;WiFi Hotspot',\
'dual SIM,GPS, Music player,video player,proximity sensor,accelerometer,virtual light sensor',\
'touchscreen,',\
'3200*1440',\
108,\
40,\
220,\
5000,\
'handset,earphones,travel adapter,USB cable,SIM eject tool,user guide, non removable battery',\
220,\
3.9,\
97999.00,\
'free dilevery')")
mycon.commit()

cursor.execute("insert into phone values(106,\
'VIVO Y91i',\
'Android',\
'2GB',\
'32GB',\
'256GB',\
'Vivo',\
'15.5*0.8*7.5 cm',\
'ocean blue',\
'Bluetooth;WiFi Hotspot',\
'dual SIM,GPS, Music player,video player,proximity sensor,accelerometer,ambient light sensor,e compass,virtual gyroscope,fingerprint',\
'touchscreen,',\
'1520*720',\
13,\
5,\
164,\
4030,\
'handset,earphones,travel adapter,USB cable,USB power adaptor,SIM eject tool,user guide,protective case and film',\
900,\
4.1,\
7999.00,\
'free dilevery')")
mycon.commit()

cursor.execute("insert into phone values(107,\
'VIVO V17',\
'Android',\
'8GB',\
'128GB',\
'256GB',\
'Vivo',\
'15.9*0.9*7.4 cm',\
'midnight ocean',\
'Bluetooth;WiFi Hotspot',\
'dual SIM,GPS, Music player,video player,proximity sensor,accelerometer,ambient light sensor,e compass,virtual gyroscope,fingerprint',\
'touchscreen,',\
'1520*720',\
60,\
32,\
176,\
4500,\
'handset,earphones,travel adapter,USB cable,USB power adaptor,SIM eject tool,user guide,protective case and film',\
1000,\
4.4,\
24990.00,\
'free dilevery')")
mycon.commit()

cursor.execute("insert into phone values(108,\
'OPPO A11k',\
'Android',\
'2GB',\
'32GB',\
'256GB',\
'Oppo',\
'15.6*0.8*7.6 cm',\
'flowing silver',\
'Bluetooth;WiFi Hotspot',\
'dual SIM,GPS, Music player,video player,FM radio,fingerprint',\
'touchscreen,',\
'1520*720',\
15,\
5,\
165,\
4230,\
'handset,earphones,travel adapter,USB cable,USB power adaptor,SIM eject tool,user guide,protective case,warranty card',\
100,\
3.9,\
8990.00,\
'free dilevery')")
mycon.commit()

cursor.execute("insert into phone values(109,\
'OPPO Reno3 Pro',\
'Android',\
'8GB',\
'128GB',\
'256GB',\
'Oppo',\
'15.9*0.8*7.3 cm',\
'midnight black',\
'Bluetooth;WiFi Hotspot',\
'dual SIM,GPS, Music player,video player,FM radio,fingerprint',\
'touchscreen,',\
'2400*1080',\
64,\
44,\
175,\
4020,\
'handset,earphones,travel adapter,USB cable,USB power adaptor,SIM eject tool,user guide,protective case,warranty card,talktime 32 hrs',\
100,\
3.7,\
31990.00,\
'free dilevery')")
mycon.commit()

cursor.execute("insert into phone values(110,\
'IPHONE Xs',\
'IOS',\
'64GB',\
'256GB',\
'512GB',\
'Apple',\
'15.8*0.8*7.7 cm',\
'gold',\
'Bluetooth;WiFi Hotspot',\
'dual SIM,GPS, Music player,video player,depth control,all glass and stainless steel,water and dust resistant,fingerprint,face sensitivity',\
'touchscreen,',\
'4000*1080',\
24,\
7,\
208,\
4500,\
'handset,earpods with lightning connector,USB cable,USB power adaptor,user guide,protective case,warranty card',\
500,\
4.3,\
69990.00,\
'free dilevery')")
mycon.commit()
cursor.execute("create table if not exists USERS(GMAIL_ACCOUNT char(50) primary key,\
PASSWORD CHAR(20) NOT NULL,\
name char(30),\
MOBILE_NUMBER varchar(30) unique NOT NULL,\
city char(50),\
address char(60))")
mycon.commit()
########################################################################################################################################################
cursor.execute("insert into USERS values('ajaysingh@gmail.com',\
'ajaysingh',\
'Ajay Singh',\
'9982551867',\
'Ajmer',\
'72,SG Road,Ajmer')")
cursor.execute("insert into users values('shrutisinha12@gmail.com',\
'039735s',\
'Shruti Sinha',\
'9739163094',\
'Jodhpur',\
'16,Shastri Nagar,Jodhpur')")
cursor.execute("insert into users values('ali89@yahoo.com',\
'ali89',\
'Mahummad Ali Khan',\
'8873924109',\
'Jaipur',\
'44,Ramganj,Jaipur')")
mycon.commit()
