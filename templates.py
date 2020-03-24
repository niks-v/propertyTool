# WEBSITE-COM = [url format, url min page, url max page, url extensions, parent class, price, address, date, rooms, bathrooms, cars, type]
# USE WEBSITE DOMAIN WITH . REPLACED WITH -

from datetime import datetime

websites = {
    "realestate-com-au" : [
        "https://www.realestate.com.au/buy/list-1",
        1,
        80,
        "?activeSort=list-date",
        ('article', {"class":'residential-card'}),
        ('span', {"class":"property-price"}),
        ('a', {"class":"residential-card__details-link"}),
        str(datetime.now()),
        ('span', {"class":"general-features__beds"}),
        ('span', {"class":"general-features__baths"}),
        ('span', {"class":"general-features__cars"}),
        ('span', {"class":"residential-card__property-type"})
        ]
}
