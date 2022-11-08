# TrentonEats Project 
Trenton Eats Local: User’s Guide

Introduction to the System
Trenton Eats, a web application created in partnership with the Trenton Eats Local Club, was made in response to the decline of the restaurant industry during the COVID-19 pandemic, particularly in response to the difficulties faced by local restaurants in Trenton. The web app allows users to view a list of local restaurants in Trenton, displaying details such as opening hours, directions, location, etc. while also facilitating rating and reviewing for each restaurant (among other features).. Local restaurant owners can also fill out a form to add their restaurant to the website, providing them an opportunity to advertise their restaurants to consumers. Unlike other “Find a Restaurant” websites, Trenton Eats is specific to Trenton, catering to local restaurants in terms of helping them promote their business  as well as consumers looking to eat and support businesses in Trenton.

Use Cases
PRELIMINARY NOTES: 
Some functionalities described below (specifically use cases under “Part 2: Logged In” within the section titled “A Trenton Restaurant-Goer” as well as all use cases in the sections  “A Restaurant Owner” and “An Administrator”) require logging in, which is done on the web-app by redirecting through Google authentication. We assume that users have a Google account or are willing to create one in order to access the web app.

 Additionally, certain use cases require special access in order to complete, which will be specified in the pertinent sections below (see “A Restaurant Owner” and “An Administrator”). We will provide graders in COS 333 with special access such that they can complete all use cases listed below, but general users would have to follow the directions described in the sections below to be able to complete certain functionalities (i.e. those described in  “A Restaurant Owner” and “An Administrator”).

Moving on to the use cases themselves, the first use case is simply accessing the system, described below:
Accessing the system
Type into your browser the following URL link: https://trentoneats.herokuapp.com/

The remaining use cases are organized into those that would be performed by three different users: (1) a “Trenton Restaurant-Goer” (someone who looking to get a meal at a local restaurant in Trenton);  (2) a “Restaurant Owner” (someone who owns a restaurant in Trenton); and (3) an “Administrator” (someone who is responsible for managing the web application). 

A Trenton Restaurant-Goer 
This section describes use cases for someone looking to find a meal at a local restaurant in Trenton. The first part (Part 1) below starts with functions that can be performed on the web application without logging in.
Part 1: A Trenton Restaurant-Goer Who is Not Logged In
Viewing Restaurant List on Home Page
After navigating to the website at the above URL link, you should be able to see the home page of the site which lists all restaurants currently added to the application (depending on the screen size of your device, you may have to scroll down a little to fully view the list). For each restaurant, notice that the corresponding list entry displays the restaurant name at the top, as well  the address of the restaurant. Additionally, the list entry for each restaurant  also displays the  number of reviews for the restaurant as well as relevant information regarding whether the restaurant is open or closed, the cuisine type of the restaurant, the price range (inexpensive, moderate, or pricey), as well as the type of restaurant (fast food, casual, or fine dining) in colorful “tags” at the bottom of the list entry. Finally, each list entry for a restaurant also displays the rating (out of 5.0) using colored stars..

NOTE: In terms of the price ranges displayed in the tags, restaurants are categorized as inexpensive, moderate, or pricey based on the following thresholds:
Inexpensive: Average cost of a meal at this restaurant is below $10.
Moderate: Average cost of a meal is between $10-$30.
Pricey: Average cost of a meal is $3	1 or above. 
	
These thresholds are the same as those used by other popular “Find a Restaurant” websites, such as Yelp.com. 

Sort Restaurants By Rating
Click on the blue button labeled “Sort Restaurants By:” under “Restaurant Search Results”. In the drop-down list that is displayed after clicking the button, click on the option to “Show Best Rated Restaurants First”. Notice that the list of restaurants on the home page is now sorted by rating, with those restaurants that are more highly rated appearing first and those that have a lower rating appearing lower down the list. You can confirm this by viewing the colored stars in each restaurant entry and noticing how the rating decreases down the list.

Sort Restaurants By Price (Low to High)
Now, go back  to the “Sort Restaurants By:” button and click it again. Select the option in the drop-down list titled “Price (Low to High)”. Now, notice that the restaurants in the list are sorting in ascending price order, with restaurants categorized as inexpensive placed towards the top, followed by moderately priced restaurants, and finally by pricey restaurants. You can confirm this by viewing the green-colored tags at the bottom of each restaurant list entry, which read either “Inexpensive $”, “Moderate $$”, or “Pricey $$$” (colored different shades of green to more easily signal to viewers the price range of the restaurant). See the use case titled “Viewing Restaurant List on Home Page”  for the price thresholds used to categorize restaurants as inexpensive, moderate, or pricey. 

Sort Restaurants By Price (High to Low)
Go back to the “Sort Restaurants By:” button and select the option from the corresponding drop-down titled “Price (High to Low)”. This is similar to the use case described previously, except this functionality was added in case users want to view restaurants with more expensive restaurants placed first in the list. After selecting the “Price (High to Low)” option, you should see that the restaurants in the list will be sorted from “Pricey $$$” to “Moderate $$” to “Inexpensive $”  (with pricey restaurants at the top). Again, you can confirm this by checking the green-colored  tags at the bottom of the list entry for each restaurant.

Searching for a Restaurant
Go to the search bar located at the top of the webpage, just under the header “Explore food, Trenton Style” (the search bar should say “Enter a restaurant name here!”). Type  ‘J’ into the search bar, and you will see the restaurant results  automatically update to show 2 restaurants that have a ‘J’ in their title: “Bamboo Grill Jamaican Restaurant”  and “Don Julio’s Bar and Grill”. Note that you can still use the “Sort Restaurants By:” button at this point, even after inputting text into the search bar; for example, try clicking on the button and selecting the “Show Best Rated Restaurants First” option. Between “Bamboo Grill Jamaican Restaurant”  and “Don Julio’s Bar and Grill”,  the restaurant with the better rating will now be displayed at the top of the list, with the other restaurant placed beneath it.

Now type in ‘u’ into the search bar so that it says ‘Ju’. The result page should once again update to only show “Don Julio’s Bar and Grill”, as this is the only restaurant currently on the web app that has the letters “Ju” consecutively in the title (i.e. in “Julio’s”). 

The search bar works by taking the letters/words you input and matching those letters/words to the restaurant titles such that any restaurant with the corresponding letter or word in its title would automatically be displayed under “Restaurant Search Results”. Therefore, you can use the search bar to search for any restaurant by its title.

Redirecting to the Home Page
Direct your mouse to the blue navigation bar at the top of the webpage and click on “Home” (located in the top left corner). If you are on a mobile device, you may have to click on the three lines displayed in the navigation bar to access the list of pages and then click on “Home” from there. This will refresh the page, clearing any text you entered in the search bar and bringing you back to the homepage of the website (the one you saw when first accessing the system through the url https://trentoneats.herokuapp.com/). As such, you should also see the full list of restaurants under “Restaurant Search Results” rather than only seeing the ones you may have previously searched for.

Using Advanced Search
After having redirected to the homepage after clicking “Home” in the navigation bar, click on the red text labeled “Try Advanced Search Features”, located just under the text “Don’t have a specific restaurant in mind?” and above “Restaurant Search Results”. After clicking this text you should see the arrow to the left of the text “Try Advanced Search Features” shift to a downwards position (pointing down) and an array of advanced search options revealed below the text. 

Let’s try using the advanced search feature to search for restaurants that have Soul food, are at a moderate price range, and feature a casual dining experience. In the advanced search options, start by choosing “Soul” in the “Select a Cuisine” list. You can select “Soul” by simply clicking on it. Under “Select Price Range(s)”, select the checkbox corresponding to “$$” (the checkbox is located just to the left of the “$$”), which indicates moderate price. Under “Select Dining Type”, choose the radio button near “Casual”. Finally, click on the blue  submit button. After clicking submit, you should see two restaurants under “Restaurant Search Results”: “Ila Mae’s Restaurant” and “The Big Easy of Trenton Restaurant”. As indicated by the colorful tags at the bottom of the list entry, both of these restaurants sell Soul food, are at a moderate price range, and feature casual dining.

As illustrated by the example above,  the advanced search options can be used to search for restaurants using any combination of cuisine type, price range, and/or dining type.

View Restaurant Details
Go back to the home page by clicking on “Home” in the navigation bar. In the list of restaurants under “Restaurant Search Results”, scroll down until you find the restaurant titled “Blue Danube Restaurant”. Click the list entry (to do this, click anywhere within the pink colored box; if you are using a mouse, the box should turn blue when you hover the mouse over it before you click).. By clicking the list entry for any restaurant (in this case Blue Danube Restaurant), you will be directed to a new page that displays pertinent information regarding that restaurant. 
On this new page (which we will call the “Restaurant Details Page” from here on), which in this case is specific to Blue Danube, notice that a picture of the restaurant (taken from Google) is displayed. Additionally, the details page indicates whether the restaurant is currently closed or open, the hours of operation, the address (accompanied with a map of the location on larger screen sizes), the cuisine(s), price range, and type (fast food, casual, or fine dining) are all shown towards the top of the screen. Scrolling down a little, under the section titled “More Details”, you can also see the review count (indicating number of reviews left for this restaurant), the rating (given by colored stars). The buttons labeled “Menu” and “Website’ will be addressed in subsequent use cases. Finally, at the very bottom of the Restaurant Details page, you will see the reviews (in the form of comments)  that any users have left (if there are no reviews for a given restaurant, this will not be displayed). 

Get Directions to a Restaurant
On the restaurant details page for Blue Danube Restaurant, click on the white button labeled “Get Directions” located towards the middle of the page near the address of the restaurant. Clicking this button will open a new tab which leads to Google Maps, allowing you to input any starting location to get directions to Blue Danube Restaurant (the address of which will be pre-filled for you in the destination within the Google Maps tab). 

Accessing a Restaurant Menu
Go back to the Restaurant Details page for Blue Danube Restaurant (if you previously completed the “Get Directions to a Restaurant” use case, the Restaurant Details page for Blue Danube Restaurant should still be open in its own tab). Now, scroll down towards the bottom of the page and locate the white “Menu” button and click it. This should once again open up a new tab, this time leading to the menu for Blue Danube Restaurant. 

Note that if another restaurant did not have an online menu, the white “Menu” button would not be present on its corresponding Restaurant Details page.

Accessing a Restaurant Website
Go back to the Restaurant Details page for Blue Danube Restaurant. Scroll down once more and click the white “Website” button. This will open up a new tab, this time displaying the main website for Blue Danube Restaurant.

Note that if another restaurant did not have an online menu, the white “Website” button would not be present on its corresponding Restaurant Details page.

Viewing the About Page
Go back to the Restaurant Details page for Blue Danube Restaurant. Go to the top of the page to the navigation bar and click on “About”. This will redirect you to the about page, which includes information about “Who We Are” (including information about the Trenton Eats Local team/club, as well as the developers), “How to Use this Website” (information about using the web app), as well as how to “Contact Us” (featuring an email account administers will check to answer questions and manage the website).

Surprise Me!
Use the navigation bar to click on “Home”, going back to the home page. Located just under the search bar, find the blue text that says “Surprise Me!”. Click it. This will take you to the Restaurant Details page of a random restaurant, allowing users to be “surprised” by a restaurant that the website chooses for them if they so wish.

This concludes all use cases that can be completed without logging in. The next part (Part 2) describes use cases for Trenton Restaurant-Goers who are logged in (this section also describes how to log in).
Part 2: Logged in
Logging in
In order to log in, go to the navigation bar and click on “Login”. This will redirect you to the Google sign-in page, where you will be able to sign in to your Google account. After signing in, you will be redirected to the home page of the web application. Notice that the navigation bar now displays “Logout” instead of “Login”. 

Adding a Restaurant as a Favorite
In the restaurant list under “Restaurant Search Results”, locate the restaurant titled “Sabor Latino”. Click it to go to the corresponding Restaurant Details page. Now that you have logged in, you should be able to see a light blue button labeled “Add this restaurant as a favorite!” towards the middle of the page. Click this button (once you have clicked it, the page should reload and the button should read “Remove as favorite”). Now, navigate to the “My Favorites” page by clicking “My Favorites” in the navigation bar. See that “Sabor Latino” is listed as a favorite restaurant under the title “My Favorites”.

Removing a Restaurant as a Favorite
Go back to the Restaurant Details page for Sabor Latino by clicking on the list entry for Sabor Latino  in the “My Favorites” page. Locate the light blue button towards the middle of the page labeled “Remove as favorite” (this is the button that used to read “Add this restaurant as a favorite!”, but is now “Remove as favorite”  as Sabor Latino was previously added as a favorite). Click this button. Notice that the page reloads and the button once again reads “Add this restaurant as a favorite!”. Navigate to the “My Favorites” page again using the navigation bar. Notice that Sabor Latino is no longer listed as a favorite restaurant.

Writing a Review for a Restaurant
Go back to the home page using the navigation bar. Locate Sabor Latino once more in the restaurant list, and click the list entry to go to the Restaurant Details page for Sabor Latino. Scroll down if necessary to locate the section titled “Write a Review for this Restaurant!”, a section of the page that is only visible to users who are logged in. Give Sabor Latino a great review by (1) sliding your mouse across the stars under “Give a rating:” such that all of the stars are completely blue (a 5.0/5.0 rating) and (2) writing “This restaurant is really great!” in the space to type your review (under “Your review”). Click on the blue submit button. Notice that your written review is now displayed in the review carousel at the bottom of the page, and that the review count and stars under “More Details” are updated to reflect your rating.

All of the use cases above are those that pertain to a Trenton Restaurant-Goer looking to use the web application to find a restaurant in Trenton to dine at. The use case in the next section is relevant to a Trenton restaurant owner. 

A Restaurant Owner
Adding a Restaurant
To add a restaurant to the web application as a restaurant owner, an make sure you are logged in and click “I Am a Restaurant” in the navigation bar. This will take you to a form that will allow you to request to add a restaurant to the website. To understand  how one might fill out the form, start by entering “A new restaurant” in the “Name” field (which says “Restaurant Name in the input box). Next, in the address field, type “11”; a list of nearby  addresses containing 11 should appear as a drop down below the bar you are typing in — click on the first  of those addresses, and notice that the address input box automatically populates with that address. Next, input the following times as the hours of operation for the restaurant: on Monday, uncheck the “Open?” checkbox to indicate that the restaurant is closed. Do the same for Tuesday and Wednesday. For Thursday, keep the “Open?” checkbox checked and indicate that the restaurant will be open from 11:00 AM to 3:00PM by clicking into the boxes displaying the times and choosing from the drop down list the times that the restaurant is open from and until. Input the same hours for Friday, Saturday, and Sunday as you did for Thursday. Next, copy and paste the following link for the restaurant menu: www.chick-fil-a.com/menu (note that the https beginning for the url is already added in the form), and the following link for the restaurant website: www.chick-fil-a.com. As for the restaurant type, click the radio button near “Fast Food”, and for Cuisine(s) check “American”.  Then, use the slider to indicate that the average price of a meal at your new restaurant is $20. Finally, upload an image for your restaurant by clicking the blue “Upload Files” button on the form, navigating to the “Camera” option at the top of the pop-up, and capturing an image of yourself or your surroundings (be sure to click the red upload button and the subsequent “Done” button  after capturing the image to upload it). 

Hit submit to submit the form. Note that this submit button itself does not add the new restaurant to the web application — the restaurant must be approved by an administrator to actually add it to the website. 

An additional note about the process of adding a restaurant is that any user (including Trenton Restaurant-Goers) is able to access the “I Am a Restaurant” form and fill out the form to request adding a new restaurant to the website. The administrator, however, only approves the restaurants that are requested to be added by restaurant owners —  restaurant owners must therefore send an email to trentoneats@gmail.com with the title of their restaurant and proof of restaurant ownership in order to have their restaurant approved and added to the web application.

The next use case describes the approval process that an administrator carries out.
Approving A Request to Add  a Restaurant to the Web Application
In order to approve a restaurant to be on the website once a restaurant owner fills out the form (and has emailed with proof of restaurant ownership), administrators can go to the “Restaurant Approval” page by clicking on “Requests” using the navigation bar. Here, you can see a list of restaurants that have submitted the form using “I Am a Restaurant” that await approval. Using the search bar at the top of the page, search for “A new Restaurant”, and see that the corresponding restaurant is below the search bar. Click on the restaurant (“A new restaurant”), and observe how this takes you to a new page. This new page is very similar to a Restaurant Details page, with very similar information, but now has a section in the middle of the page titled “Approve or Deny this restaurant!” (because you are an administrator evaluating the restaurant for approval). In this section, click on the button labeled “Approve”. This will take you back to the Restaurant Approval page; notice that the restaurant you just approved (A new restaurant”) is no longer there. Now, navigate to the home page using “Home” in the navigation bar and observe that the restaurant “A new restaurant” has been added to the home page (and thus added to the website). 

Denying  A Request to Add  a Restaurant to the Web Application
Navigate to the Restaurant Approval page by using “Requests” in the navigation bar. Use the search bar to search for “A Denied Restaurant” and see that this restaurant appears beneath the search bar. Click on the restaurant to once again be taken to a very similar version of the Restaurant Details page. In the section titled “Approve or Deny this restaurant!”, click “Deny”. This will take you back to the Restaurant Approval page; notice that the restaurant titled “A Denied Restaurant” is no longer included in the list. Navigate back to the home page using the navigation bar, and see that the restaurant titled “A Denied Restaurant” is also not  in the list of restaurants in the home page (as it has been denied by the administrator).

Additional Functionalities
Mobile Friendliness
The application is mobile friendly in that the various pages resize to allow usability on smaller screens.

Logging Out
To log out of the application after logging in, you can click on “Logout” in the navigation bar. This will log you out and return you to the homepage of the web application.

ID Does Not Exist
If the user tries to access the Restaurant Details page of some restaurant that doesn’t exist by manually typing in the URL,, a “no such ID” page will be displayed. For example, if a user were to search for the following url: trentoneats.herokuapp.com/resdetails?id=5555, the page would display the following text: “No such id exists in the database” as 5555 is not a restaurant ID that is currently  in the database.

