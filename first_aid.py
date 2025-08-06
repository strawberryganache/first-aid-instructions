# import streamlit as st
# import json

# # Load the first aid data
# with open("first_aid_data.json", "r") as f:
#     data = json.load(f)

# st.set_page_config(page_title="First Aid Instruction App", layout="centered")

# st.title("🩹 First Aid Instruction App")
# st.markdown("Quickly find first aid instructions for common emergencies.")

# # Get all topics organized by category
# all_topics = {
#     category: list(topics.keys())
#     for category, topics in data.items()
# }

# # Sidebar: Choose a category
# selected_category = st.sidebar.selectbox("📂 Select a category", list(all_topics.keys()))

# # Show dropdown of topics in the selected category
# selected_topic = st.selectbox(
#     f"🔍 Topics in {selected_category}",
#     all_topics[selected_category]
# )

# # Display the instructions
# if selected_topic:
#     st.subheader(f"🩺 {selected_topic}")
#     st.write(data[selected_category][selected_topic])

import streamlit as st
import json

# Load data
with open("first_aid_data.json", "r") as f:
    data = json.load(f)

st.set_page_config(page_title="First Aid Instruction App", layout="centered")

st.title("🩹 First Aid Instruction App")
st.markdown("Quickly search or browse for first aid instructions for common emergencies.")

# 🔍 Search bar
search_query = st.text_input("🔍 Search for a condition or keyword (e.g. burn, bleeding, CPR)")

results = []

# Search through all categories and topics
if search_query:
    query = search_query.lower()
    for category, topics in data.items():
        for topic, instruction in topics.items():
            if query in topic.lower() or query in instruction.lower():
                results.append((category, topic, instruction))

    if results:
        st.subheader(f"🔎 {len(results)} result(s) found:")
        for category, topic, instruction in results:
            st.markdown(f"### 🗂️ {topic} ({category})")
            st.write(instruction)
            st.markdown("---")
    else:
        st.warning("No matches found. Try another keyword.")
else:
    # Default view: Category dropdown
    selected_category = st.sidebar.selectbox("📂 Browse by category", list(data.keys()))
    selected_topic = st.selectbox("📋 Topics in " + selected_category, list(data[selected_category].keys()))

    if selected_topic:
        st.subheader(f"🩺 {selected_topic}")
        st.write(data[selected_category][selected_topic])

