# travel_list_goals ={
#     "Europe" : {"cities_visited":["United Kingdom","Spain,Greece, France"]},
#     "Africa" : {"planned_visits": ["Tanzania","Rwanda","Uganda","South Africa","Botswana"],"planned_visits":20}
    
    
# }
# print(travel_list_goals)


# #Nesting Dictionaries within a list

# travel_list_goals = [
#     {

#     "Continent":"Europe",
#     "cities_visited":["United Kingdom","Spain,Greece, France"],
#     "total_visits":12
    
#     },


#     {

#     "Continent" :"Africa",
#     "planned_visits": ["Tanzania","Rwanda","Uganda","South Africa","Botswana"],
#     "planned_visits":20

#     },
    
    
# ]

# def add_new_country(country_visited,times_visited,cities_visited):
#     new_country ={}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited

#     travel_log.append(new_country)






# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


dict ={
    "a":1,
    "b":2,
    "c":3
}

dict["c"]=[1,2,3]

print(dict[1])