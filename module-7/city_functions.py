def city_country(city, country, language=None, population=None):
    if population: 
        if language:
            formatted_city_country = f"{city}, {country} - population {population}, {language}"
        else:
            formatted_city_country = f"{city}, {country} - population {population}"
    else:
        if language:
            formatted_city_country = f"{city}, {country}, {language}"
        else:
            formatted_city_country = f"{city}, {country}"
    return formatted_city_country.title()

print(city_country("Toronto", "Canada"))
print(city_country("Omaha", "United States", 486000))
print(city_country("Dublin", "Ireland", 570000, "Irish"))
print(city_country("Husavik", "Iceland", "Icelandic"))


