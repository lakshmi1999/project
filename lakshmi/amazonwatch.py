
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome(executable_path="/home/ubuntu/Downloads/chromedriver")
names=[]
reviews=[]
ratings=[]
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=3")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=4")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=5")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=6")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=7")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=8")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=9")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/product-reviews/B000GAYQJ0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=10")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for a in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
	name=a.find('span', attrs={'class':'a-profile-name'}).text
	review=a.find('span',attrs={'class':'a-size-base review-text review-text-content'}).text
	rating=a.find('a',href=True, attrs={'class':'a-link-normal'}).text
	names.append(name)
	reviews.append(review)
	ratings.append(rating)
driver.get("https://www.amazon.in/Casio-Vintage-Digital-Small-Watch-A158WA-1Q/dp/B000GAYQJ0/ref=cm_cr_arp_d_product_top?ie=UTF8")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
cost=soup.find('span',attrs={'class':'a-size-medium a-color-price priceBlockBuyingPriceString'}).text
cost=cost.replace("₹","")
cost=cost.replace(",","")

df = pd.DataFrame({'Name':names,'Ratings':ratings,'Review':reviews,'Cost(₹)':float(cost)})
df.to_csv("amazonwatch.csv", index=False, encoding='utf-8')
reviews_df = pd.read_csv("amazonwatch.csv")
reviews_df["Names"] = reviews_df["Name"]
reviews_df["rate"] = reviews_df["Ratings"].apply(lambda x: x.replace("out of 5 stars", ""))
reviews_df["Good/Bad"] = reviews_df["rate"].apply(lambda x: 0 if x < '3' else 1)
reviews_df = reviews_df[["Names","Review", "Good/Bad"]]
print(reviews_df)
print(reviews_df["Good/Bad"].value_counts(normalize = True))
reviews_df.head()

