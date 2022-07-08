# Unique-Link-Finder
An expirimental python program that will search websites for links and indexes them by frequency.  This project was created to test out website comprehension in Python.

The program starts by searching the starting website for all links starting with https://, and stores links not yet found in a variable.  For example, entering in https://www.google.com will give you a result of many different google domains. Then, it will search through each of the links found for more links, and then it will search those links, etc. until all links found have been searched and there are no more unique links. The .txt file websites.txt will store sites sorted by frequency.




The variable in main.py called starting_website can change the website that is first searched.
