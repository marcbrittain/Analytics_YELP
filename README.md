
# Restaurant Rating Finder 
* Created By: *Marc Brittain*

The function of this tool is to use the improve upon the already built YELP API package. In creating this tool, I followed the recommended advice from the YELP website which suggested to store your personal API key and information in a seperate file and to then call the file itself. The functions are built assuming one has stored the API information as recommended from YELP. These particular functions are made for accessing restaurant information for multiple cities. The max restaurants that can be returned for a given city is 1000, and note that YELP only allows 25,000 calls per day so the max amount of cities are 25. My goal was to create this easy-to-use package to help access the abundance of information on the YELP API. More analytical tools are currently in progress. Let's begin with a quick tutorial.

# Installation

There are 3 modules that need to be installed to use this package:
* pandas module : allows the creation of dataframe which can be easily written out to excel files
* numpy module : useful when converting dataframes to arrays (should already be installed with python)
* YELP API : available on YELP's website. The tool to grab all of the raw information

To install, download the python file 'findCity.py' which contains all of the functions. From there you will need to create a seperate file in the same directory where 'findCity' downloaded called 'config_secret.json'. This is where you will store your YELP API key that you obtain from their website. Below is how they recommend setting up the file itself.


```python
{
    "consumer_key": "your_consumer_key",
    "consumer_secret": "your_consumer_secret",
    "token": "your_token",
    "token_secret": "your_token_secret"
}
```

After the file with your API information is set up, the next step is to run the script findCity, which contains all of the functions.


```python
run findCity
```

This should only take a second to run the script. The main function in the script is called restaurant_ratings_city. What is returned from this function is a dataframe so if one wants to utilize the data, assign to a variable as shown below. 


```python
df = restaurant_ratings_city() # call the function and assign it to a variable 'df'

# then follow the prompt and hit enter
# this step may take a little while due to the fact that it is getting all of the information from the YELP server.
```

    Enter City Names (comma separated, no spaces): Chicago,Miami,Austin



```python
df.head() # now call the variable to see the information that it collected

# the .head() function returns only the first 5 entries to get a preview
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Chicago Restaurants</th>
      <th>Chicago Ratings</th>
      <th>Chicago Phone Number</th>
      <th>Miami Restaurants</th>
      <th>Miami Ratings</th>
      <th>Miami Phone Number</th>
      <th>Austin Restaurants</th>
      <th>Austin Ratings</th>
      <th>Austin Phone Number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Frank and Mary's Tavern</td>
      <td>4.5</td>
      <td>7734638179</td>
      <td>Cardon Y El Tirano</td>
      <td>5.0</td>
      <td>3053921257</td>
      <td>Baretto</td>
      <td>4.5</td>
      <td>5123457994</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Crab Pad</td>
      <td>4.5</td>
      <td>7733608332</td>
      <td>Doce Provisions</td>
      <td>4.5</td>
      <td>7864520161</td>
      <td>Blue Moon Bar &amp; Grill</td>
      <td>3.5</td>
      <td>5129169951</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Giant</td>
      <td>4.5</td>
      <td>7732520997</td>
      <td>Glass &amp; Vine</td>
      <td>4.0</td>
      <td>3052005268</td>
      <td>Coast Bar &amp; Kitchen</td>
      <td>4.5</td>
      <td>5124674621</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pub Royale</td>
      <td>4.0</td>
      <td>7736616874</td>
      <td>Red Carpet Italian</td>
      <td>5.0</td>
      <td>3055294220</td>
      <td>Boteco</td>
      <td>5.0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aloha Poke Co</td>
      <td>4.0</td>
      <td>None</td>
      <td>Diced</td>
      <td>4.5</td>
      <td>7867732190</td>
      <td>Hey!... You Gonna Eat or What?</td>
      <td>4.5</td>
      <td>5122963547</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail() # let's see how many restaurants it returned

# the .tail() function returns the last 5 entries 
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Chicago Restaurants</th>
      <th>Chicago Ratings</th>
      <th>Chicago Phone Number</th>
      <th>Miami Restaurants</th>
      <th>Miami Ratings</th>
      <th>Miami Phone Number</th>
      <th>Austin Restaurants</th>
      <th>Austin Ratings</th>
      <th>Austin Phone Number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>995</th>
      <td>Valois</td>
      <td>4.0</td>
      <td>7736670647</td>
      <td>Chez Le Bebe</td>
      <td>3.5</td>
      <td>3057517639</td>
      <td>Downtown Jo's Coffee Shop</td>
      <td>3.5</td>
      <td>5124699003</td>
    </tr>
    <tr>
      <th>996</th>
      <td>Beef &amp; Burger</td>
      <td>4.0</td>
      <td>7736854960</td>
      <td>El Tambo Grill</td>
      <td>3.5</td>
      <td>7867099943</td>
      <td>Caffe Yolly</td>
      <td>4.5</td>
      <td>5124685575</td>
    </tr>
    <tr>
      <th>997</th>
      <td>La Casa De Samuel</td>
      <td>3.5</td>
      <td>7733767474</td>
      <td>Ceviche &amp; Grill</td>
      <td>4.0</td>
      <td>3052286072</td>
      <td>Danny's BBQ</td>
      <td>4.5</td>
      <td>None</td>
    </tr>
    <tr>
      <th>998</th>
      <td>Mr. B's BBQ</td>
      <td>4.0</td>
      <td>7738801100</td>
      <td>Charcoals Latin Grill</td>
      <td>3.5</td>
      <td>3054630209</td>
      <td>Heros Gyros</td>
      <td>4.5</td>
      <td>5124689735</td>
    </tr>
    <tr>
      <th>999</th>
      <td>Smoke Daddy</td>
      <td>3.5</td>
      <td>7737726656</td>
      <td>Luis Galindo's Latin American 2</td>
      <td>3.5</td>
      <td>3052277002</td>
      <td>Giovanni's Pizza Stand</td>
      <td>4.5</td>
      <td>5124427033</td>
    </tr>
  </tbody>
</table>
</div>



We can now see that we have 3,000 restaurants with their YELP rating, phone number, and name. If one wants to have all of this information in an excel workbook, just execute the line of code below and it will be formatted just like the dataframe.


```python
df.to_excel('title_of_excel_file.xlsx')
```
