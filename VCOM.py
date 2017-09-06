#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  VCOM.py
#  
#  Copyright 2017 Salvatore Bruccoleri <salvatorebrk@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


class vcom(object):
	''' Class Vcom Vostalpine - Loop on Modbus'''
	
	def __init__(self):
		self.ID_device="None"
		self.IP_device='0.0.0.0'
		self.Port="0000"
		self.Version="v 1.0 on ModBus"
		self.Register_ACTUAL=[["LOOP1_ZONE_NUM", 0X0000 , 0],
							["LOOP1_SEQ_NUM" , 0X0001 , 0],
							["LOOP2_ZONE_NUM", 0X0002 , 0],
							["LOOP2_SEQ_NUM" , 0X0003 , 0],
							["LOOP3_ZONE_NUM", 0X0004 , 0],
							["LOOP3_SEQ_NUM" , 0X0005 , 0],
							["LOOP4_ZONE_NUM", 0X0006 , 0],
							["LOOP4_SEQ_NUM" , 0X0007 , 0],
							# LOOP 1 VEHICLE DATA
							["LOOP1_TYPE" , 0x0010 , 0],		# Vehicle type
							["LOOP1_LINE" , 0X0011 , 0],		# Line number
							["LOOP1_SRV_NUM",0x0012 , 0],		# Vehicle service number (Route)
							["LOOP1_CP" , 0X0013 , 0],			# 6BYTE Category (high byte) Punctuality (low byte) 
							["LOOP1_STUFF_H",0x0014 , 0],		# STUFF NUMBER HIGH
							["LOOP1_STUFF_L",0X0015 , 0],		# STUFF NUMBER LOW
							["LOOP1_FLEET_H",0x0016 , 0],		# Fleet number (high word)
							["LOOP1_FLEET_L",0X0017 , 0],		# Fleet number (low word)
							["LOOP1_M_CTRL", 0X0018 , 0],		# Manual control 
							["LOOP1_DIA_CNT",0x0019 , 0],		# Diagnostic count 
							# LOOP 2 VEHICLE DATA
							["LOOP2_TYPE" , 0x0020 , 0],		# Vehicle type
							["LOOP2_LINE" , 0X0021 , 0],		# Line number
							["LOOP2_SRV_NUM",0x0022 , 0],		# Vehicle service number (Route)
							["LOOP2_CP" , 0X0023 , 0],			# 6BYTE Category (high byte) Punctuality (low byte) 
							["LOOP2_STUFF_H",0x0024 , 0],		# STUFF NUMBER HIGH
							["LOOP2_STUFF_L",0X0025 , 0],		# STUFF NUMBER LOW
							["LOOP2_FLEET_H",0x0026 , 0],		# Fleet number (high word)
							["LOOP2_FLEET_L",0X0027 , 0],		# Fleet number (low word)
							["LOOP2_M_CTRL", 0X0028 , 0],		# Manual control 
							["LOOP2_DIA_CNT",0x0029 , 0],		# Diagnostic count 
							# LOOP 3 VEHICLE DATA
							["LOOP3_TYPE" , 0x0030 , 0],		# Vehicle type
							["LOOP3_LINE" , 0X0031 , 0],		# Line number
							["LOOP3_SRV_NUM",0x032 , 0],		# Vehicle service number (Route)
							["LOOP3_CP" , 0X0033 , 0],			# 6BYTE Category (high byte) Punctuality (low byte) 
							["LOOP3_STUFF_H",0x0034 , 0],		# STUFF NUMBER HIGH
							["LOOP3_STUFF_L",0X0035 , 0],		# STUFF NUMBER LOW
							["LOOP3_FLEET_H",0x0036 , 0],		# Fleet number (high word)
							["LOOP3_FLEET_L",0X0037 , 0],		# Fleet number (low word)
							["LOOP3_M_CTRL", 0X0038 , 0],		# Manual control 
							["LOOP3_DIA_CNT",0x0039 , 0],		# Diagnostic count
							# LOOP 4 VEHICLE DATA
							["LOOP4_TYPE" , 0x0040 , 0],		# Vehicle type
							["LOOP4_LINE" , 0X0041 , 0],		# Line number
							["LOOP4_SRV_NUM",0x0042 , 0],		# Vehicle service number (Route)
							["LOOP4_CP" , 0X0043 , 0],			# 6BYTE Category (high byte) Punctuality (low byte) 
							["LOOP4_STUFF_H",0x0044 , 0],		# STUFF NUMBER HIGH
							["LOOP4_STUFF_L",0X0045 , 0],		# STUFF NUMBER LOW
							["LOOP4_FLEET_H",0x0046 , 0],		# Fleet number (high word)
							["LOOP4_FLEET_L",0X0047 , 0],		# Fleet number (low word)
							["LOOP4_M_CTRL", 0X0048 , 0],		# Manual control 
							["LOOP4_DIA_CNT",0x0049 , 0],		# Diagnostic count  
							]
		self.Register_STORED=[
							# LOOP 1 VEHICLE DATA
							["LOOP1_TYPE" , 0x0050 , 0],		# Vehicle type
							["LOOP1_LINE" , 0X0051 , 0],		# Line number
							["LOOP1_SRV_NUM",0x0052 , 0],		# Vehicle service number (Route)
							["LOOP1_CP" , 0X0053 , 0],			# 6BYTE Category (high byte) Punctuality (low byte) 
							["LOOP1_STUFF_H",0x0054 , 0],		# STUFF NUMBER HIGH
							["LOOP1_STUFF_L",0X0055 , 0],		# STUFF NUMBER LOW
							["LOOP1_FLEET_H",0x0056 , 0],		# Fleet number (high word)
							["LOOP1_FLEET_L",0X0057 , 0],		# Fleet number (low word)
							["LOOP1_M_CTRL", 0X0058 , 0],		# Manual control 
							["LOOP1_DIA_CNT",0x0059 , 0],		# Diagnostic count 
							# LOOP 2 VEHICLE DATA
							["LOOP2_TYPE" , 0x0060 , 0],		# Vehicle type
							["LOOP2_LINE" , 0X0061 , 0],		# Line number
							["LOOP2_SRV_NUM",0x0062 , 0],		# Vehicle service number (Route)
							["LOOP2_CP" , 0X0063 , 0],			# 6BYTE Category (high byte) Punctuality (low byte) 
							["LOOP2_STUFF_H",0x0064 , 0],		# STUFF NUMBER HIGH
							["LOOP2_STUFF_L",0X0065 , 0],		# STUFF NUMBER LOW
							["LOOP2_FLEET_H",0x0066 , 0],		# Fleet number (high word)
							["LOOP2_FLEET_L",0X0067 , 0],		# Fleet number (low word)
							["LOOP2_M_CTRL", 0X0068 , 0],		# Manual control 
							["LOOP2_DIA_CNT",0x0069 , 0],		# Diagnostic count 
							# LOOP 3 VEHICLE DATA
							["LOOP3_TYPE" , 0x0070 , 0],		# Vehicle type
							["LOOP3_LINE" , 0X0071 , 0],		# Line number
							["LOOP3_SRV_NUM",0x072 , 0],		# Vehicle service number (Route)
							["LOOP3_CP" , 0X0073 , 0],			# 6BYTE Category (high byte) Punctuality (low byte) 
							["LOOP3_STUFF_H",0x0074 , 0],		# STUFF NUMBER HIGH
							["LOOP3_STUFF_L",0X0075 , 0],		# STUFF NUMBER LOW
							["LOOP3_FLEET_H",0x0076 , 0],		# Fleet number (high word)
							["LOOP3_FLEET_L",0X0077 , 0],		# Fleet number (low word)
							["LOOP3_M_CTRL", 0X0078 , 0],		# Manual control 
							["LOOP3_DIA_CNT",0x0079 , 0],		# Diagnostic count
							# LOOP 4 VEHICLE DATA
							["LOOP4_TYPE" , 0x0080 , 0],		# Vehicle type
							["LOOP4_LINE" , 0X0081 , 0],		# Line number
							["LOOP4_SRV_NUM",0x0082 , 0],		# Vehicle service number (Route)
							["LOOP4_CP" , 0X0083 , 0],			# 6BYTE Category (high byte) Punctuality (low byte) 
							["LOOP4_STUFF_H",0x0084 , 0],		# STUFF NUMBER HIGH
							["LOOP4_STUFF_L",0X0085 , 0],		# STUFF NUMBER LOW
							["LOOP4_FLEET_H",0x0086 , 0],		# Fleet number (high word)
							["LOOP4_FLEET_L",0X0087 , 0],		# Fleet number (low word)
							["LOOP4_M_CTRL", 0X0088 , 0],		# Manual control 
							["LOOP4_DIA_CNT",0x0089 , 0],		# Diagnostic count  
							]
	def readValue(self,reg):
		for item in self.Register_STORED:
			if(item[0]==reg):
				print item[2]

	def getValue(self,reg,data):
		for item in self.Register_STORED:
			if(item[0]==reg):
				item[2]=data