import matplotlib.pyplot as plt
import os
import pandas as pd
import streamlit as st

from PIL import Image


st.beta_set_page_config(
    page_title="Network Analysis of TV Sitcoms",
    layout="wide",
    initial_sidebar_state="expanded",
)

cwd = os.getcwd()


genre = st.sidebar.radio(
    "Network Analysis of TV Sitcoms",
    ('Objective', 'Friends', 'The Office'))


if genre == 'Objective':
    st.header('Network Analysis of TV Sitcoms')
    
    col1, col2 = st.beta_columns(2)
    
    image = Image.open('{}/images/friends/friends_main.webp'.format(cwd))
    col1.image(image, width=450, height=400)
    
    image = Image.open('{}/images/the_office/the office_main.jpg'.format(cwd))
    col2.image(image, width=400, height=300)
    
elif genre == 'Friends':    
    friend_details = st.selectbox(
        '',
        ['Details', 'Dataset', 'Data Cleaning', 'EDA'])
    
    if friend_details == 'Details':
        st.write(' <iframe width="800" height="350" src="https://www.youtube.com/embed/sLisEEwYZvw"></iframe>', unsafe_allow_html=True)

        st.write('<br><br><p><b>F.R.I.E.N.D.S</b> is an American television sitcom, created by David Crane and Marta Kauffman, which aired on NBC <br> from September 22, 1994, to May 6, 2004, lasting ten seasons.</p>', unsafe_allow_html=True)

        st.write('<b>Main Cast and Characters</b>',unsafe_allow_html=True)

        col1, col2, col3, col4, col5, col6 = st.beta_columns(6)
        image = Image.open('{}/images/friends/rachel_green.jpg'.format(cwd))
        col1.image(image, width=175, caption='Jennifer Aniston as Rachel Green')
        image = Image.open('{}/images/friends/monica_geller.jpg'.format(cwd))
        col2.image(image, width=175, caption='Courteney Cox as Monica Geller')
        image = Image.open('{}/images/friends/phoebe_buffay.png'.format(cwd))
        col3.image(image, width=175, caption='Lisa Kudrow as Phoebe Buffay')


        col1, col2, col3, col4, col5, col6 = st.beta_columns(6)
        image = Image.open('{}/images/friends/joey_tribbiani.jpg'.format(cwd))
        col1.image(image, width=175, caption='Matt LeBlanc as Joey Tribbiani')
        image = Image.open('{}/images/friends/chandler_bing.png'.format(cwd))
        col2.image(image, width=175, caption='Matthew Perry as Chandler Bing')
        image = Image.open('{}/images/friends/ross_geller.jpg'.format(cwd))
        col3.image(image, width=175, caption='David Schwimmer as Ross Geller')
        
    elif friend_details == 'Dataset':
        friends_lines = pd.read_csv('dataset/friends/friends_lines.csv')
        friends_speaker_combinations = pd.read_csv('dataset/friends/friends_speaker_combinations_per_episode.csv')
        friends_speaker_pair_interaction = pd.read_csv('dataset/friends/friends_speaker_pair_interaction_factors.csv')
        
        st.write('First Dataset: Friends Lines')
        st.table(friends_lines.head(5))
        
        st.write('Second Dataset: Friends Speaker Combinations')
        st.table(friends_speaker_combinations.head(5))
        
        st.write('Thirds Dataset: Friends Speaker Pair Interaction')
        st.table(friends_speaker_pair_interaction.head(5))
        
    elif friend_details == 'EDA':
        friends_lines = pd.read_csv('dataset/friends/friends_lines.csv')
        total_lines = len(friends_lines)
        col1, col2 = st.beta_columns(2)
        
        ls_df = friends_lines.groupby(['speaker'])[['line_text']].count().reset_index()
        ls_df = ls_df.rename(columns={'line_text': 'num_lines'})
        ls_df['lineshare'] = ls_df['num_lines']/total_lines
        ls_df = ls_df.sort_values("lineshare", ascending=False)
        
        fig = plt.figure(figsize=(5,4))
        fig.set_size_inches(6.7, 4.27)
        data = ls_df.head(10)
        plt.bar(data['speaker'],data['lineshare'])

        plt.xticks(rotation=90)
        plt.title("Friends Characters Lineshare")
        col1.pyplot(fig)
        
        friends_speaker_combinations = pd.read_csv('dataset/friends/friends_speaker_combinations_per_episode.csv')
        friends_speaker_pair_interaction = pd.read_csv('dataset/friends/friends_speaker_pair_interaction_factors.csv')
        
        data = friends_speaker_pair_interaction.groupby(['speaker1','speaker2'])['interaction_factor'].sum().reset_index(name='total_interaction_factor')
        fig, ax1 = plt.subplots()
        fig.set_size_inches(6.7, 4.27)
        ax1.set(title='Total Interaction Factor')
        ax1.hist(data['total_interaction_factor'])
        col2.pyplot(fig)