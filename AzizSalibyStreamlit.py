# Import Libraries 
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


Menu = option_menu(None, ["Dataset","Quiz","Dashboard"],icons=["cloud","clipboard-check","bar-chart-line"],menu_icon="cast", default_index=0, orientation="horizontal", styles={"container": {"padding": "0!important", "background-color": "#fafafa"},"icon": {"color": "black", "font-size": "25px"}, "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},"nav-link-selected": {"background-color": "purple"},})
if Menu == "Dataset": st.title('Suicide Dataset')
if Menu == "Dashboard": st.title('Suicide Dashboard')



# Setting a small introduction on the suicide topic
if Menu=="Dataset":st.caption("Suicide is the attempt when someone try to harm himself with the intent to end their life. For a long time this topic has been a major problem for NGOs and governments since it is considered as taboo and doesn't get the attention it deserves. But it is really important to study the trend of this problem to get insights about: where we should launch prevention campaign, in which country, the target population... in order to minimize its growth")

# Loading the Data
if Menu=="Dataset":st.header("Take a first look at the data")
data = pd.read_csv("master.csv")
if Menu=="Dataset":st.write(data)

if Menu=="Dataset":col1, col2, col3 = st.columns(3)
if Menu=="Dataset":col1.metric("Columns", "12",delta_color="inverse")
if Menu=="Dataset":col2.metric("Records", "27820",delta_color="inverse")
if Menu=="Dataset":col3.metric("Number of countries", "90",delta_color="inverse")


# printing general informations about our data
data.info()

# Checking for missing data in the columns
data.isnull().sum()

# Dropping the column that contains missing value
data.drop("HDI for year",axis=1,inplace=True)

# Dividing the data into 2 subcategory, data that contains all the information on males and the other on females
data_men = data[data.sex == "male"]
data_women = data[data.sex == "female"]

#Now our data is clean and splitted and ready for the EDA part

# Pie Chart 
# The most important question Who commit suicides more males or females

if Menu=="Dashboard":st.header(" Who commit suicide more? females or males?")
if Menu=="Dashboard":fig= go.Figure(data=[go.Pie(labels=['Males', 'Females'], values=[data_men["suicides_no"].sum(),data_women["suicides_no"].sum()])])
if Menu=="Dashboard":st.plotly_chart(fig)
if Menu=="Dashboard":st.write("As clear in the pie charts 5,188,910 (76.9%) male and 1,559,510 (23.1%) female has committed suicide from 1985 till 2016, which implies that males are 3.3 times more likely to commit suicide than females.")


# Same Plot for all countries 

if Menu=="Dashboard":st.header("Suicide percentage in a specific country")

if Menu=="Dashboard":
    option = st.selectbox(
     'Select Please your Specific country',
     ('Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
 'Austria' ,'Azerbaijan' ,'Bahamas', 'Bahrain' ,'Barbados', 'Belarus', 'Belgium',
 'Belize' ,'Bosnia and Herzegovina' ,'Brazil', 'Bulgaria' ,'Cabo Verde',
 'Canada' ,'Chile', 'Colombia' ,'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
 'Czech Republic', 'Denmark' ,'Dominica', 'Ecuador', 'El Salvador', 'Estonia'
 'Fiji', 'Finland', 'France' ,'Georgia', 'Germany' ,'Greece', 'Grenada',
 'Guatemala' ,'Guyana' ,'Hungary' ,'Iceland' ,'Ireland', 'Israel', 'Italy',
 'Jamaica' ,'Japan', 'Kazakhstan' ,'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
 'Lithuania' ,'Luxembourg', 'Macau', 'Maldives', 'Malta', 'Mauritius', 'Mexico',
 'Mongolia', 'Montenegro', 'Netherlands' ,'New Zealand', 'Nicaragua' ,'Norway',
 'Oman' ,'Panama' ,'Paraguay' ,'Philippines', 'Poland', 'Portugal',
 'Puerto Rico', 'Qatar', 'Republic of Korea' ,'Romania', 'Russian Federation',
 'Saint Kitts and Nevis' ,'Saint Lucia', 'Saint Vincent and Grenadines',
 'San Marino', 'Serbia', 'Seychelles', 'Singapore' ,'Slovakia' ,'Slovenia',
 'South Africa', 'Spain', 'Sri Lanka' ,'Suriname' ,'Sweden', 'Switzerland',
 'Thailand' ,'Trinidad and Tobago' ,'Turkey', 'Turkmenistan', 'Ukraine',
 'United Arab Emirates' ,'United Kingdom', 'United States', 'Uruguay',
 'Uzbekistan'))
if Menu=="Dashboard":st.write('You selected:', option)
if Menu=="Dashboard":datacountry1 = data[data["country"]==option]
if Menu=="Dashboard":data_men1 = datacountry1[data.sex == "male"]
if Menu=="Dashboard":data_women1 = datacountry1[data.sex == "female"]
if Menu=="Dashboard":plt.pie([data_men1["suicides_no"].sum(),data_women1["suicides_no"].sum() ], labels= ['Percantage of men that commited suicides', 'Percentage of women that commited suiced'], autopct='%1.1f%%')
if Menu=="Dashboard":fig= go.Figure(data=[go.Pie(labels=['Males', 'Females'], values=[data_men1["suicides_no"].sum(),data_women1["suicides_no"].sum()])])
if Menu=="Dashboard":st.plotly_chart(fig)

# Number of suicides across the years
if Menu=="Dashboard":st.header("Number of Suicide by gender across years ")

if Menu=="Dashboard":Female = st.checkbox('Female')
if Menu=="Dashboard":Male = st.checkbox('Male')
if Menu=="Dashboard":Both = st.checkbox('Male-Female')
if Menu=="Dashboard":figw = px.histogram(data_women,x='year',y='suicides_no',text_auto=True)
if Menu=="Dashboard":figw.update_traces(opacity=1)
if Menu=="Dashboard":figw.update_layout(bargap=0.2,
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="Black",
    legend_title_font_color="black")
if Menu=="Dashboard":figm = px.histogram(data_men,x='year',y='suicides_no',text_auto=True)
if Menu=="Dashboard":figm.update_traces(opacity=1)
if Menu=="Dashboard":figm.update_layout(bargap=0.2,
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="Black",
    legend_title_font_color="black")
       
if Menu=="Dashboard":fig1= px.histogram(data,x='year',y='suicides_no', color='sex',text_auto=True)

if Menu=="Dashboard":fig1.update_traces(opacity=1)
if Menu=="Dashboard":fig1.update_layout(bargap=0.2,
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="Black",
    legend_title_font_color="black")

    
    
       
if Menu=="Dashboard":
    if Female:
        st.plotly_chart(figw)

if Menu=="Dashboard":
    if Male:
        st.plotly_chart(figm)
    
if Menu=="Dashboard":
    if Both:
        st.plotly_chart(fig1)
    


#Lets Take a look on the trend of suicides in the world.
if Menu=="Dashboard":st.header("Suicide Trend")
total_gender = data[['sex', 'suicides_no', 'population', 'year', 'country']]
total_gender['proportion'] = total_gender.suicides_no / total_gender.population
gender_prop = pd.DataFrame(total_gender.groupby(['year', 'sex'])['proportion'].mean()).unstack()
fig = go.Figure()

fig.add_trace(go.Scatter(x= gender_prop.index,
                         y = gender_prop.proportion.male,
                         mode = 'lines+markers',
                         name = 'Male death ',
                         marker = dict(color='#FF9900')))

fig.add_trace(go.Scatter(x= gender_prop.index,
                         y = gender_prop.proportion.female,
                         mode = 'lines+markers',
                         name = 'Female death',
                         marker = dict(color='rgb(179,222,105)')))

fig.update_layout(height=500, width=900,font = dict(color="black"))

fig.update_xaxes(title_text = 'Year', color="RebeccaPurple")
fig.update_yaxes(title_text = 'Proportion', color="RebeccaPurple")
if Menu=="Dashboard":st.plotly_chart(fig)

if Menu=="Dashboard":st.write("The rate of suicides reaches its peak in 1995 for males (249 suicide attempt per 100K population). First, it began to increase from 1985 (178 suicide attempt/100k) to reach its peak in 1995 and after that year it took a negative trend to reach the lowest rate recorded in 2015 (175 suicide/100k). Whereas the rate of suicides for females didn’t witnessed a high decrease or increase in its rate, it’s kind of stable trend (between 48 and 64 suicide/100k population). ")


# Number of suicides/100k pop in all countries (using plotly map)
if Menu=="Dashboard":st.header("Geographical representation of suicide rate")
if Menu=="Dashboard":geo = data.groupby(by=['country']).agg({"suicides/100k pop": ['sum']})
if Menu=="Dashboard":geo.columns = ['total_suicide']
if Menu=="Dashboard":geo.reset_index(inplace=True)

if Menu=="Dashboard":fig = px.choropleth(geo, locations="country", locationmode='country names',
                    color="total_suicide", 
                    hover_name="country",
                    color_continuous_scale='sunset')

if Menu=="Dashboard":st.plotly_chart(fig)

if Menu=="Dashboard":st.write("Asia and Europe have highest rate in suicide than North America, South America and Australia. For instance Russia, Ukraine, Kazakhstan, Bulgaria, France score the highest suicide rate. Whic means most probably that countries with long winter season have the highest number of suicides")

#Top 10 countries which recored the highest suicides rates across the years
if Menu=="Dashboard":st.header("Top 10 Countries with the highest Suicide Rate")

if Menu=="Dashboard":Year = st.slider('Select The year Please', 1987, 2016, 1988)

if Menu=="Dashboard":datayear = data[data["year"]==Year]

if Menu=="Dashboard":f, ax = plt.subplots(1,1, figsize=(10,8))
if Menu=="Dashboard":data_country_total = datayear.groupby(by=['country']).agg({'suicides/100k pop': ['sum']})
if Menu=="Dashboard":data_country_total.columns = ['total_suicide']
if Menu=="Dashboard":data_country_total.reset_index(inplace=True)
if Menu=="Dashboard":data_country_total = data_country_total.sort_values(by=['total_suicide'], ascending=False).head(10)

if Menu=="Dashboard":fig = px.bar(data_country_total, x='total_suicide', y='country',orientation='h')

if Menu=="Dashboard":plt.title('Top 10 Countries With Highest Number Of Suicides')

if Menu=="Dashboard":st.plotly_chart(fig)

if Menu=="Dashboard": st.write("In the last Figure, you can pick the year that you want on the slider and see the top 10 countries that have the highest number of suicides for this chosen year. For example, for year 1988 the top 10 countries are: Singapore, Austria, Finland, France, Bulgaria, Ukraine, Japan, Belgium and Mauritius")

#Recommendation Page in the Dashboard.

if Menu=="Quiz":st.title("Here's a small quiz to test your Suicide knowledge before taking a deep dive in the suicide concepts anf facts.")
if Menu=="Quiz":st.write("1- Who do you think commit suicide more:")
if Menu=="Quiz":st.write("")
if Menu=="Quiz":Female= st.checkbox('Females')
if Menu=="Quiz":Male= st.checkbox('Males')
if Menu=="Quiz":
    if Female:
        st.write("False")
if Menu=="Quiz":
    if Male:
        st.write("Correct, Males are 3.3 times more likely to commit suicides than females")
if Menu=="Quiz":st.write("")
if Menu=="Quiz":st.write("")
          
        
if Menu=="Quiz":st.write("2- In which year-interval do you think that the world witnessed the highest suicide rate:")
if Menu=="Quiz":st.write("")
if Menu=="Quiz":a= st.checkbox('[1985-1990]')
if Menu=="Quiz":b= st.checkbox('[1990-1995]')
if Menu=="Quiz":c= st.checkbox('[1995-2000]')
if Menu=="Quiz":d= st.checkbox('[2000-2015]')
if Menu=="Quiz":
    if a|c|d:
        st.write("False")
if Menu=="Quiz":
    if b:
        st.write("Correct, in 1995 the world record the highest suicide rate reading 249 suicide per 100k popultaion")

if Menu=="Quiz":st.write("") 
if Menu=="Quiz":st.write("")
        
if Menu=="Quiz":st.write("3- Which continent have the highest suicide rate from 1985 till 2015 :")
if Menu=="Quiz":st.write("")
if Menu=="Quiz":e= st.checkbox('Europe and Asia')
if Menu=="Quiz":f= st.checkbox(' North America, South America and Australia')
if Menu=="Quiz":
    if e:
        st.write("Correct, Keep going")
if Menu=="Quiz":
    if f:
        st.write("Oups, False")
        
if Menu=="Quiz":st.write("")
if Menu=="Quiz":st.write("")
        
if Menu=="Quiz":st.write("Please use the last graph in the Dashboard page to answer this question")
if Menu=="Quiz":st.write("4- For year 1990 which country have the highest suicide rate")
if Menu=="Quiz":st.write("")
if Menu=="Quiz":q= st.checkbox('France')
if Menu=="Quiz":w= st.checkbox('Ukraine')
if Menu=="Quiz":r= st.checkbox('Belgium')
if Menu=="Quiz":t= st.checkbox('Russian Federation')

if Menu=="Quiz":
    if q|w|r:
        st.write("False")
if Menu=="Quiz":
    if f:
        st.write("Correct")

if Menu=="Quiz":st.write("")
if Menu=="Quiz":st.write("")

if Menu=="Quiz": st.title("I hope you enjoyed it ")

 
st.caption("AzizSaliby-SuicideDashboard") 

if Menu=="Dashboard": st.caption("Thank You")




