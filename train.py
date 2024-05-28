import requests
def a(trainno):
    base_url="https://rappid.in/apis/train.php?train_no={}".format(trainno)
    response=requests.get(base_url)
    data=response.json()
    return data
if __name__=="__main__":
    train_no="22675"
    train_status=a(train_no)
    print("*****************************************************************")
    print("\t\t Train Name: ",train_status["train_name"])
    print("*****************************************************************")
    for x in train_status['data']:
        if x["is_current_station"]:
            print("station \t\t: ",x["station_name"])
            print("Distance from the starting \t: ",x["distance"])
            print("Timing \t\t\t\t: ",x["Timing"])
            print("Delay \t\t\t\t: ",x["Delay"])
            print("Platform No \t\t\t\t: ",x["Platform No"])
            print("Halt \t\t\t\t: ",x["Halt"])
        else:
            print(x['station_name'])
print("*****************************************************************")
print("\t\t Msg: ",train_status["message"])
print("\t\t Msg upd: ",train_status["updated_time"])
print("*****************************************************************")




