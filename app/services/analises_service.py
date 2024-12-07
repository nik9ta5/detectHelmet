import json


#Словарь, для хранения состояний всех подключенных клиентов
StateForClients = dict()


#Анализ результата, полученного от модели   
def analysDetectResult(results, client_uuid : str):
    json_f = results[0].to_json() #преобразует в json, все найденные объекты
    json_f = json.loads(json_f)
    
    # ИЗМЕНИТЬ ПОДСЧЕТ ПРИ ИЗМЕНЕНИИ МОДЕЛИ!!!
    # Подсчет кол-ва распознанных объектов
    prsn, head, hemls = 0, 0, 0
    for item in json_f:
        if item['name'] == 'person':
            prsn += 1
        if item['name'] == 'head':
            head += 1
        if item['name'] == 'helmet':
            hemls += 1

    print(prsn, head, hemls)
    #Если содержится - сравниваем
    if client_uuid in StateForClients:
        print('point1')
        # or StateForClients[client_uuid]['head'] != head or StateForClients[client_uuid]['helmet'] != hemls
        if StateForClients[client_uuid]['person'] != prsn:
            print('point2')
            #Обновляем состояние
            StateForClients[client_uuid]['person'] = prsn
            StateForClients[client_uuid]['head'] = head
            StateForClients[client_uuid]['helmet'] = hemls

            if prsn > 0: 
                print('point3')
                return (True, results[0].plot()) #Рассылаем уведомления
        print('point4')
        print(StateForClients)
        return (False, [])
    
    else:
        print('point5')
        print(client_uuid)
        #Сохраняем состояние
        StateForClients[client_uuid] = {}
        StateForClients[client_uuid]['person'] = prsn
        StateForClients[client_uuid]['head'] = head
        StateForClients[client_uuid]['helmet'] = hemls
        print(StateForClients)

    return (False, []) #Уведомления не рассылаем