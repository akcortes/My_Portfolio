
# Green Indicator for G8 Countries- Python (API Response Python and MySQL Data cleaning and transforming)

Jira: https://ironhack.atlassian.net/jira/software/projects/SPE/boards/14

Python Script: Added to the Folder

ER Model= ![image](https://user-images.githubusercontent.com/92767118/145793546-a59b93a7-7d9b-465d-bf80-e3a6e488e3cf.png)


Data Sources and Metadata:

OECD
https://www.oecd.org/environment/climate-data/

ClimateWatch Data
https://www.climatewatchdata.org/ghg-emissions?calculation=PER_CAPITA&end_year=2016&gases=ch4&regions=CAN%2CDEU%2CITA%2CJPN%2CRUS%2CGBR%2CUSA%2CFRA&start_year=2016![image](https://user-images.githubusercontent.com/92767118/145794478-4326cf02-a6ea-4d72-9ff9-0ce064306ff1.png)

UN
www.sdg6data.org/data-lab


Indicator:
<img width="930" alt="Screen Shot 2021-12-13 at 11 20 47" src="https://user-images.githubusercontent.com/92767118/145794757-4c723dc9-b7d6-4006-b453-8e50bf317d69.png">




# SQL SCRIPT


CREATE TEMPORARY TABLE Result_landFR
WITH max_min AS 
(
SELECT max(value) as MAX_VALUE,
min(value) AS MIN_VALUE
FROM labo.land_fr
)
SELECT 
Id,Country,TRUNCATE(value,2) AS VALUE, TRUNCATE((value-MIN_VALUE)/(MAX_VALUE-MIN_VALUE),2) AS Normalization, TRUNCATE((value-MIN_VALUE)/(MAX_VALUE-MIN_VALUE)*0.6,2) as Weight
FROM labo.land_fr, max_min 
WHERE land_FR.Code='L.FR';

SELECT * FROM Result_landFR;


CREATE TEMPORARY TABLE Result_landAG
WITH max_min AS 
(
SELECT max(value) as MAX_VALUE,
min(value) AS MIN_VALUE
FROM labo.land_AG
)
SELECT 
Id,Country,TRUNCATE(value,2) AS VALUE, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE)),2) AS Normalization, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE))*0.4,2) as Weight
FROM labo.land_AG, max_min 
WHERE land_AG.Code='L.AG';

CREATE TEMPORARY TABLE Land_Total
SELECT Result_landFR.Id,Result_landFR.Country,Result_landFR.Normalization,Result_landFR.Weight,Result_landAG.Normalization AS Normalization_AG,Result_landAG.Weight AS WeightAG,
Result_landAG.Weight+Result_landFR.Weight AS Total_Land
FROM Result_landAG
INNER JOIN Result_landFR
ON Result_landAG.Country=Result_landFR.Country;



#Emisiones
CREATE TEMPORARY TABLE Result_CH4
WITH max_min AS 
(
SELECT max(value) as MAX_VALUE,
min(value) AS MIN_VALUE
FROM labo.emissions
WHERE emissions.Code='EM.CH'
)
SELECT 
Id,Country,TRUNCATE(value,2) AS VALUE, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE)),2) AS Normalization_CH4, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE))*0.085,2) as Weight_CH4
FROM labo.emissions, max_min 
WHERE emissions.Code='EM.CH';


CREATE TEMPORARY TABLE Result_CO2
WITH max_min AS 
(
SELECT max(value) as MAX_VALUE,
min(value) AS MIN_VALUE
FROM labo.emissions
WHERE emissions.Code='EM.CO'
)
SELECT 
Id,Country,TRUNCATE(value,2) AS VALUE, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE)),2) AS Normalization_CO2, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE))*0.7,2) as Weight_CO2
FROM labo.emissions, max_min 
WHERE emissions.Code='EM.CO';


CREATE TEMPORARY TABLE Result_FG
WITH max_min AS 
(
SELECT max(value) as MAX_VALUE,
min(value) AS MIN_VALUE
FROM labo.emissions
WHERE emissions.Code='EM.FG'
)
SELECT 
Id,Country,TRUNCATE(value,2) AS VALUE, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE)),2) AS Normalization_FG, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE))*0.15,2) as Weight_FG
FROM labo.emissions, max_min 
WHERE emissions.Code='EM.FG';


CREATE TEMPORARY TABLE Result_NO
WITH max_min AS 
(
SELECT max(value) as MAX_VALUE,
min(value) AS MIN_VALUE
FROM labo.emissions
WHERE emissions.Code='EM.NO'
)
SELECT 
Id,Country,TRUNCATE(value,2) AS VALUE, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE)),2) AS Normalization_NO, TRUNCATE(ABS((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE))*0.065,2) as Weight_NO
FROM labo.emissions, max_min 
WHERE emissions.Code='EM.NO';



CREATE TEMPORARY TABLE Emissions_Total
SELECT Result_CO2.Country,Result_CH4.Weight_CH4,Result_CO2.Weight_CO2,Result_FG.Weight_FG,Result_NO.Weight_NO,(Result_CH4.Weight_CH4+Result_CO2.Weight_CO2+Result_FG.Weight_FG+Result_NO.Weight_NO) AS Total_Emissions
FROM Result_CO2
INNER JOIN Result_FG
ON Result_FG.Country=Result_CO2.Country
INNER JOIN Result_NO
ON Result_NO.Country=Result_FG.Country
INNER JOIN Result_CH4
ON Result_NO.Country=Result_CH4.Country;


CREATE TEMPORARY TABLE air_pol
WITH max_min AS 
(
SELECT max(value) as MAX_VALUE,
min(value) AS MIN_VALUE
FROM labo.air_pollution
)
SELECT 
Id,Country,TRUNCATE(value,2) AS VALUE, TRUNCATE(abs((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE)),2) AS Normalization_air, TRUNCATE(abs((value-MAX_VALUE)/(MAX_VALUE-MIN_VALUE)),2) as Weight_air
FROM labo.air_pollution, max_min;

#Indicator total
CREATE TEMPORARY TABLE Green_Indicator_G8
SELECT 
air_pol.Country,air_pol.Weight_air AS Total_Air,Emissions_Total.Total_Emissions,Land_Total.Total_Land,(air_pol.Weight_air*0.2 + Emissions_Total.Total_Emissions*0.7 + Land_Total.Total_Land*0.1) AS Green_Indicator_G8
FROM air_pol
INNER JOIN Emissions_Total
ON air_pol.Country=Emissions_Total.Country
INNER JOIN Land_Total
ON Land_Total.Country=air_pol.Country
ORDER BY Green_Indicator_G8 DESC;


SELECT * FROM air_pol;
SELECT * FROM Result_FG;
SELECT * FROM Result_CH4;
SELECT * FROM Result_CO2;
SELECT * FROM Land_Total;
SELECT * FROM Emissions;
SELECT * FROM Result_NO;
SELECT * FROM Emissions_Total;
SELECT * FROM Green_Indicator_G8;
