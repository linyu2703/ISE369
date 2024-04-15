import os
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import pandas as pd
import numpy as np

os.getcwd() #original directory
os.chdir('/Users/yulin/Downloads') #changed directory
print(os.getcwd()) #new directory

df = gpd.read_file('ca_cong_adopted_2021') #imported file and read as geopandas

df.to_file('myJson.geojson', driver='GeoJSON') #converted to geoJSON file
df_gj = gpd.read_file('myJson.geojson')

cali=folium.Map(location=(42.9525, -76.01667), zoom_start=7) #testing folium and geoJSON
folium.GeoJson(df_gj).add_to(cali)
cali.save("cali.html")

df1 = df.copy() #copied geoDataFrame into a separate variable
df2= pd.DataFrame(df1) #turn geopandasDataFrame to pandasDataFrame
df3 = df2[['DISTRICT', 'AREA']].dropna() #selected Area and District columns from the pandasDataFrame and removed NAs

#Use the AREA column to find the longest and smallest districts - 1pt
q1 = df.sort_values("AREA", ascending=False) #sorted based on AREA column in a descending order
print("District # with the largest area:", q1["DISTRICT"].iloc[0])
print("Area of the largest district:", q1["AREA"].max())
print("District # with the smallest area:", q1["DISTRICT"].iloc[-1])
print("Area of the smallest district:", q1["AREA"].min())

#Create a choropleth map showing the area of each district - 2pt
cali1 = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(geo_data=df_gj,data=df3, columns=["DISTRICT","AREA"], key_on="feature.properties.DISTRICT", fill_color='YlGnBu', fill_opacity=0.5, line_color = "#0000", line_opacity=1).add_to(cali1) #"data=" has to be in pandasDataFrame, order in columns is important
cali1.save('q1_area_chor.html')

#Calculate the population density for each district using the POPULATION and AREA columns - 1pt
#population density = num of people / land area
df["popDensity"] = df["POPULATION"]/df["AREA"] #created a new column that displays population density
print(df["popDensity"]) #displaying the population density column

#Create a choropleth map displaying the population density of each district - 2pt
df4 = df.copy() #copied new geoDataFrame with added column into a separate variable
df5= pd.DataFrame(df4) #turn geopandasDataFrame to pandasDataFrame
df6 = df5[['DISTRICT', 'popDensity']].dropna() #selected popDensity and District columns from the pandasDataFrame and removed NAs
cali2 = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(geo_data=df_gj,data=df6, columns=["DISTRICT","popDensity"],key_on="feature.properties.DISTRICT", fill_color='RdYlGn', fill_opacity=0.5, line_color = "#0000", line_opacity=1).add_to(cali2)
cali2.save('q2_popDen_chor.html')

#Identify the district with the highest population density - 1pt
q2 = df.sort_values("popDensity", ascending=False) #sorted based on population density in a descending order
print("District # with the highest population density:", q2["DISTRICT"].iloc[0])
print("Population density of the district with the highest population density:", q2["popDensity"].max())
#Discuss how population density might impact resource allocation or urban planning within the state
#Regions with high population density impacts resource allocations by putting more pressure on the available resources such as water, energy, and food.
#As these resources have to be dispersed to everyone which limits the amount each person can receieve to avoid depletion of resources and equitability of distribution.
#This also puts pressure on urban planning within the state because high population density leads to overcrowding and deforestation, so the urban planners have to consider the find a way to satisfy the needs of everyone impartially while avoiding the destruction of our ecosystem and resources.

#Calculate the percentage of these three ethnicities in the state of California –1pt
def percentage(part, whole): #created function percentage
    return 100 * float(part)/float(whole) #returns percentage of part/whole
black = (df["DOJ_NH_BLK"].sum()) #total black, non-hispanic, population
asian = (df["DOJ_NH_ASN"].sum()) #total asian, non-hispanic, population
white = (df["NH_WHT_CVA"].sum()) #total white, non hispanic, population
totalPop = (df["CVAP_19"].sum()) #total poplulation of every district
print("Percentage of Black, non-hispanic, population in state of Cali with all districts combined:", percentage(black,totalPop), "%")
print("Percentage of Asian, non-hispanic, population in state of Cali with all districts combined:", percentage(asian,totalPop), "%")
print("Percentage of White, non-hispanic, population in state of Cali with all districts combined:", percentage(white,totalPop), "%")

# Visualize the geographic distribution of each of these population groups – 2pt //is this just a choropleth map as well? is it just visualizing the different race columns?
df7 = df2[['DISTRICT', 'DOJ_NH_BLK']].dropna() #selected Black ethnicty and District columns from the pandasDataFrame and removed NAs
cali3 = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(geo_data=df_gj,data=df7, columns=["DISTRICT","DOJ_NH_BLK"],key_on="feature.properties.DISTRICT", fill_color='RdYlBu', fill_opacity=0.5, line_color = "#0000", line_opacity=1).add_to(cali3)
cali3.save('q3_black_chor.html')

df8 = df2[['DISTRICT', 'DOJ_NH_ASN']].dropna() #selected Asian ethnicty and District columns from the pandasDataFrame and removed NAs
cali4 = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(geo_data=df_gj,data=df8, columns=["DISTRICT","DOJ_NH_ASN"],key_on="feature.properties.DISTRICT", fill_color='RdYlGn', fill_opacity=0.5, line_color = "#0000", line_opacity=1).add_to(cali4)
cali4.save('q3_asian_chor.html')

df9 = df2[['DISTRICT', 'NH_WHT_CVA']].dropna() #selected White ethnicty and District columns from the pandasDataFrame and removed NAs
cali5 = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(geo_data=df_gj,data=df9, columns=["DISTRICT","NH_WHT_CVA"],key_on="feature.properties.DISTRICT", fill_color='YlGnBu', fill_opacity=0.5, line_color = "#0000", line_opacity=1).add_to(cali5)
cali5.save('q3_white_chor.html')