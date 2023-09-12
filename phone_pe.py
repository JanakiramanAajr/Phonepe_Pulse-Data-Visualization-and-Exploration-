import mysql.connector as sql
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px
mydb = sql.connect(host="localhost",
                   user="root",
                   password="",
                   database="phone_pe"
                   )
mycursor = mydb.cursor(buffered=True)
mycursor.execute('''SELECT * FROM top_transaction ORDER BY States''')
df = pd.DataFrame(mycursor.fetchall(), columns=mycursor.column_names)
# st.dataframe(df)
# df = pd.read_csv(f"D:\git_pro\Top_transaction.csv")
# df = df.rename(columns={'distric_name': 'District'}, inplace=True)
mycursor.execute('''SELECT * FROM aggregated_transaction ORDER BY States''')
df1 = pd.DataFrame(mycursor.fetchall(), columns=mycursor.column_names)
mycursor.execute('''SELECT * FROM aggregated_user ORDER BY States''')
df2 = pd.DataFrame(mycursor.fetchall(), columns=mycursor.column_names)
def hi_tran_d_y_tc(df):
    st.write('hello')
    # Filter the DataFrame for Quarters 1, 2, 3, and 4
    filtered_df = df[df['Quarters'].isin([1, 2, 3, 4])]
    # Group by 'States' and sum the 'Transaction_Count'
    sum_by_state = filtered_df.groupby(['District', 'Transaction_Year'])[
        'Transaction_Count'].sum().reset_index()
    # Sort by the sum in descending order and get the top ten states
    top_ten_district_year_tranc_count = sum_by_state.sort_values(by='Transaction_Count', ascending=False).head(10)
    return top_ten_district_year_tranc_count
def hi_tran_d_y_ta(df):
    st.write('hello')
    # Filter the DataFrame for Quarters 1, 2, 3, and 4
    filtered_df = df[df['Quarters'].isin([1, 2, 3, 4])]
    # Group by 'States' and sum the 'Transaction_Count'
    sum_by_state = filtered_df.groupby(['District', 'Transaction_Year'])[
        'Transaction_Amount'].sum().reset_index()
    # Sort by the sum in descending order and get the top ten states
    top_ten_district_year_tranc_amount = sum_by_state.sort_values(by='Transaction_Amount', ascending=False).head(10)
    return (top_ten_district_year_tranc_amount)
def hi_tran_s_y_tc(df):
    st.write('hello')
    # Filter the DataFrame for Quarters 1, 2, 3, and 4
    filtered_df = df[df['Quarters'].isin([1, 2, 3, 4])]
    # Group by 'States' and sum the 'Transaction_Count'
    sum_by_state = filtered_df.groupby(['States', 'Transaction_Year'])[
        'Transaction_Count'].sum().reset_index()
    # Sort by the sum in descending order and get the top ten states
    top_ten_states_year_tranc_count = sum_by_state.sort_values(by='Transaction_Count', ascending=False).head(10)
    return (top_ten_states_year_tranc_count)

def hi_tran_s_y_ta(df):
    st.write('hello')
    # Filter the DataFrame for Quarters 1, 2, 3, and 4
    filtered_df = df[df['Quarters'].isin([1, 2, 3, 4])]
    # Group by 'States' and sum the 'Transaction_Count'
    sum_by_state = filtered_df.groupby(['States', 'Transaction_Year'])[
        'Transaction_Amount'].sum().reset_index()
    # Sort by the sum in descending order and get the top ten states
    top_ten_states_year_tranc_amount = sum_by_state.sort_values(by='Transaction_Amount', ascending=False).head(10)
    return (top_ten_states_year_tranc_amount)

def hi_tran_d_s_tc(df):
    st.write('hello')
    # Filter the DataFrame for Quarters 1, 2, 3, and 4
    filtered_df = df[df['Quarters'].isin([1, 2, 3, 4])]
    # Group by 'States' and sum the 'Transaction_Count'
    sum_by_state = filtered_df.groupby(['District', 'States'])[
        'Transaction_Count'].sum().reset_index()
    # Sort by the sum in descending order and get the top ten states
    top_ten_district_state_tranc_count = sum_by_state.sort_values(by='Transaction_Count', ascending=False).head(10)
    return (top_ten_district_state_tranc_count)

def hi_tran_d_s_ta(df):
    st.write('hello')
    # Filter the DataFrame for Quarters 1, 2, 3, and 4
    filtered_df = df[df['Quarters'].isin([1, 2, 3, 4])]
    # Group by 'States' and sum the 'Transaction_Count'
    sum_by_state = filtered_df.groupby(['District', 'States'])[
        'Transaction_Amount'].sum().reset_index()
    # Sort by the sum in descending order and get the top ten states
    top_ten_district_state_tranc_amount = sum_by_state.sort_values(by='Transaction_Amount', ascending=False).head(10)
    return (top_ten_district_state_tranc_amount)
def hi_tran_s_tc_ta(df):
    st.write('hello')
    # Filter the DataFrame for Quarters 1, 2, 3, and 4
    filtered_df = df[df['Quarters'].isin([1, 2, 3, 4])]
    # Group by 'States' and sum the 'Transaction_Count'
    sum_by_state = filtered_df.groupby(['States', 'Transaction_Count'])[
        'Transaction_Amount'].sum().reset_index()
    # Sort by the sum in descending order and get the top ten states
    top_ten_state_tranc_count_tranc_amount = sum_by_state.sort_values(by='Transaction_Amount', ascending=False).head(10)
    return (top_ten_state_tranc_count_tranc_amount)

def hi_tran_d_tc_ta(df):
    st.write('hello')
    # Filter the DataFrame for Quarters 1, 2, 3, and 4
    filtered_df = df[df['Quarters'].isin([1, 2, 3, 4])]
    # Group by 'States' and sum the 'Transaction_Count'
    sum_by_state = filtered_df.groupby(['District', 'Transaction_Count'])[
        'Transaction_Amount'].sum().reset_index()
    # Sort by the sum in descending order and get the top ten states
    top_ten_district_tranc_count_tranc_amount = sum_by_state.sort_values(by='Transaction_Amount', ascending=False).head(10)
    return (top_ten_district_tranc_count_tranc_amount)


st.set_page_config(page_title= "Phonepe Pulse Data Visualization ",
                   page_icon= Image.open(r"D:\git_pro\phone_pe_logo.png") ,
                   layout= "wide",
                   initial_sidebar_state= "expanded")

selected = option_menu(None, ["Home","Top Charts","Explore Data","About"],
    icons=["house","graph-up-arrow","bar-chart-line", "exclamation-circle"],
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected == 'Home':
    # Open the image
    image = Image.open(r"D:\git_pro\phone_pe_logo.png")

    # Resize the image to the desired dimensions
    new_width = 300 # Set your desired width
    new_height = 200  # Set your desired height
    resized_image = image.resize((new_width, new_height))
    # Display the resized image
    st.image(resized_image,caption="PhonePe")
    st.download_button(":blue[DOWNLOAD THE APP NOW]", "https://www.phonepe.com/app-download/")
    st.title('Phonepe Pulse Data Visualization')

    # st.write(df.columns)
if selected == "Top Charts":
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 \
        = st.tabs(["click1", "click2", "click3", "click4", "click5", "click6", "click7", "click8", "click9,10"])
    with tab1:
        st.header('Top 10 District and transaction count belongs to Year')
        top_ten_district_year_tranc_count = hi_tran_d_y_tc(df)
        st.dataframe(top_ten_district_year_tranc_count)
        a = top_ten_district_year_tranc_count
        st.title("Top 10 District and transaction count belongs to Year")
        st.plotly_chart(px.bar(a, x="Transaction_Count", y="District", color="Transaction_Year",
                     title="Stacked Bar Chart by Transaction Year"))
        # st.bar_chart(data = a, y= "Transaction_Count", x="District")

    with tab2:
        st.header('Top 10 District and amount of transaction belongs to year')
        top_ten_district_year_tranc_amount = hi_tran_d_y_ta(df)
        st.dataframe(top_ten_district_year_tranc_amount)
        b = top_ten_district_year_tranc_amount
        st.title("Top 10 District and amount of transaction belongs to year")
        st.plotly_chart(px.bar(b, x="Transaction_Amount", y="District", color="Transaction_Year",
                               title="Stacked Bar Chart by Transaction Year"))
        # st.bar_chart(data=b, y="Transaction_Amount", x="District")
    with tab3:
        st.header('Top 10 States and transation count belongs to year')
        top_ten_state_year_tranc_count = hi_tran_s_y_tc(df)
        st.dataframe(top_ten_state_year_tranc_count)
        c=top_ten_state_year_tranc_count
        st.title("Top 10 States and transation count belongs to year")
        st.plotly_chart(px.bar(c, x="Transaction_Count", y="States", color="Transaction_Year",
                               title="Stacked Bar Chart by Transaction Year"))
        # st.bar_chart(data=c, y="Transaction_Count", x="States")
    with tab4:
        st.header('Top 10 States and amount of transaction belongs to year')
        top_ten_state_year_tranc_amount = hi_tran_s_y_ta(df)
        st.dataframe(top_ten_state_year_tranc_amount)
        d = top_ten_state_year_tranc_amount
        st.title("Top 10 States and amount of transaction belongs to year")
        st.plotly_chart(px.bar(d, x="Transaction_Amount", y="States", color="Transaction_Year",
                               title="Stacked Bar Chart by Transaction Year"))
        # st.bar_chart(data=d, y="Transaction_Amount", x="States")
    with tab5:
        st.header('Top 10 District and transaction count belongs to States')
        top_ten_district_state_tranc_count = hi_tran_d_s_tc(df)
        st.dataframe(top_ten_district_state_tranc_count)
        e = top_ten_district_state_tranc_count
        st.title("Top 10 District and transaction count belongs to States")
        st.plotly_chart(px.bar(e, x="Transaction_Count", y="District", color="States",
                               title="Stacked Bar Chart by States"))
        # st.bar_chart(data=d, y="Transaction_Count", x="District")
    with tab6:
        st.header('Top 10 District and amount of transaction belongs to year')
        top_ten_district_state_tranc_amount = hi_tran_d_s_ta(df)
        st.dataframe(top_ten_district_state_tranc_amount)
        f = top_ten_district_state_tranc_amount
        st.title("Top 10 District and amount of transaction belongs to year")
        st.plotly_chart(px.bar(f, x="Transaction_Amount", y="District", color="States",
                               title="Stacked Bar Chart by States"))
        # st.bar_chart(data=e, y="Transaction_Amount", x="District")
    with tab7:
        st.header('Top 10 States and amount of transaction belongs to transaction count')
        top_ten_state_tranc_count_tranc_amount = hi_tran_s_tc_ta(df)
        st.dataframe(top_ten_state_tranc_count_tranc_amount)
        g = top_ten_state_tranc_count_tranc_amount
        st.title("Top 10 States and amount of transaction belongs to transaction count")
        st.plotly_chart(px.bar(g, x="Transaction_Amount", y="States", color="Transaction_Count",
                               title="Stacked Bar Chart by Transaction Count"))
        # st.bar_chart(data=f, y="Transaction_Amount", x="States")
    with tab8:
        st.header('Top 10 District and amount of transaction belongs to transaction count')
        top_ten_district_tranc_count_tranc_amount = hi_tran_d_tc_ta(df)
        st.dataframe(top_ten_district_tranc_count_tranc_amount)
        h = top_ten_district_tranc_count_tranc_amount
        st.title("Top 10 District and amount of transaction belongs to transaction count")
        st.plotly_chart(px.bar(h, x="Transaction_Count", y="District", color="Transaction_Count",
                               title="Stacked Bar Chart by Transaction Count"))
        # st.bar_chart(data=g, y="Transaction_Amount", x="District")
    with tab9:
        list_states = sorted(list(set(df['States'])))
        select_1 = st.header('Select State Name')
        option = st.selectbox('',list_states)
        # target_state = 'west-bengal'
        st.header('Maximum Transaction Count of District for particular State belongs to year')

        # Filter the DataFrame for the specified state
        state_df1 = df[df['States'] == option]

        # Group by 'distric_name' and sum the 'Transaction_Count'
        sum_by_district1 = state_df1.groupby('District')['Transaction_Count'].sum().reset_index()

        # Sort by the sum in descending order and get the top district
        top_district1 = sum_by_district1.sort_values(by='Transaction_Count', ascending=False).iloc[:]

        top_district1


        # target_state = 'west-bengal'
        st.header('Maximum Transaction amount of District for particular State belongs to year')

        # Filter the DataFrame for the specified state
        state_df = df[df['States'] == option]

        # Group by 'distric_name' and sum the 'Transaction_Count'
        sum_by_district = state_df.groupby('District')['Transaction_Amount'].sum().reset_index()

        # Sort by the sum in descending order and get the top district
        top_district2 = sum_by_district.sort_values(by='Transaction_Amount', ascending=False).iloc[:]

        top_district2

if selected == "Explore Data":
    s = df1['States']
    a = []
    for i in s:
        j = (i.replace('-', ' ')).title()
        a.append(j)
    df1['States'] = a
    s1 = df2['States']
    a1 = []
    for i in s1:
        j = (i.replace('-', ' ')).title()
        a1.append(j)
    df2['States'] = a1

    tab1, tab2 = st.tabs(["Transaction", "Users"])
    with tab1:
        st.write('Total Transaction Amount:',(sum(df1['Transaction_Amount'])))
        st.write('Total Transaction Count:',(sum(df1['Transaction_Count'])))

        # Choropleth map
        fig = px.choropleth(
        df1,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='States',  # Column in DataFrame
        animation_frame='Transaction_Year',  # DataFrame column for animation
        color='Transaction_Amount', # DataFrame column for coloring
        color_continuous_scale='Inferno',
        title='Rape cases across the states',
        height=1000,
        width=2000
        )
        st.plotly_chart(fig.update_geos(fitbounds="locations", visible=False))
    with tab2:
        st.write('Total Register Users:', (sum(df2['Register_users'])))
        st.write('Total App Opens:', (sum(df2['App_opens'])))
        fig = px.choropleth(
            df2,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',  # Column in DataFrame
            animation_frame='Transaction_Year',  # DataFrame column for animation
            color='Register_users',  # DataFrame column for coloring
            color_continuous_scale='Inferno',
            title='Rape cases across the states',
            height=1000,
            width=2000
        )
        st.plotly_chart(fig.update_geos(fitbounds="locations", visible=False))
if selected == "About":
    col1, col2 = st.columns([3, 3], gap="medium")
    with col1:
        st.write(" ")
        st.write(" ")
        st.markdown("### :violet[About PhonePe Pulse:] ")
        st.write(
            "##### BENGALURU, India, On Sept. 3, 2021 PhonePe, India's leading fintech platform, announced the launch of PhonePe Pulse, India's first interactive website with data, insights and trends on digital payments in the country. The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers on an interactive map of India. With  over 45% market share, PhonePe's data is representative of the country's digital payment habits.")

        st.write(
            "##### The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews. The report is available as a free download on the PhonePe Pulse website and GitHub.")

        st.markdown("### :violet[About PhonePe:] ")
        st.write(
            "##### PhonePe is India's leading fintech platform with over 300 million registered users. Using PhonePe, users can send and receive money, recharge mobile, DTH, pay at stores, make utility payments, buy gold and make investments. PhonePe forayed into financial services in 2017 with the launch of Gold providing users with a safe and convenient option to buy 24-karat gold securely on its platform. PhonePe has since launched several Mutual Funds and Insurance products like tax-saving funds, liquid funds, international travel insurance and Corona Care, a dedicated insurance product for the COVID-19 pandemic among others. PhonePe also launched its Switch platform in 2018, and today its customers can place orders on over 600 apps directly from within the PhonePe mobile app. PhonePe is accepted at 20+ million merchant outlets across Bharat")

        st.write("**:violet[My Project GitHub link]** ⬇️")
        st.write("https://github.com/JanakiramanAajr/Phonepe_Pulse-Data-Visualization-and-Exploration-.git")
    with col2:
        st.write('-------------------')
        st.write('---- Thank You----')