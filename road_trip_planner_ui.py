import streamlit as st
from collections import deque

# ----- Graph of US States -----
usa_map = {
    "Alabama": ["Florida", "Georgia", "Tennessee", "Mississippi"],
    "Alaska": [],
    "Arizona": ["California", "Nevada", "Utah", "Colorado", "New Mexico"],
    "Arkansas": ["Louisiana", "Mississippi", "Tennessee", "Missouri", "Oklahoma", "Texas"],
    "California": ["Oregon", "Nevada", "Arizona"],
    "Colorado": ["Wyoming", "Nebraska", "Kansas", "Oklahoma", "New Mexico", "Arizona", "Utah"],
    "Connecticut": ["New York", "Massachusetts", "Rhode Island"],
    "Delaware": ["Maryland", "Pennsylvania", "New Jersey"],
    "Florida": ["Alabama", "Georgia"],
    "Georgia": ["Florida", "Alabama", "Tennessee", "North Carolina", "South Carolina"],
    "Hawaii": [],
    "Idaho": ["Washington", "Oregon", "Nevada", "Utah", "Wyoming", "Montana"],
    "Illinois": ["Wisconsin", "Iowa", "Missouri", "Kentucky", "Indiana"],
    "Indiana": ["Illinois", "Kentucky", "Ohio", "Michigan"],
    "Iowa": ["Minnesota", "Wisconsin", "Illinois", "Missouri", "Nebraska", "South Dakota"],
    "Kansas": ["Nebraska", "Missouri", "Oklahoma", "Colorado"],
    "Kentucky": ["Illinois", "Indiana", "Ohio", "West Virginia", "Virginia", "Tennessee", "Missouri"],
    "Louisiana": ["Arkansas", "Mississippi", "Texas"],
    "Maine": ["New Hampshire"],
    "Maryland": ["Delaware", "Pennsylvania", "Virginia", "West Virginia"],
    "Massachusetts": ["Connecticut", "New York", "New Hampshire", "Rhode Island", "Vermont"],
    "Michigan": ["Indiana", "Ohio", "Wisconsin", "Minnesota"],
    "Minnesota": ["North Dakota", "South Dakota", "Iowa", "Wisconsin", "Michigan"],
    "Mississippi": ["Alabama", "Arkansas", "Tennessee", "Louisiana"],
    "Missouri": ["Iowa", "Illinois", "Kentucky", "Tennessee", "Arkansas", "Oklahoma", "Kansas", "Nebraska"],
    "Montana": ["Idaho", "Wyoming", "South Dakota", "North Dakota"],
    "Nebraska": ["Colorado", "Iowa", "Kansas", "Missouri", "South Dakota", "Wyoming"],
    "Nevada": ["Idaho", "Utah", "Arizona", "California", "Oregon"],
    "New Hampshire": ["Maine", "Massachusetts", "Vermont"],
    "New Jersey": ["Delaware", "Pennsylvania", "New York"],
    "New Mexico": ["Arizona", "Utah", "Colorado", "Oklahoma", "Texas"],
    "New York": ["Connecticut", "Massachusetts", "Vermont", "New Jersey", "Pennsylvania", "Rhode Island"],
    "North Carolina": ["Virginia", "Tennessee", "Georgia", "South Carolina"],
    "North Dakota": ["Minnesota", "South Dakota", "Montana"],
    "Ohio": ["Pennsylvania", "West Virginia", "Kentucky", "Indiana", "Michigan"],
    "Oklahoma": ["Kansas", "Missouri", "Arkansas", "Texas", "New Mexico", "Colorado"],
    "Oregon": ["California", "Nevada", "Idaho", "Washington"],
    "Pennsylvania": ["New York", "New Jersey", "Delaware", "Maryland", "West Virginia", "Ohio"],
    "Rhode Island": ["Connecticut", "Massachusetts"],
    "South Carolina": ["Georgia", "North Carolina"],
    "South Dakota": ["North Dakota", "Minnesota", "Iowa", "Nebraska", "Wyoming", "Montana"],
    "Tennessee": ["Kentucky", "Virginia", "North Carolina", "Georgia", "Alabama", "Mississippi", "Arkansas", "Missouri"],
    "Texas": ["New Mexico", "Oklahoma", "Arkansas", "Louisiana"],
    "Utah": ["Idaho", "Wyoming", "Colorado", "New Mexico", "Arizona", "Nevada"],
    "Vermont": ["New York", "New Hampshire", "Massachusetts"],
    "Virginia": ["Kentucky", "West Virginia", "Maryland", "North Carolina", "Tennessee"],
    "Washington": ["Idaho", "Oregon"],
    "West Virginia": ["Ohio", "Pennsylvania", "Maryland", "Virginia", "Kentucky"],
    "Wisconsin": ["Minnesota", "Iowa", "Illinois", "Michigan"],
    "Wyoming": ["Montana", "South Dakota", "Nebraska", "Colorado", "Utah", "Idaho"]
}

from collections import deque
# ----- BFS Function -----
def bfs_path(graph, start, goal):
    queue = deque([start])
    visited = set()
    parent = {}

    while queue:
        current = queue.popleft()
        visited.add(current)

        if current == goal:
            # reconstruct path
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = current
    return None

# ----- Streamlit UI -----
st.title("🗺️ Road Trip Planner - BFS Shortest Route")
st.write("Select your starting state and destination state:")

states = sorted(list(usa_map.keys()))
start_state = st.selectbox("Start State", states)
end_state = st.selectbox("Destination State", states)


if st.button("Find Shortest Route"):
    if start_state == end_state:
        st.warning("Start and destination states are the same!")
    else:
        path = bfs_path(usa_map, start_state, end_state)
        if path:
            st.success("Shortest path found!")
            st.write(" -> ".join(path))
        else:
            st.error("No path found between these states.")

