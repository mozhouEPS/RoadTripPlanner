import streamlit as st
from usstates import usa_map, state_info
from bfs import bfs_path

st.title("🗺️ Road Trip Planner - BFS Shortest Route with Must-Visit States")
st.write("Plan your road trip and include must-visit states in order!")

states = sorted(list(usa_map.keys()))
start_default = states.index("Washington")
end_default = states.index("Florida")

start_state = st.selectbox("Start State", states, index=start_default)
end_state = st.selectbox("Destination State", states, index=end_default)

# Multi-select for must-visit states
must_visit = st.multiselect(
    "⭐ Select Must-Visit States (in order)",
    options=[s for s in states if s not in [start_state, end_state]],
)

if st.button("Find Route"):
    if start_state == end_state:
        st.warning("Start and destination states are the same!")
    else:
        # Build full path by connecting segments
        full_path = []
        waypoints = [start_state] + must_visit + [end_state]

        for i in range(len(waypoints) - 1):
            segment = bfs_path(usa_map, waypoints[i], waypoints[i + 1])
            if segment is None:
                st.error(f"No path found between {waypoints[i]} and {waypoints[i+1]}.")
                full_path = None
                break
            if i > 0:
                # Avoid repeating the connecting state
                segment = segment[1:]
            full_path.extend(segment)

        if full_path:
            st.success("✅ Full route including must-visit states found!")
            st.write(" → ".join(full_path))
            
            # --- Route Summary ---
            st.subheader("📍 Route Summary")
            st.write(f"**Start:** {start_state}")
            st.write(f"**End:** {end_state}")
            if must_visit:
                st.write(f"**Must-Visit Stops (in order):** {', '.join(must_visit)}")
            st.write(f"**Total states visited:** {len(full_path)}")

            # --- Learn about states ---
            total_drive_time = 0
            st.subheader("🔎 Learn About Each State")
            for state in full_path:
                with st.expander(state):
                    info = state_info.get(state)
                    if info:
                        st.write(f"**Fun Fact:** {info['fun_fact']}")
                        st.write("**Things to Do:**")
                        for act in info["things_to_do"]:
                            st.write(f"• {act}")
                        st.write(f"**Estimated drive time to next state:** {info['drive_time']} hrs")
                        total_drive_time += info['drive_time']
                    else:
                        st.write("No additional info available.")

            st.subheader("🧭 Route Insights")
            st.write(f"Estimated total driving time: **{total_drive_time} hours**")
