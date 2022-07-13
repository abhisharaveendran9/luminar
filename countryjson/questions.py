# print total number of country details

import json

with open("countries.json",encoding="utf") as f:
    data=json.load(f)

#print(len(data))

# india_detail=[country for country in data if country["name"]=="India"]
#print(india_detail)

# print languages of ukrane
#language_by_cntry=[country["languages"] for country in data if country["name"]=="Ukraine"]
#print(language_by_cntry)

# language_by_country=[country["languages"] for country in data if country["name"]=="India"]
# for lan in language_by_country[0]:
#    print(lan["name"])
#print(language_by_country)



# print currency of china
# currency_details=[country["currencies"] for country in data if country["name"].startswith("Palestine")]
# print(currency_details)

currency_detail=[country["currencies"] for country in data if country["name"].lower().startswith("sri")]
currency_name=[details.get("name") for details in currency_detail[0]]
# print(currency_name)


def get_country_data(country_name):
    return [country for country in data if country["name"].lower().startswith(country_name)]


aust_data=get_country_data("austria")
print(aust_data[0].get("borders"))


# print nigehbouring countries of australia
country_data=get_country_data("india")
country_borders=country_data[0].get("borders")
sharing_borders=[country.get("name") for country in data if country["alpha3Code"] in country_borders]
print(sharing_borders)



# print population of india
populated_country=max(data,key=lambda d:d.get("population"))
print(populated_country["name"])