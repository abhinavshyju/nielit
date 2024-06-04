import json
from selenium import webdriver
import time 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


profile_path = "C:/Users/abhin/AppData/Roaming/Mozilla/Firefox/Profiles/7l3ebdv8.default-release"

options = Options()


options.profile = profile_path

driver = webdriver.Firefox(options=options)



with open('./data.json', 'r') as f:
    data = json.load(f)


for item in data["courses"]:
    print(item["CourseName"] + " => starting")
    driver.get(f"https://cybershikshaa.azurefd.net/#/course/{item["ProductId"]}/item/0")
    time.sleep(3)


    # driver.get('https://cybershikshaa.azurefd.net/#/course/119/item/746') 
# driver.get('https://cybershikshaa.azurefd.net/#/course/116/item/750') 
# time.sleep(5)


    time.sleep(5)
    while True:
            try:
                print("Video playing and try to skip")
                videoId = driver.find_element(By.CLASS_NAME, 'vjs-tech').get_attribute('id')

                skip_script = f"""   var video = document.getElementById('{videoId}'); 
                var videoDuration = video.duration;
                video.currentTime = videoDuration - 3;"""
                

                script = f"""
                var video = document.getElementById('{videoId}'); 
                return video.duration;
                """
                video_duration = driver.execute_script(script)

                for i in range(5):
                    driver.execute_script(skip_script)
                
                script2= f"""
                var video = document.getElementById('{videoId}'); 
                return video.currentTime;
                """
                current_Time = driver.execute_script(script2)
                time.sleep(5)
                while (video_duration - current_Time ) > 20 :
                    print(video_duration - current_Time)
                    driver.execute_script(skip_script)
                    print("Skip.....")
                    time.sleep(2)
                    current_Time = driver.execute_script(script2)


                
                time.sleep(video_duration - current_Time + 5)
                no_next_video = driver.find_elements(By.CSS_SELECTOR, 'button[type="button"][name="Next"].is-disabled')
                
                if not no_next_video :
                    next_buttons_video = driver.find_elements(By.NAME, 'Next')
                    if next_buttons_video :
                        print("video over next button clicked")
                        next_buttons_video[0].click()
                        time.sleep(5)

                    else :
                        print("video over but no next button")
                        break
                else:
                    break

            except:
                no_next = driver.find_elements(By.CSS_SELECTOR, 'button[type="button"][name="Next"].is-disabled')
                if not no_next:
                    next_buttons = driver.find_elements(By.CSS_SELECTOR, '[name="Next"]')
                    if next_buttons:
                        print("Next button clicked")
                        next_buttons[0].click()
                        time.sleep(2) 
                    else:
                        print("No next button found")
                        try:
                            print("Video playing and try to skip")

                            videoId = driver.find_element(By.CLASS_NAME, 'vjs-tech').get_attribute('id')
                            print(videoId)

                            skip_script = f"""   var video = document.getElementById('{videoId}'); 
                            var videoDuration = video.duration;
                            video.currentTime = videoDuration - 10;"""

                            script = f"""
                            var video = document.getElementById('{videoId}'); 
                            var videoDuration = video.duration;
                            video.currentTime = videoDuration - 10;
                            video.play()  
                            return video.duration;
                            """
                            video_duration = driver.execute_script(script)

                            driver.execute_script(skip_script)
                            
                            script2= f"""
                            var video = document.getElementById('{videoId}'); 
                            return video.currentTime;
                            """
                            current_Time = driver.execute_script(script2)
                            
                            
                            time.sleep(video_duration - current_Time + 5)
                            next_buttons_video = driver.find_elements(By.NAME, 'Next')
                            if next_buttons_video :
                                print("video over next button clicked")
                                next_buttons_video[0].click()
                                time.sleep(2)
                            else :
                                print("video over but no next button")
                                break

                        except Exception as e:
                            print("Error in video playing", e)
                            break

                else:
                    
                    try : 
                        submit_button = driver.find_element(By.CSS_SELECTOR , 'button[type="button"].ms-Button.ms-Button--primary.start-test-link.root-145')
                        print("Submit button braking")
                        break
                    except:

                        try:
                            videoId = driver.find_element(By.CLASS_NAME, 'vjs-tech').get_attribute('id')
                            print(videoId)

                            skip_script = f"""   var video = document.getElementById('{videoId}'); 
                            var videoDuration = video.duration;
                            video.currentTime = videoDuration - 10;"""

                            driver.execute_script(skip_script)

                            script = f"""
                            var video = document.getElementById('{videoId}'); 
                            var videoDuration = video.duration;
                            video.currentTime = videoDuration - 3;
                            video.play()  
                            return video.duration;
                            """
                            video_duration = driver.execute_script(script)
                            
                            script2= f"""
                            var video = document.getElementById('{videoId}'); 
                            return video.currentTime;
                            """

                            current_Time = driver.execute_script(script2)

                            time.sleep(video_duration - current_Time + 5)

                            next_buttons_video = driver.find_elements(By.NAME, 'Next')
                            if next_buttons_video :
                                print("video over next button clicked 2")
                                next_buttons_video[0].click()
                                time.sleep(2)
                            else :
                                print("video over but no next button 2")
                                break

                        except Exception as e:
                            print("video error",e)
                            break
            
                print("error")
    print(item["CourseName"] + " => ending")
    time.sleep(3)
    


# print(10)
time.sleep(200)
driver.quit()
