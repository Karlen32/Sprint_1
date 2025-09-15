types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_duplicates(dict):
    for key in dict:
        new_list = []
        for item in dict[key]:
            if item not in new_list:
                new_list.append(item)
        dict[key] = new_list

def new_tickets(types, tickets):
    delete_duplicates(tickets)
    all = []           
    result = {}
    for key in types:   
        uniq = []
        for item in tickets.get(key, []):
            if item not in all:   
                uniq.append(item)
                all.append(item)  
        result[types[key]] = uniq
    return result

tickets_type = new_tickets(types, tickets)
print(tickets_type)

