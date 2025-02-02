import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.sidebar.header('EDA: Pima diabetes') 
st.sidebar.subheader('Visualization using seaborn and plotly')

# Get the data
df = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/diabetes.csv")
df['Outcome'] = df['Outcome'].apply(lambda x: 'DM' if x == 1 else 'noDM')

classes=df.Outcome
noDB,DB=classes.value_counts()
st.sidebar.write('non-diabetes(noDM):',noDB)
st.sidebar.write('diabetes(DM):',DB)
# st.sidebar.write('***')
fig0 = plt.figure(figsize=(4,3))
sns.countplot(classes, label='count', palette=dict(noDM = 'g', DM = 'r'))
st.sidebar.write(fig0)

st.subheader(f'Data Information: shape = {df.shape}')
st.write(f'##### features = {list(df.columns)[:-1]}')
st.write(f'##### classes = {pd.unique(classes)}')
st.write('***')
# Show the data as a table (you can also use st.write(df))
st.dataframe(df)
# Get statistics on the data
# st.write(df.describe())
    
# histogram with plotly
st.header("Histogram")
## multi-column layput
row0_1, row0_space2, row0_2 = st.beta_columns(
    (1, .1, 1))

with row0_1: 
    hist_x = st.selectbox("Select a feature", options=df.columns, index=df.columns.get_loc("Pregnancies"))
        
with row0_2: 
    bar_mode = st.selectbox("Select barmode", ["relative", "group"], 0)

hist_bins = st.slider(label="Histogram bins", min_value=5, max_value=50, value=25, step=1, key='h1')
# hist_cats = df['Outcome'].sort_values().unique()
hist_cats = df[hist_x].sort_values().unique()
hist_fig1 = px.histogram(df, x=hist_x, nbins=hist_bins, 
                         title="Histogram of " + hist_x,
                         template="plotly_white", 
                         color='Outcome', 
                         barmode=bar_mode, 
                         color_discrete_map=dict(noDM = 'green', DM = 'red'),  
                         category_orders={hist_x: hist_cats}) 
st.write(hist_fig1)


# boxplots
st.header("Boxplot")
st.subheader("With a categorical variable - Outcome [noDM, DM]")
## multi-column layput
row1_1, row1_space2, row1_2 = st.beta_columns(
    (1, .1, 1))

with row1_1: 
    box_x = st.selectbox("Boxplot variable", options=df.columns, index=df.columns.get_loc("Age"))
        
with row1_2: 
    box_cat = st.selectbox("Categorical variable", ["Outcome"], 0)

st.write("Hint - try comparison w.r.t Catagories")
box_fig = px.box(df, x=box_cat, y=box_x, title="Box plot of " + box_x, color='Outcome', 
                        color_discrete_map=dict(noDM = 'green', DM = 'red'), 
                        template="plotly_white") 
st.write(box_fig)

# Correlations
## multi-column layout
st.header("Correlations")
row2_1, row2_space2, row2_2 = st.beta_columns((1, .1, 1))

with row2_1: 
    corr_x = st.selectbox("Correlation - X variable", options=df.columns, index=df.columns.get_loc("Age"))
        
with row2_2: 
    corr_y = st.selectbox("Correlation - Y variable", options=df.columns, index=df.columns.get_loc("Pregnancies"))

corr2_fig = px.scatter(df, x=corr_x, y=corr_y, 
                            color='Outcome', 
                            color_discrete_map=dict(noDM = 'green', DM = 'red'), 
                            template="plotly_white")
st.write(corr2_fig)

# heatmap
st.subheader('Heatmap of correlation')
fig4 = plt.figure(figsize=(6,5))
sns.heatmap(df.corr(),annot=True, vmin=-1, vmax=1, cmap='coolwarm')
st.pyplot(fig4)
# st.write(fig4)

# correlation heatmap
st.subheader('Heatmap of selected parameters')
fig5 = plt.figure(figsize=(5,4))
hmap_params = st.multiselect("Select parameters to include on heatmap", options=list(df.columns), default=[p for p in df.columns if "Outcome" not in p])
sns.heatmap(df[hmap_params].corr(), annot=True, vmin=-1, vmax=1, cmap='coolwarm')
st.pyplot(fig5)

