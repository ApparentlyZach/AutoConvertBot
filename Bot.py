#This Bot was designed and coded by ApparentlyZach 2020.11.05
#This is my literal first coding project in Python, so the efficiency level is most likely a 1 out of 5 stars

import discord
from discord import Intents
import re
from discord.ext import commands
import json
from discord.ext.commands import bot

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
            global Value, Unit
            Provision = re.findall(r'\d+\s?[a-zA-Z]+', content)
            Value = re.sub(r'[^0-9]', "", str(Provision))
            Temp = int(Value)
            Value = round(Temp, 2)
            UnformattedUnit = re.sub(r'[^a-zA-Z]+', "", str(Provision))
            Unit = UnformattedUnit.lower()
            print("Value:", Value, " UnformattedUnit:", UnformattedUnit, " Unit:", Unit)
            await client.process_commands(message)
            await client.unit_conversion(Value, Unit, message)
        else:
            pass

    #Determine The Conversion Type and Convert
    @client.event
    async def unit_conversion(Value, Unit, message):
        if Unit == "c" or Unit == "f":#Temperature Conversion
            if Unit == "c":		# Celcius to Farenheit
                OriginalUnit="Celcius"
                ConvertedUnit="Farenheit"
                ConvertedValue = round(((Value * 1.8) + 32),2)
                await client.process_commands(message)
                await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
            elif Unit =="f":	# Farenheit to Celcius
                OriginalUnit="Farenheit"
                ConvertedUnit="Celcius"
                ConvertedValue = round(((Value - 32) / 1.8),2)
                await client.process_commands(message)
                await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
            else:
                pass
        elif Unit == "in" or Unit == "inch" or Unit == "inches" or Unit == "ft" or Unit == "foot" or Unit == "feet" or Unit == "yd" or Unit == "yard" or Unit == "yards" or Unit == "mi" or Unit == "mile" or Unit == "miles" or Unit == "mm" or Unit == "millimeter" or Unit == "millimeters" or Unit == "cm" or Unit == "centimeter" or Unit == "centimeters" or Unit == "m" or Unit == "meter" or Unit == "meters" or Unit == "km" or Unit == "kilometer" or Unit == "kilometers": #Length Conversion
            if Unit == "in" or Unit == "inch" or Unit == "inches" or Unit == "ft" or Unit == "foot" or Unit == "feet" or Unit == "yd" or Unit == "yard" or Unit == "yards" or Unit == "mi" or Unit == "mile" or Unit == "miles":	#SI to Metric
                if Unit == "in" or Unit == "inch" or Unit == "inches":	# Inches to Centimeters and/or Meters
                    OriginalUnit="Inch(es)"
                    ConvertedUnit="Centimeter(s)"
                    SimplifiedConvertedUnit="Meter(s)"
                    ConvertedValue = round((Value * 2.540),2)
                    SimplifiedConvertedValue = round(((Value * 2.540) / 100),2)
                    if ConvertedValue >= 100:
                    	await client.process_commands(message)
                    	await client.simplified_embed(OriginalUnit, SimplifiedConvertedUnit, Value, SimplifiedConvertedValue, Unit, message)
                    else:
                    	await client.process_commands(message)
                    	await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "ft" or Unit == "foot" or Unit == "feet":	# Feet to Centimeters and/or Meters
                    OriginalUnit="Foot/Feet"
                    ConvertedUnit="Centimeter(s)"
                    SimplifiedConvertedUnit="Meter(s)"
                    ConvertedValue = round(((Value * 12) * 2.540),2)
                    SimplifiedConvertedValue = round((((Value * 12) * 2.540) / 100),2)
                    if ConvertedValue >= 100:
                    	await client.process_commands(message)
                    	await client.simplified_embed(OriginalUnit, SimplifiedConvertedUnit, Value, SimplifiedConvertedValue, Unit, message)
                    else:
                    	await client.process_commands(message)
                    	await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "yd" or Unit == "yard" or Unit == "yards":	# Yards to Meters
                    OriginalUnit="Yard(s)"
                    ConvertedUnit="Meter(s)"
                    ConvertedValue = round((Value * 0.9144),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "mi" or Unit == "mile" or Unit == "miles":	# Miles to Kilometers
                    OriginalUnit="Mile(s)"
                    ConvertedUnit="Kilometer(s)"
                    ConvertedValue = round((Value * 1.60934),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    pass
            elif Unit == "mm" or Unit == "millimeter" or Unit == "millimeters" or Unit == "cm" or Unit == "centimeter" or Unit == "centimeters" or Unit == "m" or Unit == "meter" or Unit == "meters" or Unit == "km" or Unit == "kilometer" or Unit == "kilometers": #Metric to SI
                if Unit == "mm" or Unit == "millimeter" or Unit == "millimeters":		# Millimeters to Inches
                    OriginalUnit="Millimeter(s)"
                    ConvertedUnit="Inch(es)"
                    ConvertedValue = round((Value * 0.0393701),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "cm" or Unit == "centimeter" or Unit == "centimeters":	# Centimeters to Inches
                    OriginalUnit="Centimeter(s)"
                    ConvertedUnit="Inch(es)"
                    ConvertedValue = round((Value * 0.393701),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "m" or Unit == "meter" or Unit == "meters":				# Meters to Feet
                    OriginalUnit="Meter(s)"
                    ConvertedUnit="Feet"
                    ConvertedValue = round((Value * 3.28084),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "km" or Unit == "kilometer" or Unit == "kilometers":		# Kilometers to Miles
                    OriginalUnit="Kilometer(s)"
                    ConvertedUnit="Mile(s)"
                    ConvertedValue = round((Value * 0.621371),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    pass
            else:
                pass
        elif Unit == "lb" or Unit == "lbs" or Unit == "pound" or Unit == "pounds" or Unit == "ton" or Unit == "tons" or Unit == "g" or Unit == "gram" or Unit == "grams" or Unit == "kg" or Unit == "kilogram" or Unit == "kilograms" or Unit == "tonne" or Unit == "tonnes":
			#Weight Conversion
            if Unit == "lb" or Unit == "lbs" or Unit == "pound" or Unit == "pounds" or Unit == "ton" or Unit == "tons":	#SI to Metric
                if Unit == "lb" or Unit == "lbs" or Unit == "pound" or Unit == "pounds":	# Pounds to Kilograms
                    OriginalUnit="Pound(s)"
                    ConvertedUnit="Kilogram(s)"
                    ConvertedValue = round((Value * 0.453592),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "ton" or Unit == "tons":					# Ton to Tonne
                    OriginalUnit="Ton"
                    ConvertedUnit="Tonne"
                    ConvertedValue = round((Value * 0.907185),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    pass

            elif Unit == "g" or Unit == "gram" or Unit == "grams" or Unit == "kg" or Unit == "kilogram" or Unit == "kilograms" or Unit == "tonne" or Unit == "tonnes": #Metric to SI
                if Unit == "g" or Unit == "gram" or Unit == "grams":				# Grams to Ounces
                    OriginalUnit="Gram(s)"
                    ConvertedUnit="Dry Ounce(s)"
                    ConvertedValue = round((Value * 0.035274),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "kg" or Unit == "kilogram" or Unit == "kilograms":	# Kilograms to Pounds
                    OriginalUnit="Kilogram(s)"
                    ConvertedUnit="Pound(s)"
                    ConvertedValue = round((Value * 2.20462),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "tonne" or Unit == "tonnes":				# Tonne to Ton
                    OriginalUnit="Tonne"
                    ConvertedUnit="Ton"
                    ConvertedValue = round((Value * 1.10231),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    pass

            else:
                pass

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
                    	await client.process_commands(message)
                    	await client.simplified_embed(OriginalUnit, SimplifiedConvertedUnit, Value, SimplifiedConvertedValue, Unit, message)
                    else:
                    	await client.process_commands(message)
                    	await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)

                elif Unit == "pt" or Unit == "pint":		# Pint to Liters
                    OriginalUnit="Pint(s)"
                    ConvertedUnit="Liter(s)"
                    ConvertedValue = round((Value * 0.568261),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "qt" or Unit == "quart":		# Quart to Liters
                    OriginalUnit="Quart(s)"
                    ConvertedUnit="Liter(s)"
                    ConvertedValue = round((Value * 0.946353),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "gal" or Unit == "gallon":	# Gal to Liters
                    OriginalUnit="Gallon(s)"
                    ConvertedUnit="Liter(s)"
                    ConvertedValue = round((Value * 3.78541),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    pass

            elif Unit == "ml" or Unit == "milliliter" or Unit == "milliliters" or Unit == "l" or Unit == "liter" or Unit == "liters" or Unit == "litre" or Unit == "litres":	#Metric to SI
                if Unit == "ml" or Unit == "milliliter" or Unit == "milliliters":			# Millimeters to Fluid Ounces
                    OriginalUnit="Milliliter(s)"
                    ConvertedUnit="Fluid Ounce(s)"
                    ConvertedValue = round((Value * 0.033814),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                elif Unit == "l" or Unit == "liter" or Unit == "liters" or Unit == "litre" or Unit == "litres":	# Liters to Gallons
                    OriginalUnit="Liter(s)"
                    ConvertedUnit="Gallon(s)"
                    ConvertedValue = round((Value * 0.264172),2)
                    await client.process_commands(message)
                    await client.basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message)
                else:
                    pass
 
            else:
                pass

        elif Unit == "oz" or Unit == "ounce" or Unit == "ounces":	#Ounces Conversion as Ounces is Vague
            OriginalUnit="Ounce(s)"
            ConvertedDryUnit="Gram(s)"
            ConvertedLiquidUnit="Milliliter(s)"
            ConvertedDryValue = round((Value * 28.3495),2)
            SimplifiedConvertedDryValue = round(((Value * 28.3495) / 1000),2)
            ConvertedLiquidValue = round((Value * 29.5735),2)
            SimplifiedLiquidValue = round(((Value * 29.5735) / 1000),2)
            if ConvertedDryValue >= 1000:
                embed = discord.Embed(description="Converted...")
                embed.add_field(name=OriginalUnit + " to", value=Value, inline=True)
                embed.add_field(name="Kilogram(s) or", value=SimplifiedConvertedDryValue, inline=True)
                embed.add_field(name="Liter(s)", value=ConvertedLiquidValue, inline=True)
                await message.channel.send(embed=embed)
                Value = 0
                Unit = ""
            else:
                embed = discord.Embed(description="Converted...")
                embed.add_field(name=OriginalUnit + " to", value=Value, inline=True)
                embed.add_field(name=ConvertedDryUnit + " or", value=ConvertedDryValue, inline=True)
                embed.add_field(name=ConvertedLiquidUnit, value=ConvertedLiquidValue, inline=True)
                await message.channel.send(embed=embed)
                Value = 0
                Unit = ""
        else:
            print("no unit for automatic conversion found.")
			
			
	#Embed Responses
    @client.event
    async def basic_embed(OriginalUnit, ConvertedUnit, Value, ConvertedValue, Unit, message):
        embed = discord.Embed(description="Converted...")
        embed.add_field(name=OriginalUnit + " to", value=Value, inline=True)
        embed.add_field(name=ConvertedUnit, value=ConvertedValue, inline=True)
        await message.channel.send(embed=embed)
        Value = 0
        Unit = ""
	
    @client.event
    async def simplified_embed(OriginalUnit, SimplifiedConvertedUnit, Value, SimplifiedConvertedValue, Unit, message):
        embed = discord.Embed(description="Converted...")
        embed.add_field(name=OriginalUnit + " to", value=Value, inline=True)
        embed.add_field(name=SimplifiedConvertedUnit, value=SimplifiedConvertedValue, inline=True)
        await message.channel.send(embed=embed)
        Value = 0
        Unit = ""
		
client.run('<your_bot_token_here>') #Discord Bot Token
