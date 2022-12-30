# http://indianrailapi.com/api/v2/TrainSchedule/apikey/<apikey>/TrainNumber/<TrainNumber>/

import requests 
class IRCTC:
    def __init__(self):
        user_input=input('''How would you like to proceed
            1. Enter 1 to check live train status
            2. Enter 2 to check PNR
            3. Enter 3 to ckeck train Schedule
                
                ''')
        if user_input=='1':
            print('Live Station')
        elif user_input=='2':
            print('PNR')
        else:
            print('Train Schedule')
            self.train_schedule()
    def train_schedule(self):
        train_no=input('Enter the Train No.')
        self.fetch_data(train_no)
        
    def fetch_data(self,train_no):
        url=''
        data=requests.get(url) #url{}.formate(train_no)
        data=data.json
        print(data['Route'])
        for i in data['Route']:
            print(i['stationName'],'|',i['ArrivalTime'],'|',i['departureTime'],'|',i['Distance'],'kms')

obj=IRCTC()