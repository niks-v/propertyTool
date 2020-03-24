# [url format, url min page, url max page, url extensions, parent class, price, address, date, rooms, bathrooms, cars, type]

from datetime import datetime

websites = [
    [ # realestate.com.au # robots.txt disallows data collecting :( should have checked that first
        "https://www.realestate.com.au/buy/list-{{number}}",
        1,
        3,
        "?activeSort=list-date",
        ('article', {"class":'residential-card'}), # parent 4
        ('span', {"class":"property-price"}), # price 5 
        ('a', {"class":"residential-card__details-link"}), # address 6
        str(datetime.now()), # date 7
        ('span', {"class":"general-features__beds"}), # beds 8
        ('span', {"class":"general-features__baths"}), # baths 9
        ('span', {"class":"general-features__cars"}), # cars 10
        ('span', {"class":"residential-card__property-type"}) # type 11
    ]
]
