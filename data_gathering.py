from dotenv import load_dotenv
import os
import requests
import time
from PIL import Image
import urllib.request 
from requests.auth import HTTPBasicAuth
from io import BytesIO

def get_data():
    # method = "GET"
    # url = "https://api.mobygames.com/v1/games/55403/platforms/5/screenshots"
    # url = "https://api.mobygames.com/v1/games/random"
    # response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    # print(response.json())
    # game_ids = response.json()["games"]
    # for game_id in game_ids:
    #     url = "https://api.mobygames.com/v1/games/" + str(game_id) + "/platforms"
    #     try:
    #         response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    #         print(response.json()["platforms"])
    #         time.sleep(1)
    #     except:
    #         print("No platforms for game id: " + str(game_id))

    # windows_platform = 3
    
    # for game_id in game_ids:
    #     try:
    #         url = "https://api.mobygames.com/v1/games/" + str(game_id) + "/platforms"
    #         response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    #         platforms = response.json()["platforms"]
    #         if windows_platform in [platform["platform_id"] for platform in platforms]:
    #             try:
    #                 url = "https://api.mobygames.com/v1/games/" + str(game_id) + "/platforms/5/screenshots"
    #                 print(url)
    #                 response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    #                 #print(response.json())
    #                 #Try to collect 100 total screenshots:
    #                 for i in range(100):
    #                     image = response.json()["screenshots"][i]["image"]
    #                     #Save image to file:
    #                     print(image.type)

    #                 time.sleep(1)
    #             except:
    #                 print("No screenshots for game id: " + str(game_id))
    #         else:
    #             print("Game is not on Windows platform") 
    #     except:
    #         print("No platforms for game id: " + str(game_id))
    
    # method = "GET"
    # url = "https://api.mobygames.com/v1/platforms"
    # response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    # for platform in response.json()["platforms"]:
    #     print(platform["platform_id"], platform["platform_name"])

    #Windows platform id is 3, Playstation is 6, Playstation 2 is 7, Playstation 3 is 81, Playstation 4 is 141, Playstation 5 is 288 
    #Get all screenshots for a specific game:
    method = "GET"

    #Red Dead Redemption 2 for PS4
    '''
    game_id = 115902
    url = "https://api.mobygames.com/v1/games/" + str(game_id) + "/platforms/141/screenshots"
    response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    #Transform image to PIL image:
    for screenshot_index in range(len(response.json()["screenshots"])):
        image_url = response.json()["screenshots"][screenshot_index]["image"]
        img_response = requests.get(image_url)
        image = Image.open(BytesIO(img_response.content))
        image.save(os.path.join("gathered_images", "red_dead_redemption_2_ps4_" + str(screenshot_index) + ".jpg"))
    '''
    
    #Elden Ring for Windows
    '''
    game_id = 174989
    url = "https://api.mobygames.com/v1/games/" + str(game_id) + "/platforms/3/screenshots"
    response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    #Transform image to PIL image:
    print(response.json())
    for screenshot_index in range(len(response.json()["screenshots"])):
        image_url = response.json()["screenshots"][screenshot_index]["image"]
        img_response = requests.get(image_url)
        image = Image.open(BytesIO(img_response.content))
        image.save(os.path.join("gathered_images", "elden_ring_ps5_" + str(screenshot_index) + ".jpg"))
    '''

    #God of War for PS4
    '''
    game_id = 107419
    url = "https://api.mobygames.com/v1/games/" + str(game_id) + "/platforms/141/screenshots"
    response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    #Transform image to PIL image:
    for screenshot_index in range(len(response.json()["screenshots"])):
        image_url = response.json()["screenshots"][screenshot_index]["image"]
        img_response = requests.get(image_url)
        image = Image.open(BytesIO(img_response.content))
        image.save(os.path.join("gathered_images", "god_of_war_ps4_" + str(screenshot_index) + ".jpg"))
    '''
    #The last of us for PS4
    
    game_id = 146798
    url = "https://api.mobygames.com/v1/games/" + str(game_id) + "/platforms/141/screenshots"
    response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    #Transform image to PIL image:
    for screenshot_index in range(len(response.json()["screenshots"])):
        image_url = response.json()["screenshots"][screenshot_index]["image"]
        img_response = requests.get(image_url)
        image = Image.open(BytesIO(img_response.content))
        image.save(os.path.join("gathered_images", "the_last_of_us_ps4_" + str(screenshot_index) + ".jpg"))
    
        
    #Resident Evil 4 for PS5:
    '''
    game_id = 200900
    url = "https://api.mobygames.com/v1/games/" + str(game_id) + "/platforms/288/screenshots"
    response = requests.request(method, url, auth=HTTPBasicAuth(api_key, ""))
    #Transform image to PIL image:
    for screenshot_index in range(len(response.json()["screenshots"])):
        image_url = response.json()["screenshots"][screenshot_index]["image"]
        img_response = requests.get(image_url)
        image = Image.open(BytesIO(img_response.content))
        image.save(os.path.join("gathered_images", "resident_evil_4_ps5_" + str(screenshot_index) + ".jpg"))
    '''

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_KEY")
    print(api_key)
    get_data()