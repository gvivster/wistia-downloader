
import os
import time
import sys

video_index = 1
def logo():
	sprint("""\033[1;33;40m
		 _  _  _ _           _          _____                    
		| || || (_)     _   (_)        (____ \                   
		| || || |_  ___| |_  _  ____    _   \ \ ___  _ _ _ ____  
		| ||_|| | |/___)  _)| |/ _  |  | |   | / _ \| | | |  _ \ 
		| |___| | |___ | |__| ( ( | |  | |__/ / |_| | | | | | | |
		 \______|_(___/ \___)_|\_||_|  |_____/ \___/ \____|_| |_|
	\033[0;37;40m""", 0.1)


def sprint(string, tm=10):
    for c in string + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(tm / 100)


def html_page_handle_and_download(file_name):
	print("\033[1;32;40m")
	global video_index
	with open(file_name, "r") as file:
		i = 1
		for con in file:
			# ERROR
			if i== 1 and con == '{"error":true,"iframe":true}':
				video_url = con
			if i == 63:
				video_url = con
				break
			i+=1
		if video_url == '{"error":true,"iframe":true}':
			sprint("\033[1;31;40mYour video id is not valid\033[0;37;40m", 2)
		else:
			new_video_url = video_url.split("url")[1].split(',')[0].split('"')[2]
			os.system("curl -O {}".format(new_video_url))
			video_name = video_url.split("url")[1].split(',')[0].split('"')[2].split("/")[4]
			video_name_and_index = "Video " + str(video_index) + ".mp4"
			video_index += 1
			os.rename(video_name, video_name_and_index)
		os.system("rm -rf {}".format(file_name))
	print("\033[0;37;40m")


def download_folder():
	try:
		username = os.path.expanduser("~").split('/')[2]
		sprint("\033[1;32;40mPlease enter the PATH of download folder: \033[0;37;40m", 2)
		sprint("\033[1;31;40m\t\tExample: \033[0;37;40m/Users/{}/Desktop".format(username), 2)
		sprint("\033[1;31;40m\t\tExample: \033[0;37;40m/Volumes/Storage/goinfre/{}".format(username), 2)

		folder_path = input("PATH: \033[1;33;40m")
		print("\033[0;37;40m")
		folder_path += "/wistia-downloader/"
		os.system("mkdir {} 2>/dev/null".format(folder_path))
		os.system("cp video_ID.txt {} 2>/dev/null".format(folder_path))
		os.chdir("{}".format(folder_path))
		sprint("\033[1;33;40mOpening the download folder...\033[0;37;40m", 2)
		os.system("open {}".format(folder_path))
	except FileNotFoundError:
		print("\033[1;31;40mThe PATH does not exist !! try again\033[0;37;40m")
		sprint(".....", 100)
		main()


def main():
	os.system("clear")
	logo()
	download_folder()
	url = "http://fast.wistia.net/embed/iframe/"
	i = 0
	with open("video_ID.txt", "r+") as video_id:
		if os.stat("video_ID.txt").st_size == 0:
			print("")
			sprint("\033[1;31;40mThe file video_ID.txt is empty !!\033[0;37;40m", 0.2)
			sprint(".....", 100)
			main()
		for id in video_id:
			os.system("curl -O {}".format(url + id))
			print("Video ID " + str(i + 1) + "--------------------------------------------------------------------------")
			html_page_handle_and_download(id.rstrip())
			print("-----------------------------------------------------------------------------------")
			i+=1 

	

if __name__ == '__main__':
	main()