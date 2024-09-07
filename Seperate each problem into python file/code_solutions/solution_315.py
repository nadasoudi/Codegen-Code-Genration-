import time

def get_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Error: {}".format(response.status_code))
    except Exception as e:
        print(e)
        raise Exception("Error: {}".format(e