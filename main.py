import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import plotly.express as px

with st.sidebar:
    st.title("Commercial imports and exports  (Mhw)")
    st.sidebar.title('Menu')
    st.sidebar.subheader('Introduction')
    st.sidebar.markdown('Raw datas')
    st.sidebar.markdown('Amount of datas')
    st.sidebar.markdown('Import-Export in France in a year')
    st.sidebar.markdown('   ')
    st.sidebar.markdown('Countries exchanges with France')
    st.sidebar.markdown(
        """
            <br>
            <p> Project done by Damien LIN</p>
            <div class="conteneur">
                <div class="ma-div">
                    <a href="https://github.com/Corpsy667" target="_blank" style="text-decoration: none; color:white">
                    <div style="background-color: white; color: black; padding: 10px 20px; border-radius: 5px; display: flex; align-items: center; width: 200px; justify-content: center;">
                        <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.13.0/icons/github.svg" alt="Github" height="20px" style="margin-right: 10px;">
                        Github
                    </div>
                </a>
                </div>
            </div>
            """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        """
            <br>
            <div class="conteneur">
                <div class="ma-div">
                    <a href="https://www.linkedin.com/in/damien-lin-a217071b7/" target="_blank" style="text-decoration: none; color:white">
                    <div style="background-color: #0077B5; color: white; padding: 10px 20px; border-radius: 5px; display: flex; align-items: center; width: 200px; justify-content: center;">
                        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" alt="LinkedIn Logo" height="20px" style="margin-right: 10px;">
                        LinkedIn
                    </div>
                </a>
                <p> Efrei Paris - Promo 2025 </p>
                </div>
            </div>
            """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        """
            <br>
            <div class="conteneur">
            <p> Under the supervision of : Mano Joseph   MATHEW </p>
                <div class="ma-div">
                    <a href="https://www.linkedin.com/in/manomathew/" target="_blank" style="text-decoration: none; color:white">
                    <div style="background-color: #0077B5; color: white; padding: 10px 20px; border-radius: 5px; display: flex; align-items: center; width: 200px; justify-content: center;">
                        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" alt="LinkedIn Logo" height="20px" style="margin-right: 10px;">
                        LinkedIn
                    </div>
                </a>
                </div>
            </div>
            """,
        unsafe_allow_html=True)
    st.markdown("#datavz23efrei")

st.title('Commercial exchanges with France')
st.subheader("Introduction")
st.markdown("France is a country that we all know at least a bit, either for the Eiffel Tower or for their croissants")
st.markdown("But what do you know about import export ?")
st.markdown("First what is import-export ?")
st.markdown("Basically it's the exchanges between two parts : you buy something to someone and sell it to someone else")
st.markdown("Here, Let's load data France exchanges' from 2005 to 2021 with other countries such as Switzerland, Spain, "
            "Italy, CWE(Germany, Belgium, Austria, Luxembourg, The Netherlands) and UK")
button_load = st.button("Reload data !")
data_load_state = st.text("Loading data...")
df = pd.read_csv('imports-exports-commerciaux.csv', delimiter=";")
data_load_state.text('Loading data... Done !')
sleep(1)
data_load_state.empty()
st.subheader('raw datas : ')
st.dataframe(df)
st.link_button("Go to the website where dataset comes from", "https://www.data.gouv.fr/fr/datasets/imports-et-exports-commerciaux-2005-a-2021/")

# Preparing data
print(df.dtypes)
# Changing dates into datetime
datetime_text = st.text("The date is not in the right format")
df['date'] = pd.to_datetime(df['date'])
sleep(0.1)
datetime_text.text("The date is now in the right format (datetime). :)")
sleep(1)
datetime_text.empty()
sleep(0.1)
# Sorting values
sorting_text = st.text("Let's now sort the data")
df.sort_values("date", inplace=True)
sleep(0.1)
sorting_text.text("Data... Sorted")
sleep(1)
sorting_text.empty()
sleep(0.1)
# gb_fr had a problem, so I decided to change it by myself
def convert_to_float(value):
    # Convert the value to a string, remove non-numeric characters, and convert to float
    cleaned_value = value if isinstance(value, str) else str(value)
    cleaned_value = cleaned_value.replace(' ', '').replace(',', '.')
    return float(cleaned_value)

df['gb_fr'] = df['gb_fr'].apply(convert_to_float)
st.write("Aranged data : ",df)
st.title("Let's start the analyze of the data")
# Histogram
hist_values1 = np.histogram(df['date'].dt.day, bins=32, range=(0, 32))[0]
hist_values2 = np.histogram(df['date'].dt.month, bins=13, range=(0, 13))[0]
hist_values3 = np.histogram(df['date'].dt.year, bins=17, range=(2005, 2022))[0]
st.subheader("Which days have the most amount of data ?")
st.bar_chart(hist_values1)
st.write(
    "We notice that all datas are evenly shared in days except for 31 30 and 29 because some months do not have them")
st.subheader("Which months have the most amount of data ?")
st.bar_chart(hist_values2)
st.markdown(
    "We notice that all datas are evenly shared in months (around 12k datas per month), except for febuary where there's only 29 days so less possibility of datas")
st.subheader("Which years have the most amount of data ?")
st.bar_chart(hist_values3)
st.markdown("In years too we can see that it is perfectly shared in days and for leap years there are a bit more datas")

st.subheader("With this information:")
st.markdown(
    "We can agree with the fact that the import export datas are evenly shared and that the dataset is already perfectly aranged for use")

# Year exports
st.title("Let's now check what we can do with those aranged data :")
st.subheader("Let's start with the exchanges in years")
year_to_filter = st.slider('year for exports', 2005, 2021, 2008)
filtered_data = df[df['date'].dt.year == year_to_filter]
st.subheader(f'Exchanges in {year_to_filter}')
st.write(filtered_data)

# plot the (scatter) of exports in function of dates
fig, ax = plt.subplots()
ax.scatter(filtered_data['date'].dt.month, filtered_data['export_france'], color='red')
plt.xlabel('Month')
plt.ylabel('Exports')
plt.title(f'Scatter of exports from France at year : {year_to_filter}')
st.pyplot(fig)
st.markdown(f"Just for your information, the total amount of imports is : {df['export_france'].sum()}, and on the year "
            f"{year_to_filter} there are : {filtered_data['export_france'].sum()}")

# Import now
checkbox_year = st.checkbox("same year for imports and export ?")
if checkbox_year:
    year_to_filter2 = year_to_filter
else:
    year_to_filter2 = st.slider('year for imports', 2005, 2021, 2008)
filtered_data2 = df[df['date'].dt.year == year_to_filter2]
st.subheader(f'Scatter of imports to France at year : {year_to_filter2}')
fig2, ax2 = plt.subplots()
ax2.scatter(filtered_data2['date'].dt.month, filtered_data2['import_france'], color='yellow')
plt.xlabel('Date')
plt.ylabel('Imports')
plt.title(f'Scatter of imports to France at year : {year_to_filter2}')
st.pyplot(fig2)
st.markdown(f"Just for your information, the total amount of imports is : {df['import_france'].sum()}, and on the year "
            f"{year_to_filter2} there are : {filtered_data2['import_france'].sum()}")

filtered_data2 = df[df['date'].dt.year == year_to_filter2]
st.subheader(f'Histogram of imports of {year_to_filter2} and exports of {year_to_filter} in France')

# Comparing them in a histogram
fig3, ax3 = plt.subplots()
ax3.hist(filtered_data['export_france'], bins=50, alpha=0.9, label='export')
ax3.hist(filtered_data2['import_france'], bins=50, alpha=0.9, label='import')
ax3.set_xlabel('Import//export value')
ax3.set_ylabel('Amount of the import//export')
ax3.set_title('Histogram')
ax3.legend()
st.pyplot(fig3)
st.subheader("Import export total: ")
st.markdown(f"Total amount of import export of {year_to_filter}: "
            f"{round(filtered_data['import_france'].sum(), 2)}+{round(filtered_data['export_france'].sum(), 2)} = "
            f"{round(filtered_data['import_france'].sum() + filtered_data['export_france'].sum(), 2)}.")

st.markdown(f"Total amount of import export of all time: "
            f"{round(df['import_france'].sum(), 2)}+{round(df['export_france'].sum(), 2)} = "
            f"{round(df['import_france'].sum() + df['export_france'].sum(), 2)}.")
st.markdown("This means that France is a country that exports more in Europe than import. That implicates : ")
st.markdown("   - France imports less than the half of its exports")
st.markdown("   - France produces more than it takes from the others.")
st.markdown("   - France produces quite a lot also for the others compared to what he takes.")
st.markdown("   - Following these data we might think that France is rich...")

st.title("Here's the exchange with France part : ")
selectbox_exchange = st.multiselect(
    "Which exchange do you want to see ?",
    ["date", "fr_gb", "gb_fr", "fr_cwe", "cwe_fr", "fr_ch", "ch_fr", "fr_it", "it_fr", "fr_es", "es_fr"], "date")
# st.write("You selected : ", selectbox_exchange)
table = []
exp_tablo = []
imp_tablo = []
year_to_filter3 = st.slider('choose a year that you want to examinate', 2005, 2021, 2008)
filtered_data3 = df[df['date'].dt.year == year_to_filter3]
filtered_data3cum = pd.DataFrame(filtered_data3)
if len(selectbox_exchange)>0:
    st.write("Here's the data you were looking for :\n", filtered_data3[selectbox_exchange])
for i in range(len(selectbox_exchange)):
    if selectbox_exchange[i] != "date":
        st.markdown(
            f"the total amount of exchange {selectbox_exchange[i]} at year {year_to_filter3} is: {abs(filtered_data3[selectbox_exchange[i]].sum())}")
        filtered_data3cum[f"{selectbox_exchange[i]} Cumulative"] = abs(df[selectbox_exchange[i]]).cumsum()
        table.append(f"{selectbox_exchange[i]} Cumulative")
        for value in table:
            if value.startswith('fr'):
                exp_tablo.append(value)
            elif value.endswith('fr'):
                imp_tablo.append(value)

if ((len(selectbox_exchange) >= 1) and (selectbox_exchange[0] != "date")) or (len(selectbox_exchange) > 1):
    fig = px.line(filtered_data3cum, x=filtered_data3cum['date'], y=table,
                  title=f"Cumulative sum of year {year_to_filter3}")
    fig.update_xaxes(title_text='months')
    fig.update_yaxes(title_text='amount of exchanges')
    st.plotly_chart(fig, use_container_width=True)


countries = ['gb', 'cwe', 'ch', 'it', 'es']
export_values = [filtered_data3cum[f'fr_{country}'].sum() for country in countries]
import_values = [abs(filtered_data3cum[f'{country}_fr'].sum()) for country in countries]

# Create DataFrames for pie charts
df_export = pd.DataFrame({'countries': countries, 'Export': export_values})
df_import = pd.DataFrame({'countries': countries, 'Import': import_values})

st.write("You can choose the year with values you had earlier")
st.header("Here's a pie chart with exports then imports for you to visualize it better:")

# Create a layout with two columns
col1, col2 = st.columns([4, 1])

# Display the export pie chart in the first column
with col1:
    fig_export = px.pie(df_export, names='countries', values='Export', title=f'Exports for {year_to_filter3}')
    st.plotly_chart(fig_export)

# Display the import pie chart in the second column with padding

with col2:
    fig_import = px.pie(df_import, names='countries', values='Import', title=f'Imports for {year_to_filter3}')
    st.plotly_chart(fig_import)

st.write("After playing with this we can notice that the lowest amount of exchanges with France at the beginning "
         "of the dataset is Spain-France with a total amount of 910836 exchanges in 2005 this is due to "
         "their small amount of exchange day by day (around 34). But we also notice that "
         "Italy-France does not have a lot in exchanges too it's mainly due to the fact that they started exchanging"
         " (in the dataset) after almost the second month of 2005.")
st.markdown("At the end, in year 2021 : France imported the most from CWE which is its closest country. In these countries "
            "items have less or even value with those in France. "
            "That way they can make as much money by exporting them to countries where those items are more expensive")
st.markdown("France exports the most in Switzerland, this is due mainly to their proximity and the higher prices "
            "in Switzerland : Selling to a country where your item costs more will make you richer.")