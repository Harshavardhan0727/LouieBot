import requests
Api_key = "R96yn7QWa7ETYJKxmKPSSH5I6ku5aPmqiNT7axVg"


def NasaNews(Date):

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)

    params = {'date': str(Date)}

    r = requests.get(Url,params = params )
    Date = r.json()
    print(Data)

NasaNews('2022-1-1')