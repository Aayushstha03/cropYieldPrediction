# factors that explain/affect crop growth

### Paddy
Precipitation
winter temperature (winter higher temps can prolong reproductive period)
drought or not

### Maize

### Millet

### Wheat

### Barley

# Handling missing districts 
Here are approximate neighboring districts for the missing ones based on geography:

    Bhojpur:
        Nearby districts: Dhankuta, Khotang, Sankhuwasabha, Solukhumbu
        Climatic Zone: Hill

    Jajarkot:
        Nearby districts: Dailekh, Rukum (West), Dolpa, Kalikot
        Climatic Zone: Mountain/Hill

    Kalikot:
        Nearby districts: Jumla, Mugu, Dailekh, Jajarkot
        Climatic Zone: Mountain

    Ramechhap:
        Nearby districts: Dolakha, Sindhuli, Okhaldhunga, Kavrepalanchok
        Climatic Zone: Hill

    Achham:
        Nearby districts: Bajura, Doti, Dailekh, Kalikot
        Climatic Zone: Mountain/Hill

    Rolpa:
        Nearby districts: Rukum (West), Rukum (East), Pyuthan, Dang
        Climatic Zone: Hill

    Sindhupalchok:
        Nearby districts: Rasuwa, Kavrepalanchok, Dolakha, Nuwakot
        Climatic Zone: Hill/Mountain

    Pyuthan:
        Nearby districts: Rolpa, Gulmi, Arghakhanchi, Dang
        Climatic Zone: Hill

    Parsa:
        Nearby districts: Bara, Rautahat, Chitwan, Makwanpur
        Climatic Zone: Terai

    Kapilbastu:
        Nearby districts: Rupandehi, Arghakhanchi, Dang
        Climatic Zone: Terai

    Siraha:
        Nearby districts: Saptari, Udayapur, Dhanusha
        Climatic Zone: Terai

    Bajura:
        Nearby districts: Bajhang, Achham, Kalikot, Humla
        Climatic Zone: Mountain

    Khotang:
        Nearby districts: Udayapur, Okhaldhunga, Bhojpur, Solukhumbu
        Climatic Zone: Hill


# DataSet outline
## 2925 unique weather data entries
75 districts * 39 years(1981 to 2019)

## 15750 rows
3150 per district per crop after divinding by 5 
75 districts * 42 years (1979 to 2021)

we can use data till 2019 until i add the data for weather from 2019 to 2021



# Support vector regression SVR 
used c = 10 and epsilon = 0.5 after using grid search to find the combination that gives the best result

for barley SVR
for Maize RandomForest
for Millet RandomForest
for Paddy RandomForest
for Wheat RandomForest

so lets go with RandomForest for the model!