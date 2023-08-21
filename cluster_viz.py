import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# BOXPLOT une feature numerique d'un dataframe en fonction d'un label
def boxplot_numfeature(df, feature, label, viz_outliers = False, titre = "") :
    ordre = df.groupby(label)[feature].median().sort_values().index
    plt.figure(figsize = (10, 10))
    sns.boxplot(data=df, x=feature, y=label, showfliers = viz_outliers, orient = 'h', order=ordre)
    if titre != "" :
        plt.title(titre)
    plt.show()
    return


def radar_2_a_2(df, categories, label_var, value1, value2, legend_val1, legend_val2) :
    ref_cluster =  2
    tmp_cat1 = df[df[label_var] == value1].drop(columns=[label_var])
    tmp_cat2 = df[df[label_var] == value2].drop(columns=[label_var])

    tmp_cat1_means = tmp_cat1.mean().reset_index()
    tmp_cat2_means = tmp_cat2.mean().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=tmp_cat1_means[0],
        theta=categories,
        fill='toself',
        name=legend_val1
    ))

    fig.add_trace(go.Scatterpolar(
        r=tmp_cat2_means[0],
        theta=categories,
        fill='toself',
        name=legend_val2
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 5]
        ),
    ),
    showlegend=True
    )

    fig.show()
    return