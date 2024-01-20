import streamlit as st 
import pandas as pd 
import requests 
from typing import List, Optional
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import deque
import networkx as nx
import re
import os 
import matplotlib.pyplot as plt
import visualize


def load_data(data):
    return pd.read_csv(data)


def fetch_links(url:str)-> List:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

     

def bfs_traversal(start_url:str, num_layers:int, graph:nx.Graph):
    visited = set()
    queue = deque([(start_url, 0)])
    
    while queue:
        url, layer = queue.popleft()
        if layer > num_layers:
            break
        if url not in visited:
            visited.add(url)
            connections = fetch_links(url)
            for x in connections:
                graph.add_edge(url, x)
                queue.append((x, layer + 1))


def convert_graph_to_df(my_graph):
     df = nx.to_pandas_edgelist(my_graph,source="source",target="target")
     return df 


def extract_domain_from_url(url):
    pattern = r'https?://(?:www\.)?([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None
    
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')



# def plot_network(my_graph):
#     pos = nx.spring_layout(my_graph, iterations=20)
#     vis = visualize.GraphVisualization(my_graph,pos,node_size=4, node_border_width=1, edge_width=0.5,node_color="blue")
#     fig = vis.create_figure(height=800, width=800, showlabel=False)
#     st.plotly_chart(fig,use_container_with=True)


def plot_network(my_graph, **kwargs):
    # Set default values for keyword arguments
    default_kwargs = {
        'node_size': 10,
        'node_border_width': 1,
        'edge_width': 0.5,
        'node_color': "blue",
    }
    # Update default_kwargs with the provided kwargs
    default_kwargs.update(kwargs)

    pos = nx.spring_layout(my_graph, iterations=20)
    vis = visualize.GraphVisualization(my_graph, pos, **default_kwargs)
    fig = vis.create_figure(height=800, width=800, showlabel=False)
    # SAVE
    # fig.write_html(filename)
    st.plotly_chart(fig, use_container_width=True)

# Global networkx Graph
graph = nx.Graph()

def main():
    menu = ["home", "archive", "about"]
    st.title("Scan the Web App")

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "home":
        with st.form("search_form"):
             search_url = st.text_input("Enter URL here")
             submit_btn = st.form_submit_button("Traverse")

        if submit_btn:
             st.write("Searching for:", search_url)
             link_list = fetch_links(search_url)
             
             with st.expander("List Links"):
                  st.write(link_list)
                  
             with st.expander("Plot"):
                  with st.spinner():
                       bfs_traversal(search_url,1,graph)
                       st.success("Traversing Done")
                  site_df = convert_graph_to_df(graph)
                  filename = f"{extract_domain_from_url(search_url)}.csv"
                  site_df.to_csv(os.path.join("data",filename))
                  st.toast(f"Saved file as {filename}")
                  # downloadable
                  data_csv = convert_df(site_df)
                  st.download_button(label="Download data as CSV",
                                     data=data_csv,file_name=filename,
                                     mime='text/csv')

                  st.dataframe(site_df)

                  # Plot
                #   fig, ax = plt.subplot(figsize=(20,10))
                #   nx.draw_networkx(graph,ax=ax)
                #   st.pyplot(fig)

                # convert pandas to network x graph
                  site_graph = nx.from_pandas_edgelist(site_df)
                  plot_network(site_graph)







            

    elif choice == "archive":
        filenames = os.listdir("data")
        selected_filename = st.selectbox("Select a file", filenames)
        full_file_path = os.path.join("data", selected_filename)

        site_df = load_data(full_file_path)
        site_graph = nx.from_pandas_edgelist(site_df)
        with st.expander("Preview Dataset"):
            st.dataframe(site_df)

        plot_network(site_graph)


    else:
        st.subheader("About")




if __name__ == '__main__':
	main()