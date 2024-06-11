import streamlit as st
import time
from src.rags import graphrag, raptor, sql_data_chain

st.set_page_config(layout="wide")
st.title("RAG Evaluator Application")

# Initialize session state keys
if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""
if "sdc_response" not in st.session_state:
    st.session_state["sdc_response"] = ""
if "raptor_response" not in st.session_state:
    st.session_state["raptor_response"] = ""
if "graphrag_response" not in st.session_state:
    st.session_state["graphrag_response"] = ""
if "sdc_time" not in st.session_state:
    st.session_state["sdc_time"] = 0
if "raptor_time" not in st.session_state:
    st.session_state["raptor_time"] = 0
if "graphrag_time" not in st.session_state:
    st.session_state["graphrag_time"] = 0

def get_sdc_response(input_text):
    start_time = time.time()
    response = sql_data_chain.technique_1(input_text)
    end_time = time.time()
    st.session_state["sdc_response"] = response
    st.session_state["sdc_time"] = end_time - start_time

def get_raptor_response(input_text):
    start_time = time.time()
    response = raptor.technique_2(input_text)
    end_time = time.time()
    st.session_state["raptor_response"] = response
    st.session_state["raptor_time"] = end_time - start_time

def get_graphrag_response(input_text):
    start_time = time.time()
    response = graphrag.technique_3(input_text)
    end_time = time.time()
    st.session_state["graphrag_response"] = response
    st.session_state["graphrag_time"] = end_time - start_time

def compare_responses():
    input_text = st.session_state["input_text"]
    if input_text:
        get_sdc_response(input_text)
        get_raptor_response(input_text)
        get_graphrag_response(input_text)
    else:
        st.session_state["sdc_response"] = "Please enter some text to compare."
        st.session_state["raptor_response"] = ""
        st.session_state["graphrag_response"] = ""
        st.session_state["sdc_time"] = 0
        st.session_state["raptor_time"] = 0
        st.session_state["graphrag_time"] = 0

input_text = st.text_area("Enter your input text:", key="input_text", on_change=compare_responses, height=100)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.write("### SQL Query Chain Response:")
    st.write(f"Time taken: {st.session_state['sdc_time']:.2f} seconds")
    st.text_area("", value=st.session_state.get("sdc_response", ""), height=400, key="sdc_response_display")

with col2:
    st.write("### RAPTOR Response:")
    st.write(f"Time taken: {st.session_state['raptor_time']:.2f} seconds")
    st.text_area("", value=st.session_state.get("raptor_response", ""), height=400, key="raptor_response_display")

with col3:
    st.write("### GraphRAG Response")
    st.write(f"Time taken: {st.session_state['graphrag_time']:.2f} seconds")
    st.text_area("", value=st.session_state.get("graphrag_response", ""), height=400, key="graphrag_response_display")
