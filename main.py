import streamlit as st
from query_processor import QueryProcessor
from response_generator import ResponseGenerator
import time

# Initialize our components
query_processor = QueryProcessor()
response_generator = ResponseGenerator()

# Streamlit page config
st.set_page_config(
    page_title="Data 8 Chatbot",
    page_icon="🐶",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with input field improvements
st.markdown("""
<style>
    /* Previous styles remain the same */
    .main {
        padding: 2rem;
    }
    
    /* Enhanced input field styling with placeholder */
    .stTextInput > div > div > input {
        background-color: var(--background-color);
        border: 2px solid var(--secondary-background-color);
        border-radius: 12px;
        padding: 0.75rem;
        padding-right: 40px; /* Space for the hint */
        font-size: 1rem;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.2);
    }
    
    /* Input hint styling */
    .input-hint {
        position: fixed;
        bottom: 60px;
        right: 30px;
        background-color: var(--secondary-background-color);
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 0.8rem;
        opacity: 0.7;
        color: var(--text-color);
        pointer-events: none;
        z-index: 1000;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #45a049;
        transform: translateY(-1px);
    }
    
    /* Chat message styling */
    .chat-message {
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        display: flex;
        animation: fadeIn 0.5s ease;
    }
    
    .chat-message.user {
        background-color: rgba(43, 49, 62, 0.8);
    }
    
    .chat-message.bot {
        background-color: rgba(71, 80, 99, 0.8);
    }
    
    .chat-message .avatar {
        width: 15%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .chat-message .avatar img {
        max-width: 60px;
        max-height: 60px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid var(--text-color);
    }
    
    .chat-message .message {
        width: 85%;
        padding: 0 1.5rem;
        color: var(--text-color);
        font-size: 1rem;
        line-height: 1.5;
    }
    
    /* Loading animation */
    @keyframes pulse {
        0% { opacity: 0.4; }
        50% { opacity: 0.8; }
        100% { opacity: 0.4; }
    }
    
    .loading {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 1rem;
        background-color: var(--secondary-background-color);
        border-radius: 12px;
        animation: pulse 1.5s infinite;
    }
    
    /* Fade in animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Dark mode compatibility */
    .element-container, .stMarkdown, .css-10trblm {
        color: var(--text-color) !important;
    }
    
    .sidebar .sidebar-content {
        background-color: var(--secondary-background-color);
    }
    
    .stMarkdown p, .stMarkdown li {
        color: var(--text-color) !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-color) !important;
    }
</style>

<!-- Add keyboard hint -->
<div class="input-hint">
    Press ↵ to send
</div>
""", unsafe_allow_html=True)


st.markdown("""
    <h1 style='text-align: center; margin-bottom: 2rem; animation: fadeIn 1s ease;'>
        Data 8 Chatbot 🐶
    </h1>
""", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What would you like to know about Data 8? (Press Enter to send)"):

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner():
        relevant_chunks = query_processor.process_query(prompt)
        context = " ".join(relevant_chunks)
        response = response_generator.generate_response(prompt, context)
        
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Enhanced sidebar
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <h2 style='margin-bottom: 1rem;'>About Data 8 Chatbot</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        This chatbot is designed to help you learn about Data 8 course content. 
        Feel free to ask questions about:
        - Course concepts
        - Programming assignments
        - Statistical methods
        - Data visualization
        
    """)
    
    st.markdown("---")
    
    with st.expander("✨ Tips for better results"):
        st.markdown("""
            - Be specific in your questions
            - Provide context when needed
            - Ask follow-up questions
            - Press Enter to send your message
        """)
    
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <p style='font-size: 0.9rem;'>Made with ❤️ by Yash Thapliyal for future Data 8 Students</p>
        </div>
    """, unsafe_allow_html=True)


