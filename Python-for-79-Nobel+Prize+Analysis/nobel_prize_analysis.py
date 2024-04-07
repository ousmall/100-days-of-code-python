# -*- coding: utf-8 -*-
"""Nobel_Prize_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fEHa9rEyKS6ye9Y88Fm_8Yuv1FmmRH1V

# Setup and Context

### Introduction

On November 27, 1895, Alfred Nobel signed his last will in Paris. When it was opened after his death, the will caused a lot of controversy, as Nobel had left much of his wealth for the establishment of a prize.

Alfred Nobel dictates that his entire remaining estate should be used to endow “prizes to those who, during the preceding year, have conferred the greatest benefit to humankind”.

Every year the Nobel Prize is given to scientists and scholars in the categories chemistry, literature, physics, physiology or medicine, economics, and peace.

<img src=https://i.imgur.com/36pCx5Q.jpg>

Let's see what patterns we can find in the data of the past Nobel laureates. What can we learn about the Nobel prize and our world more generally?

### Upgrade plotly (only Google Colab Notebook)

Google Colab may not be running the latest version of plotly. If you're working in Google Colab, uncomment the line below, run the cell, and restart your notebook server.
"""

# %pip install --upgrade plotly

"""### Import Statements"""

import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

"""### Notebook Presentation"""

pd.options.display.float_format = '{:,.2f}'.format

"""### Read the Data"""

df_data = pd.read_csv('nobel_prize_data.csv')

"""Caveats: The exact birth dates for Michael Houghton, Venkatraman Ramakrishnan, and Nadia Murad are unknown. I've substituted them with mid-year estimate of July 2nd.

# Data Exploration & Cleaning

**Challenge**: Preliminary data exploration.
* What is the shape of `df_data`? How many rows and columns?
* What are the column names?
* In which year was the Nobel prize first awarded?
* Which year is the latest year included in the dataset?
"""

df_data.shape

df_data.info()

df_data.sort_values('year')

"""**Challange**:
* Are there any duplicate values in the dataset?
* Are there NaN values in the dataset?
* Which columns tend to have NaN values?
* How many NaN values are there per column?
* Why do these columns have NaN values?

### Check for Duplicates
"""

print(f'Any duplicates? {df_data.duplicated().values.any()}')

"""### Check for NaN Values"""

print(f'Any NaN values among the data? {df_data.isna().values.any()}')

df_data.isna().sum()

col_subset = ['year','category', 'laureate_type',
              'birth_date','full_name', 'organization_name']
df_data.loc[df_data.birth_date.isna()][col_subset].head()

col_subset = ['year','category', 'laureate_type','full_name', 'organization_name']
df_data.loc[df_data.organization_name.isna()][col_subset]

"""### Type Conversions

**Challenge**:
* Convert the `birth_date` column to Pandas `Datetime` objects
* Add a Column called `share_pct` which has the laureates' share as a percentage in the form of a floating-point number.

#### Convert Year and Birth Date to Datetime
"""

df_data.birth_date = pd.to_datetime(df_data.birth_date)

"""#### Add a Column with the Prize Share as a Percentage"""

separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denominator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denominator
# df_data['share_pct'] = (numerator / denominator).apply(lambda x: '{:.0%}'.format(x))

df_data.head()

"""# Plotly Donut Chart: Percentage of Male vs. Female Laureates

**Challenge**: Create a [donut chart using plotly](https://plotly.com/python/pie-charts/) which shows how many prizes went to men compared to how many prizes went to women. What percentage of all the prizes went to women?
"""

gender = df_data.sex.value_counts()
print(gender)

fig = px.pie(labels=gender.index, values=gender.values, title="Percentage of Gender", names=gender.index, hole=0.6)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
fig.show()

"""# Who were the first 3 Women to Win the Nobel Prize?

**Challenge**:
* What are the names of the first 3 female Nobel laureates?
* What did the win the prize for?
* What do you see in their `birth_country`? Were they part of an organisation?
"""

df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3]

"""# Find the Repeat Winners

**Challenge**: Did some people get a Nobel Prize more than once? If so, who were they?
"""

multiple_winners = df_data.duplicated(subset=['full_name'], keep=False) # output is True or False
winner_info = df_data[multiple_winners] # find out the True one

print(f'There are {winner_info.full_name.nunique()} winners who were awarded the Nobel Prize more than once')

# col_subset = ['year', 'category', 'laureate_type', 'full_name']
# winner_info[col_subset]

winner_info[['year', 'category', 'laureate_type', 'full_name']]

"""# Number of Prizes per Category

**Challenge**:
* In how many categories are prizes awarded?
* Create a plotly bar chart with the number of prizes awarded by category.
* Use the color scale called `Aggrnyl` to colour the chart, but don't show a color axis.
* Which category has the most number of prizes awarded?
* Which category has the fewest number of prizes awarded?
"""

# How many categories?
df_data.category.nunique()

prize_per_category = df_data.category.value_counts()
category_bar = px.bar(
    x=prize_per_category.index,
    y=prize_per_category.values,
    color=prize_per_category.values,
    color_continuous_scale='Aggrnyl',
    title="Number of Prizes Awarded per Category")

category_bar.update_layout(xaxis_title='Nobel Prize Category',
              coloraxis_showscale=False,
              yaxis_title='Number of Prizes')

category_bar.show()

"""**Challenge**:
* When was the first prize in the field of Economics awarded?
* Who did the prize go to?
"""

df_data[df_data.category == 'Economics'].sort_values('year')[:3]

"""# Male and Female Winners by Category

**Challenge**: Create a [plotly bar chart](https://plotly.com/python/bar-charts/) that shows the split between men and women by category.
* Hover over the bar chart. How many prizes went to women in Literature compared to Physics?

<img src=https://i.imgur.com/od8TfOp.png width=650>
"""

cat_men_women = df_data.groupby(['category', 'sex'], as_index=False).agg({'prize':pd.Series.count})
print(cat_men_women)

cat_men_women.sort_values("prize", ascending=False, inplace=True)
cat_men_women

gender_bar_split = px.bar(x=cat_men_women.category, y=cat_men_women.prize, color=cat_men_women.sex, title='Number of Prizes Awarded per Category split by Male and Female')
gender_bar_split.update_layout(xaxis_title="Nobel Prize Category", yaxis_title="Number of Prizes")
gender_bar_split.show()

"""# Number of Prizes Awarded Over Time

**Challenge**: Are more prizes awarded recently than when the prize was first created? Show the trend in awards visually.
* Count the number of prizes awarded every year.
* Create a 5 year rolling average of the number of prizes (Hint: see previous lessons analysing Google Trends).
* Using Matplotlib superimpose the rolling average on a scatter plot.
* Show a tick mark on the x-axis for every 5 years from 1900 to 2020. (Hint: you'll need to use NumPy).

<img src=https://i.imgur.com/4jqYuWC.png width=650>

* Use the [named colours](https://matplotlib.org/3.1.0/gallery/color/named_colors.html) to draw the data points in `dogerblue` while the rolling average is coloured in `crimson`.

<img src=https://i.imgur.com/u3RlcJn.png width=350>

* Looking at the chart, did the first and second world wars have an impact on the number of prizes being given out?
* What could be the reason for the trend in the chart?

"""

prize_per_year = df_data.groupby('year').count().prize # just fetch the prize data
print(prize_per_year)

# 5-year moving average
moving_average = prize_per_year.rolling(window=5).mean()
print(moving_average) # bo data in the first 4 years

# scatter chart
plt.scatter(x=prize_per_year.index,
      y=prize_per_year.values,
      color='dodgerblue', alpha=0.7, s=100)

# line chart
plt.plot(prize_per_year.index, moving_average.values, color='crimson', linewidth=3)

plt.show()

# styling by using Numpy
ticks = np.arange(1900, 2021, step=5) # scale

plt.figure(figsize=(8, 4), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=16)
plt.yticks(fontsize=10)
plt.xticks(ticks, fontsize=10, rotation=45)

ax = plt.gca() # get current axis
ax.set_xlim(1900, 2020)

ax.scatter(x=prize_per_year.index,
      y=prize_per_year.values,
      color='dodgerblue', alpha=0.4, s=100)

ax.plot(prize_per_year.index, moving_average.values, color='crimson', linewidth=3)

plt.show()

"""# Are More Prizes Shared Than Before?

**Challenge**: Investigate if more prizes are shared than before.

* Calculate the average prize share of the winners on a year by year basis.
* Calculate the 5 year rolling average of the percentage share.
* Copy-paste the cell from the chart you created above.
* Modify the code to add a secondary axis to your Matplotlib chart.
* Plot the rolling average of the prize share on this chart.
* See if you can invert the secondary y-axis to make the relationship even more clear.
"""

yearly_avg_share = df_data.groupby(by='year').agg({'share_pct': pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()

plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks, fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx() # create second y-axis
ax1.set_xlim(1900, 2020)

ax1.scatter(x=prize_per_year.index,
      y=prize_per_year.values,
      color='dodgerblue',
      alpha=0.7,
      s=100,
      label='Nobel Prizes Per Year')

ax1.plot(prize_per_year.index,
        moving_average.values,
        c='crimson',
        linewidth=3,
        label='Number of Nobel Prizes awarded every five years')

# Adding prize share plot on second axis
ax2.plot(prize_per_year.index,
        share_moving_average.values,
        c='grey',
        linewidth=3,
        label='Number of Nobel Prizes winners every five years')

# Add legend to chart
plt.legend(fontsize=14)

plt.show()

plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks, fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx() # create second y-axis
ax1.set_xlim(1900, 2020)

# draw a scatter chart
scatter_plot = ax1.scatter(x=prize_per_year.index,
                           y=prize_per_year.values,
                           c='dodgerblue',
                           alpha=0.7,
                           s=100,
                           label='Nobel Prizes Per Year')  # add label

# draw the first line chart
line_plot = ax1.plot(prize_per_year.index,
            moving_average.values,
            c='crimson',
            linewidth=3,
            label='Number of Nobel Prizes awarded every five years)')  # add label

# ax2.invert_yaxis()

# draw the second line chart
line_plot2 = ax2.plot(prize_per_year.index,
            share_moving_average.values,
            c='grey',
            linewidth=3,
            label='Number of Nobel Prizes winners every five years')  # add label

# get label object in ax1 and ax2
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

# add legend in the chart
plt.legend(handles=handles1 + handles2,
           labels=labels1 + labels2,
           fontsize=14,
           loc='upper center',
           bbox_to_anchor=(0.5, -0.1),  # adjust position
           fancybox=True,
           shadow=True)

plt.show()

"""## To see the relationship between the number of prizes and the laureate share even more clearly we can invert the second y-axis."""

plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)

# Can invert axis
ax2.invert_yaxis()

ax1.scatter(x=prize_per_year.index,
           y=prize_per_year.values,
           c='dodgerblue',
           alpha=0.7,
           s=100,)

ax1.plot(prize_per_year.index,
        moving_average.values,
        c='crimson',
        linewidth=3,)

ax2.plot(prize_per_year.index,
        share_moving_average.values,
        c='grey',
        linewidth=3,)

plt.show()

"""# The Countries with the Most Nobel Prizes

**Challenge**:
* Create a Pandas DataFrame called `top20_countries` that has the two columns. The `prize` column should contain the total number of prizes won.

<img src=https://i.imgur.com/6HM8rfB.png width=350>

* Is it best to use `birth_country`, `birth_country_current` or `organization_country`?
* What are some potential problems when using `birth_country` or any of the others? Which column is the least problematic?
* Then use plotly to create a horizontal bar chart showing the number of prizes won by each country. Here's what you're after:

<img src=https://i.imgur.com/agcJdRS.png width=750>

* What is the ranking for the top 20 countries in terms of the number of prizes?
"""

top_countries = df_data.groupby(['birth_country_current'], as_index=False).agg({'prize':pd.Series.count})

top_countries.sort_values(by='prize', inplace=True)

top20_countries = top_countries[-20:]

top20_countries

h_bar = px.bar(x=top20_countries.prize,
         y=top20_countries.birth_country_current,
         orientation='h',
         color=top20_countries.prize,
         color_continuous_scale='Viridis',
         title="Top 20 Prizes Countries")

h_bar.update_layout(xaxis_title="Number of Prizes",
          yaxis_title="Country",
          coloraxis_showscale=False)

h_bar.show()

"""# Use a Choropleth Map to Show the Number of Prizes Won by Country

* Create this choropleth map using [the plotly documentation](https://plotly.com/python/choropleth-maps/):

<img src=https://i.imgur.com/s4lqYZH.png>

* Experiment with [plotly's available colours](https://plotly.com/python/builtin-colorscales/). I quite like the sequential colour `matter` on this map.

Hint: You'll need to use a 3 letter country code for each country.

"""

df_countries = df_data.groupby(['birth_country_current', 'ISO'], as_index=False).agg({'prize': pd.Series.count})

df_countries.sort_values('prize', ascending=False)

world_map = px.choropleth(df_countries,
              locations='ISO',
              color='prize',
              hover_name='birth_country_current',
              color_continuous_scale=px.colors.sequential.matter)

world_map.update_layout(coloraxis_showscale=True)

world_map.show()

"""# In Which Categories are the Different Countries Winning Prizes?

**Challenge**: See if you can divide up the plotly bar chart you created above to show the which categories made up the total number of prizes. Here's what you're aiming for:

<img src=https://i.imgur.com/iGaIKCL.png>

* In which category are Germany and Japan the weakest compared to the United States?
* In which category does Germany have more prizes than the UK?
* In which categories does France have more prizes than Germany?
* Which category makes up most of Australia's nobel prizes?
* Which category makes up half of the prizes in the Netherlands?
* Does the United States have more prizes in Economics than all of France? What about in Physics or Medicine?


The hard part is preparing the data for this chart!


*Hint*: Take a two-step approach. The first step is grouping the data by country and category. Then you can create a DataFrame that looks something like this:

<img src=https://i.imgur.com/VKjzKa1.png width=450>

"""

cat_country = df_data.groupby(['birth_country_current', 'category'], as_index=False).agg({'prize': pd.Series.count})

cat_country.sort_values('prize', ascending=False, inplace=True)
cat_country

merge_df = pd.merge(cat_country, top20_countries, on='birth_country_current') # only show top 20 countries

merge_df.columns=['birth_country_current', 'category', 'cat_prize', 'total_prize']

merge_df.sort_values('total_prize', inplace=True)
merge_df

cat_cntry_bar = px.bar(x=merge_df.cat_prize,
             y=merge_df.birth_country_current,
             color=merge_df.category,
             orientation='h',
             title="Top 20 Prizes and Aategories Countries")

cat_cntry_bar.update_layout(xaxis_title='Number of Prizes', yaxis_title='Country')

cat_cntry_bar.show()

"""### Number of Prizes Won by Each Country Over Time

* When did the United States eclipse every other country in terms of the number of prizes won?
* Which country or countries were leading previously?
* Calculate the cumulative number of prizes won by each country in every year. Again, use the `birth_country_current` of the winner to calculate this.
* Create a [plotly line chart](https://plotly.com/python/line-charts/) where each country is a coloured line.
"""

prize_by_year = df_data.groupby(by=['birth_country_current', 'year'], as_index=False).count()
prize_by_year = prize_by_year.sort_values('year')[['year', 'birth_country_current', 'prize']]
prize_by_year

cumulative_prizes = prize_by_year.groupby(by=['birth_country_current', 'year']).sum().groupby(level=[0]).cumsum()
cumulative_prizes.reset_index(inplace=True)
cumulative_prizes

l_chart = px.line(cumulative_prizes,
          x='year',
          y='prize',
          color='birth_country_current',
          hover_name='birth_country_current')

l_chart.update_layout(xaxis_title='Year', yaxis_title='Number of Prizes')

l_chart.show()

"""# What are the Top Research Organisations?

**Challenge**: Create a bar chart showing the organisations affiliated with the Nobel laureates. It should looks something like this:

<img src=https://i.imgur.com/zZihj2p.png width=600>

* Which organisations make up the top 20?
* How many Nobel prize winners are affiliated with the University of Chicago and Harvard University?
"""

top20_orgs = df_data.organization_name.value_counts()[:20]
top20_orgs.sort_values(ascending=True, inplace=True)

org_bar = px.bar(x = top20_orgs.values,
          y = top20_orgs.index,
          orientation='h',
          color=top20_orgs.values,
          color_continuous_scale=px.colors.sequential.haline,
          title='Top 20 Research Institutions by Number of Prizes')

org_bar.update_layout(xaxis_title='Number of Prizes',
           yaxis_title='Institution',
           coloraxis_showscale=False)

org_bar.show()

"""# Which Cities Make the Most Discoveries?

Where do major discoveries take place?  

**Challenge**:
* Create another plotly bar chart graphing the top 20 organisation cities of the research institutions associated with a Nobel laureate.
* Where is the number one hotspot for discoveries in the world?
* Which city in Europe has had the most discoveries?
"""

top20_org_cities = df_data.organization_city.value_counts()[:20]
top20_org_cities.sort_values(ascending=True, inplace=True)

city_bar2 = px.bar(x = top20_org_cities.values,
           y = top20_org_cities.index,
           orientation='h',
           color=top20_org_cities.values,
           color_continuous_scale=px.colors.sequential.Plasma,
           title='Which Cities Do the Most Research?')

city_bar2.update_layout(xaxis_title='Number of Prizes',
            yaxis_title='City',
            coloraxis_showscale=False)

city_bar2.show()

"""# Where are Nobel Laureates Born? Chart the Laureate Birth Cities

**Challenge**:
* Create a plotly bar chart graphing the top 20 birth cities of Nobel laureates.
* Use a named colour scale called `Plasma` for the chart.
* What percentage of the United States prizes came from Nobel laureates born in New York?
* How many Nobel laureates were born in London, Paris and Vienna?
* Out of the top 5 cities, how many are in the United States?

"""

top20_cities = df_data.birth_city.value_counts()[:20]
top20_cities.sort_values(ascending=True, inplace=True)

city_bar = px.bar(x=top20_cities.values,
          y=top20_cities.index,
          orientation='h',
          color=top20_cities.values,
          color_continuous_scale=px.colors.sequential.Plasma,
          title='Where were the Nobel Laureates Born?')

city_bar.update_layout(xaxis_title='Number of Prizes',
            yaxis_title='City of Birth',
            coloraxis_showscale=False)

city_bar.show()

"""# Plotly Sunburst Chart: Combine Country, City, and Organisation

**Challenge**:

* Create a DataFrame that groups the number of prizes by organisation.
* Then use the [plotly documentation to create a sunburst chart](https://plotly.com/python/sunburst-charts/)
* Click around in your chart, what do you notice about Germany and France?


Here's what you're aiming for:

<img src=https://i.imgur.com/cemX4m5.png width=300>


"""

country_city_org = df_data.groupby(by=['organization_country', 'organization_city',
                   'organization_name'], as_index=False).agg({'prize': pd.Series.count})

country_city_org = country_city_org.sort_values('prize', ascending=False)
country_city_org

burst = px.sunburst(country_city_org,
           path=['organization_country', 'organization_city', 'organization_name'],
           values='prize',
           title='Where do Discoveries Take Place?')

burst.update_layout(xaxis_title='Number of Prizes',
          yaxis_title='City',
          coloraxis_showscale=False)

burst.show()

"""# Patterns in the Laureate Age at the Time of the Award

How Old Are the Laureates When the Win the Prize?

**Challenge**: Calculate the age of the laureate in the year of the ceremony and add this as a column called `winning_age` to the `df_data` DataFrame. Hint: you can use [this](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.html) to help you.


"""

birth_year = df_data.birth_date.dt.year

df_data['winning_age'] = df_data.year - birth_year # create a new column

df_data.head()

"""### Who were the oldest and youngest winners?

**Challenge**:
* What are the names of the youngest and oldest Nobel laureate?
* What did they win the prize for?
* What is the average age of a winner?
* 75% of laureates are younger than what age when they receive the prize?
* Use Seaborn to [create histogram](https://seaborn.pydata.org/generated/seaborn.histplot.html) to visualise the distribution of laureate age at the time of winning. Experiment with the number of `bins` to see how the visualisation changes.
"""

df_data.loc[df_data.winning_age.idxmax()]

display(df_data.nlargest(n=1, columns='winning_age'))
display(df_data.nsmallest(n=1, columns='winning_age'))

"""### Descriptive Statistics for the Laureate Age at Time of Award

* Calculate the descriptive statistics for the age at the time of the award.
* Then visualise the distribution in the form of a histogram using [Seaborn's .histplot() function](https://seaborn.pydata.org/generated/seaborn.histplot.html).
* Experiment with the `bin` size. Try 10, 20, 30, and 50.  
"""

df_data.winning_age.describe()

"""### Age at Time of Award throughout History

Are Nobel laureates being nominated later in life than before? Have the ages of laureates at the time of the award increased or decreased over time?

**Challenge**

* Use Seaborn to [create a .regplot](https://seaborn.pydata.org/generated/seaborn.regplot.html?highlight=regplot#seaborn.regplot) with a trendline.
* Set the `lowess` parameter to `True` to show a moving average of the linear fit.
* According to the best fit line, how old were Nobel laureates in the years 1900-1940 when they were awarded the prize?
* According to the best fit line, what age would it predict for a Nobel laureate in 2020?

"""

plt.figure(figsize=(8, 4), dpi=200)
sns.histplot(data=df_data,
       x=df_data.winning_age,
       bins=30)

plt.xlabel('Age')
plt.title('Distribution of Age on Receipt of Prize')

plt.show()

plt.figure(figsize=(8,4), dpi=200)

with sns.axes_style("whitegrid"):
    sns.regplot(data=df_data,
          x='year',
          y='winning_age',
          lowess=True,
          scatter_kws = {'alpha': 0.4},
          line_kws={'color': 'black'})

plt.show()

"""### Winning Age Across the Nobel Prize Categories

How does the age of laureates vary by category?

* Use Seaborn's [`.boxplot()`](https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot) to show how the mean, quartiles, max, and minimum values vary across categories. Which category has the longest "whiskers"?
* In which prize category are the average winners the oldest?
* In which prize category are the average winners the youngest?
"""

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.boxplot(data=df_data,
          x='category',
          y='winning_age')

plt.show()

"""**Challenge**
* Now use Seaborn's [`.lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html?highlight=lmplot#seaborn.lmplot) and the `row` parameter to create 6 separate charts for each prize category. Again set `lowess` to `True`.
* What are the winning age trends in each category?
* Which category has the age trending up and which category has the age trending down?
* Is this `.lmplot()` telling a different story from the `.boxplot()`?
* Create another chart with Seaborn. This time use `.lmplot()` to put all 6 categories on the same chart using the `hue` parameter.

"""

# show each category by using 'row'
with sns.axes_style('whitegrid'):
    sns.lmplot(data=df_data,
          x='year',
          y='winning_age',
          row = 'category',
          lowess=True,
          aspect=2,
          scatter_kws = {'alpha': 0.6},
          line_kws = {'color': 'black'},)

plt.show()

# combine all categories by using 'hue'
with sns.axes_style("whitegrid"):
    sns.lmplot(data=df_data,
          x='year',
          y='winning_age',
          hue='category',
          lowess=True,
          aspect=2,
          scatter_kws={'alpha': 0.5},
          line_kws={'linewidth': 5})

plt.show()