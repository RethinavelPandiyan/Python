import instaloader
import socket
import sys
import os
#Print all user data by the profile
def profile_details(profile):
	print("Username:",profile.username)
	print("Name:",profile.full_name)
	print("Bio🧾:",profile.biography)
	print(f"Followers 👭: {profile.followers:,}")
	print(f"Following 🧑‍🤝‍🧑: {profile.followees:,}")
	print(f"Posts 📸: {profile.mediacount:,}")
	print("Account visiblity:","Private🔒" if profile.is_private else "Public🔓")
	print("Account status:","Verified ✅" if profile.is_verified else "Not verified ❌")
	print("Account type:","Business account" if profile.is_business_account else "Personal account")
	print("Account ID:",profile.userid)
	print("IGTV 📺  count:",profile.igtvcount)
	print("Blocked viewer:","Yes" if profile.has_blocked_viewer else "No")
	print("Highlight reels:","Yes" if profile.has_highlight_reels else "No")
	print(f"External URL: \033[94m{profile.external_url}\033[0m")
	print("Viewer followed:","Yes" if profile.followed_by_viewer else "No")
#-----Check the internet before access the instagram-----#
def check_internet():
	try:
		socket.gethostbyname("instagram.com")
		return True
	except socket.gaierror:
		print("Internet not available 📡.")
		sys.exit()
def main():
	#Load Instaloader & get Username
	L=instaloader.Instaloader()
	username=input("Target Username:").strip()
	try:
		#Load the profile data from username
		profile=instaloader.Profile.from_username(L.context,username)
	except instaloader.exceptions.ProfileNotExistsException:
		os.system("cls" if os.name=="nt" else "clear")
		print(f"{username} does't exists.")
		sys.exit()
	except instaloader.exceptions.ConnectionException as e:
		if "401" in str(e):
			os.system("cls" if os.name=="nt" else "clear")
			print(f"🔐 Authentication failed or Username '{username}' does't exists.")
			sys.exit()
		else:
			os.system("cls" if os.name=="nt" else "clear")
			print("🌐 Connection error.")
	except Exception as e:
		print(e)
	profile_details(profile)
if __name__=="__main__":
	check_internet()
	main()
