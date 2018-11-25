from reddit import Reddit
class Main:
	def __init__(self):
		pass

	def get_credentials(self):
		import json

		f = open('credentials.json', 'r')
		data = json.load(f)
		f.close()

		client_id = data["client_id"]
		client_secret = data["client_secret"]
		user_agent = data["user_agent"]
		username = data["username"]
		password = data["password"]

		return (client_id, client_secret, user_agent, username, password)
	
	def get_exclude_list(self):
		f = open('exclude.txt', 'r')
		exclude_list = []

		for line in f:
			exclude_list.append(line.strip())
		
		f.close()
		return exclude_list
	
	def exclude(self, list1, exclude_list):
		list2 = []
		for item in list1:
			if item not in exclude_list:
				list2.append(item)
		return list2

	def print_subs_list(self,subs_list):
		for item in subs_list:
			print(item)
	
	def generate_file(self,subs_list):
		f = open('trends.txt', 'w')
		for item in subs_list:
			f.write(item.display_name)
			f.write("\n")
		f.close()

if __name__ == "__main__":
	main = Main()
	credentials = main.get_credentials()
	reddit_instance = Reddit(credentials)
	subs_list = reddit_instance.get_popular_subs(limit=1000)
	exclude_list = main.get_exclude_list()
	subs_list = main.exclude(subs_list, exclude_list)
	main.generate_file(subs_list)