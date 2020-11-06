#This Bot was designed and coded by ApparentlyZach 2020.11.05
#This is my literal first coding project in Python, so the efficiency level is most likely a 1 out of 5 stars

from typing import Counter
import discord
from discord import Intents
import re
from discord.ext import commands
import json
from discord.ext.commands import bot
import time

intents = Intents.all()

#Variables
ConvertedUnit = ""
Value = 0
Unit = ""

#Events
@client.event
async def on_ready():
    print('Bot is Ready.')

class Conversions:

    #Inbound Message and Setup of Initial Variables
    @client.event
    async def on_message(message):
        content = message.content
        if not message.author.bot:
            await client.process_commands(message)
            global Value, Unit
            count = re.findall(r'\d+\s?[a-zA-Z]+', content)
            counter = len(count)
            if len(count) > 1:
                for iteration in re.finditer(r'\d+\s?[a-zA-Z]+', content):
                    print(iteration)
                    Provision = iteration.group()
                    Value = re.sub(r'[^0-9]', "", str(Provision))
                    Temp = int(Value)
                    Value = round(Temp, 2)
                    UnformattedUnit = re.sub(r'[^a-zA-Z]+', "", str(Provision))
                    Unit = UnformattedUnit.lower()
                    print("Value:", Value, " UnformattedUnit:", UnformattedUnit, " Unit:", Unit, "Loop")
                    await client.process_commands(message)
                    await client.unit_conversion(Value, Unit, message)
            elif len(count) == 1:
                Provision = count
                Value = re.sub(r'[^0-9]', "", str(Provision))
                Temp = int(Value)
                Value = round(Temp, 2)
                UnformattedUnit = re.sub(r'[^a-zA-Z]+', "", str(Provision))
                Unit = UnformattedUnit.lower()
                print("Value:", Value, " UnformattedUnit:", UnformattedUnit, " Unit:", Unit,"Single")
                await client.process_commands(message)
                await client.unit_conversion(Value, Unit, message)
            else:
                print("nothing matching REGEX found.")
        else:
            print("Bot said something.")

    #Determine The Conversion Type and Convert
    @client.event
    async def unit_conversion(Value, Unit, message):
        if Unit == "c" or Unit == "f":#Temperature Conversion
            if Unit == "c":		# Celcius to Farenheit
                OriginalUnit="Celcius"
                ConvertedUnit="Farenheit"
                ConvertedValue = round(((Value * 1.8) + 32),2)
                print("Converted C to F")
                await client.process_commands(message)
                await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
            elif Unit =="f":	# Farenheit to Celcius
                OriginalUnit="Farenheit"
                ConvertedUnit="Celcius"
                ConvertedValue = round(((Value - 32) / 1.8),2)
                print("Converted F to C")
                await client.process_commands(message)
                await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
            else:
                print("Something went wrong (Temp Conv)")
        elif Unit == "in" or Unit == "inch" or Unit == "inches" or Unit == "ft" or Unit == "foot" or Unit == "feet" or Unit == "yd" or Unit == "yard" or Unit == "yards" or Unit == "mi" or Unit == "mile" or Unit == "miles" or Unit == "mm" or Unit == "millimeter" or Unit == "millimeters" or Unit == "cm" or Unit == "centimeter" or Unit == "centimeters" or Unit == "m" or Unit == "meter" or Unit == "meters" or Unit == "km" or Unit == "kilometer" or Unit == "kilometers": #Length Conversion
            if Unit == "in" or Unit == "inch" or Unit == "inches" or Unit == "ft" or Unit == "foot" or Unit == "feet" or Unit == "yd" or Unit == "yard" or Unit == "yards" or Unit == "mi" or Unit == "mile" or Unit == "miles":	#SI to Metric
                if Unit == "in" or Unit == "inch" or Unit == "inches":	# Inches to Centimeters and/or Meters
                    OriginalUnit="Inch(es)"
                    ConvertedUnit="Centimeter(s)"
                    SimplifiedConvertedUnit="Meter(s)"
                    ConvertedValue = round((Value * 2.540),2)
                    SimplifiedConvertedValue = round(((Value * 2.540) / 100),2)
                    if ConvertedValue >= 100:
                        print("Converted In to M")
                        await client.process_commands(message)
                        await client.simplified_embed(OriginalUnit, SimplifiedConvertedUnit, Value, SimplifiedConvertedValue, Unit, message)
                    else:
                        print("Converted In to Cm")
                        await client.process_commands(message)
                        await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "ft" or Unit == "foot" or Unit == "feet":	# Feet to Centimeters and/or Meters
                    OriginalUnit="Foot/Feet"
                    ConvertedUnit="Centimeter(s)"
                    SimplifiedConvertedUnit="Meter(s)"
                    ConvertedValue = round(((Value * 12) * 2.540),2)
                    SimplifiedConvertedValue = round((((Value * 12) * 2.540) / 100),2)
                    if ConvertedValue >= 100:
                        print("Converted Ft to M")
                        await client.process_commands(message)
                        await client.simplified_embed(OriginalUnit, SimplifiedConvertedUnit, Value, SimplifiedConvertedValue, Unit, message)
                    else:
                        print("Converted Ft to Cm")
                        await client.process_commands(message)
                        await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "yd" or Unit == "yard" or Unit == "yards":	# Yards to Meters
                    OriginalUnit="Yard(s)"
                    ConvertedUnit="Meter(s)"
                    ConvertedValue = round((Value * 0.9144),2)
                    print("Converted Yd to M")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "mi" or Unit == "mile" or Unit == "miles":	# Miles to Kilometers
                    OriginalUnit="Mile(s)"
                    ConvertedUnit="Kilometer(s)"
                    ConvertedValue = round((Value * 1.60934),2)
                    print("Converted Mi to Km")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    print("Something went wrong (Distance Conv - SI>M)")
            elif Unit == "mm" or Unit == "millimeter" or Unit == "millimeters" or Unit == "cm" or Unit == "centimeter" or Unit == "centimeters" or Unit == "m" or Unit == "meter" or Unit == "meters" or Unit == "km" or Unit == "kilometer" or Unit == "kilometers": #Metric to SI
                if Unit == "mm" or Unit == "millimeter" or Unit == "millimeters":		# Millimeters to Inches
                    OriginalUnit="Millimeter(s)"
                    ConvertedUnit="Inch(es)"
                    ConvertedValue = round((Value * 0.0393701),2)
                    print("Converted Mm to In")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "cm" or Unit == "centimeter" or Unit == "centimeters":	# Centimeters to Inches
                    OriginalUnit="Centimeter(s)"
                    ConvertedUnit="Inch(es)"
                    ConvertedValue = round((Value * 0.393701),2)
                    print("Converted Cm to In")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "m" or Unit == "meter" or Unit == "meters":				# Meters to Feet
                    OriginalUnit="Meter(s)"
                    ConvertedUnit="Feet"
                    ConvertedValue = round((Value * 3.28084),2)
                    print("Converted M to Ft")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "km" or Unit == "kilometer" or Unit == "kilometers":		# Kilometers to Miles
                    OriginalUnit="Kilometer(s)"
                    ConvertedUnit="Mile(s)"
                    ConvertedValue = round((Value * 0.621371),2)
                    print("Converted Km to Mi")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    print("Something went wrong (Distance Conv - M>SI)")
            else:
                print("Something went wrong (Distance Conv)")
        elif Unit == "lb" or Unit == "lbs" or Unit == "pound" or Unit == "pounds" or Unit == "ton" or Unit == "tons" or Unit == "g" or Unit == "gram" or Unit == "grams" or Unit == "kg" or Unit == "kilogram" or Unit == "kilograms" or Unit == "tonne" or Unit == "tonnes":
			#Weight Conversion
            if Unit == "lb" or Unit == "lbs" or Unit == "pound" or Unit == "pounds" or Unit == "ton" or Unit == "tons":	#SI to Metric
                if Unit == "lb" or Unit == "lbs" or Unit == "pound" or Unit == "pounds":	# Pounds to Kilograms
                    OriginalUnit="Pound(s)"
                    ConvertedUnit="Kilogram(s)"
                    ConvertedValue = round((Value * 0.453592),2)
                    print("Converted Lb to Kg")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "ton" or Unit == "tons":					# Ton to Tonne
                    OriginalUnit="Ton"
                    ConvertedUnit="Tonne"
                    ConvertedValue = round((Value * 0.907185),2)
                    print("Converted Ton to Tonne")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    print("Something went wrong (Weight Conv - SI>M)")

            elif Unit == "g" or Unit == "gram" or Unit == "grams" or Unit == "kg" or Unit == "kilogram" or Unit == "kilograms" or Unit == "tonne" or Unit == "tonnes": #Metric to SI
                if Unit == "g" or Unit == "gram" or Unit == "grams":				# Grams to Ounces
                    OriginalUnit="Gram(s)"
                    ConvertedUnit="Dry Ounce(s)"
                    ConvertedValue = round((Value * 0.035274),2)
                    print("Converted G to Oz")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "kg" or Unit == "kilogram" or Unit == "kilograms":	# Kilograms to Pounds
                    OriginalUnit="Kilogram(s)"
                    ConvertedUnit="Pound(s)"
                    ConvertedValue = round((Value * 2.20462),2)
                    print("Converted Kg to Lb")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "tonne" or Unit == "tonnes":				# Tonne to Ton
                    OriginalUnit="Tonne"
                    ConvertedUnit="Ton"
                    ConvertedValue = round((Value * 1.10231),2)
                    print("Converted Tonne to Ton")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    print("Something went wrong (Weight Conv - M>SI)")

            else:
                print("Something went wrong (Weight Conv)")

        elif Unit == "cup" or Unit == "pt" or Unit == "pint" or Unit == "qt" or Unit == "quart" or Unit == "gal" or Unit == "gallon" or Unit == "ml" or Unit == "milliliter" or Unit == "milliliters" or Unit == "l" or Unit == "liter" or Unit == "liters" or Unit == "litre" or Unit == "litres":
            #Volume Conversion
            if Unit == "cup" or Unit == "pt" or Unit == "pint" or Unit == "qt" or Unit == "quart" or Unit == "gal" or Unit == "gallon": #SI to Metric
                if Unit == "cup":				# Cup to Milliliters or Liters
                    OriginalUnit="Cup(s)"
                    ConvertedUnit="Milliliter(s)"
                    SimplifiedConvertedUnit="Liter(s)"
                    ConvertedValue = round((Value * 236.588),2)
                    SimplifiedConvertedValue = round(((Value * 236.588) / 1000),2)
                    if ConvertedValue >=1000:
                        print("Converted Cup to L")
                        await client.process_commands(message)
                        await client.simplified_embed(OriginalUnit, SimplifiedConvertedUnit, Value, SimplifiedConvertedValue, Unit, message)
                    else:
                        print("Converted Cuo to Ml")
                        await client.process_commands(message)
                        await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)

                elif Unit == "pt" or Unit == "pint":		# Pint to Liters
                    OriginalUnit="Pint(s)"
                    ConvertedUnit="Liter(s)"
                    ConvertedValue = round((Value * 0.568261),2)
                    print("Converted Pt to L")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "qt" or Unit == "quart":		# Quart to Liters
                    OriginalUnit="Quart(s)"
                    ConvertedUnit="Liter(s)"
                    ConvertedValue = round((Value * 0.946353),2)
                    print("Converted Qt to L")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "gal" or Unit == "gallon":	# Gal to Liters
                    OriginalUnit="Gallon(s)"
                    ConvertedUnit="Liter(s)"
                    ConvertedValue = round((Value * 3.78541),2)
                    print("Converted Gal to L")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    print("Something went wrong (Volume Conv - SI>M)")

            elif Unit == "ml" or Unit == "milliliter" or Unit == "milliliters" or Unit == "l" or Unit == "liter" or Unit == "liters" or Unit == "litre" or Unit == "litres":	#Metric to SI
                if Unit == "ml" or Unit == "milliliter" or Unit == "milliliters":			# Millimeters to Fluid Ounces
                    OriginalUnit="Milliliter(s)"
                    ConvertedUnit="Fluid Ounce(s)"
                    ConvertedValue = round((Value * 0.033814),2)
                    print("Converted Ml to Fl Oz")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "l" or Unit == "liter" or Unit == "liters" or Unit == "litre" or Unit == "litres":	# Liters to Gallons
                    OriginalUnit="Liter(s)"
                    ConvertedUnit="Gallon(s)"
                    ConvertedValue = round((Value * 0.264172),2)
                    print("Converted L to Gal")
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    print("Something went wrong (Volume Conv - M>SI)")
 
            else:
                print("Something went wrong (Volume Conv)")

        elif Unit == "oz" or Unit == "ounce" or Unit == "ounces":	#Ounces Conversion as Ounces is Vague
            OriginalUnit="Ounce(s)"
            ConvertedDryUnit="Gram(s)"
            ConvertedLiquidUnit="Milliliter(s)"
            ConvertedDryValue = round((Value * 28.3495),2)
            SimplifiedConvertedDryValue = round(((Value * 28.3495) / 1000),2)
            ConvertedLiquidValue = round((Value * 29.5735),2)
            SimplifiedLiquidValue = round(((Value * 29.5735) / 1000),2)
            if ConvertedDryValue >= 1000:
                print("Converted Oz to Kg or L")
                embed = discord.Embed(description="Converted...")
                embed.add_field(name=OriginalUnit + " to", value=Value, inline=True)
                embed.add_field(name="Kilogram(s) or", value=SimplifiedConvertedDryValue, inline=True)
                embed.add_field(name="Liter(s)", value=ConvertedLiquidValue, inline=True)
                await message.channel.send(embed=embed)
                Value = 0
                Unit = ""
            else:
                print("Converted Oz to G or Ml")
                embed = discord.Embed(description="Converted...")
                embed.add_field(name=OriginalUnit + " to", value=Value, inline=True)
                embed.add_field(name=ConvertedDryUnit + " or", value=ConvertedDryValue, inline=True)
                embed.add_field(name=ConvertedLiquidUnit, value=ConvertedLiquidValue, inline=True)
                await message.channel.send(embed=embed)
                Value = 0
                Unit = ""
        else:
            print("Something went wrong with the conversion or Unit recognition")
			
			
	#Embed Responses
    @client.event
    async def basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message):
        embed = discord.Embed(description="Converted...")
        embed.add_field(name=OriginalUnit + " to", value=Value, inline=True)
        embed.add_field(name=ConvertedUnit, value=ConvertedValue, inline=True)
        await client.process_commands(message)
        await message.channel.send(embed=embed)
        Value = 0
        Unit = ""
	
 
    @client.event
    async def simplified_embed(OriginalUnit, SimplifiedConvertedUnit, Value, SimplifiedConvertedValue, Unit, message):
        embed = discord.Embed(description="Converted...")
        embed.add_field(name=OriginalUnit + " to", value=Value, inline=True)
        embed.add_field(name=SimplifiedConvertedUnit, value=SimplifiedConvertedValue, inline=True)
        await client.process_commands(message)
        await message.channel.send(embed=embed)
        Value = 0
        Unit = ""

client.run('<YOUR_BOT_TOKEN_HERE>') #Discord Bot Token
