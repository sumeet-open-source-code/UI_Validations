from selenium import webdriver


class ValidateYahooUI:
	'Validate user interface for Yahoo Web App'


	def getHomePageHeaderLinks(self):

		driver = webdriver.Chrome()
		# Yahoo URL and Page Tile will be imported from constatnts file
		driver.get("https://in.yahoo.com/?p=us")
		assert "Yahoo India | News, Finance, Cricket, Lifestyle and Entertainment" in driver.title
		header_links_list = driver.find_element_by_id("header-nav-bar")
		items = header_links_list.find_elements_by_tag_name("li")
		for item in items:
		    text = item.text
		    print(text)



obj = ValidateYahooUI()
obj.getHomePageHeaderLinks()
