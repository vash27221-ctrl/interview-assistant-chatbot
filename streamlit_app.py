import streamlit as st
import time
import json
from kiro7 import InterviewOrchestrator
import os

# Page configuration
st.set_page_config(
    page_title="Interview Assistant Chatbot",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern, interactive UI
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #6366f1;
        --secondary-color: #8b5cf6;
        --background-color: #0f172a;
        --card-background: #1e293b;
        --text-color: #e2e8f0;
        --border-color: #334155;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        animation: fadeIn 0.8s ease-in;
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    /* Chat message styling */
    .chat-message {
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
        animation: slideIn 0.5s ease-out;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .chat-message.bot {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-left: 5px solid #8b5cf6;
    }
    
    .chat-message.user {
        background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
        color: white;
        border-left: 5px solid #06b6d4;
    }
    
    .chat-message .role {
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        opacity: 0.9;
    }
    
    .chat-message .content {
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* Typing indicator */
    .typing-indicator {
        display: flex;
        align-items: center;
        padding: 1rem;
        background: rgba(102, 126, 234, 0.1);
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .typing-indicator span {
        height: 10px;
        width: 10px;
        background: #667eea;
        border-radius: 50%;
        display: inline-block;
        margin: 0 3px;
        animation: bounce 1.4s infinite ease-in-out both;
    }
    
    .typing-indicator span:nth-child(1) {
        animation-delay: -0.32s;
    }
    
    .typing-indicator span:nth-child(2) {
        animation-delay: -0.16s;
    }
    
    @keyframes bounce {
        0%, 80%, 100% { 
            transform: scale(0);
        } 40% { 
            transform: scale(1.0);
        }
    }
    
    /* Analysis dropdown styling */
    .analysis-container {
        background: rgba(102, 126, 234, 0.05);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 10px;
        padding: 1rem;
        margin-top: 0.5rem;
    }
    
    .analysis-label {
        color: #667eea;
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    .analysis-content {
        color: #94a3b8;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Input styling */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid rgba(102, 126, 234, 0.3);
        padding: 0.75rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    }
    
    /* Stats card */
    .stats-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    .stats-card h3 {
        color: #667eea;
        font-size: 2rem;
        margin: 0;
        font-weight: 700;
    }
    
    .stats-card p {
        color: #94a3b8;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Progress bar */
    .progress-container {
        background: rgba(102, 126, 234, 0.1);
        border-radius: 10px;
        height: 8px;
        margin: 1rem 0;
        overflow: hidden;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.chatbot = None
    st.session_state.messages = []
    st.session_state.interview_started = False
    st.session_state.interview_ended = False
    st.session_state.domain = ""
    st.session_state.question_count = 0
    st.session_state.show_analysis = {}
    st.session_state.theme_color = "#667eea"

def typewriter_effect(text, speed=0.03):
    """Display text with typewriter effect"""
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f'<div class="chat-message bot"><div class="role">🤖 Interviewer</div><div class="content">{displayed_text}▌</div></div>', unsafe_allow_html=True)
        time.sleep(speed)
    placeholder.markdown(f'<div class="chat-message bot"><div class="role">🤖 Interviewer</div><div class="content">{displayed_text}</div></div>', unsafe_allow_html=True)
    return placeholder

def display_message(role, content, analysis=None, msg_id=None):
    """Display a chat message with optional analysis"""
    if role == "bot":
        st.markdown(f'<div class="chat-message bot"><div class="role">🤖 Interviewer</div><div class="content">{content}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message user"><div class="role">👤 You</div><div class="content">{content}</div></div>', unsafe_allow_html=True)
    
    # Show analysis if available
    if analysis and msg_id is not None:
        with st.expander("📊 View Analysis", expanded=False):
            st.markdown(f'<div class="analysis-container">', unsafe_allow_html=True)
            
            # Display analysis notes
            if 'analysis_notes' in analysis:
                st.markdown(f'<div class="analysis-label">Analysis Notes:</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="analysis-content">{analysis["analysis_notes"]}</div>', unsafe_allow_html=True)
            
            # Display answer type
            if 'answer_type' in analysis:
                st.markdown(f'<div class="analysis-label">Answer Type:</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="analysis-content">{analysis["answer_type"]}</div>', unsafe_allow_html=True)
            
            # Display content summary
            if 'content_summary' in analysis:
                st.markdown(f'<div class="analysis-label">Summary:</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="analysis-content">{analysis["content_summary"]}</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

def show_typing_indicator():
    """Show typing indicator animation"""
    return st.markdown("""
        <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
        </div>
    """, unsafe_allow_html=True)

# Main header
st.markdown("""
    <div class="main-header">
        <h1>🎯 Interview Assistant Chatbot</h1>
        <p>Your AI-powered technical interview companion</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    # Theme color picker
    theme_color = st.color_picker("Choose Theme Color", st.session_state.theme_color)
    if theme_color != st.session_state.theme_color:
        st.session_state.theme_color = theme_color
    
    # Font size
    font_size = st.slider("Font Size", 0.9, 1.5, 1.1, 0.1)
    
    # Typewriter speed
    typewriter_speed = st.slider("Question Speed", 0.01, 0.1, 0.03, 0.01)
    st.session_state.typewriter_speed = typewriter_speed
    
    st.markdown("---")
    
    # Stats
    if st.session_state.interview_started:
        st.markdown(f"""
            <div class="stats-card">
                <h3>{st.session_state.question_count}</h3>
                <p>Questions Asked</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Instructions
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. Enter your interview domain
    2. Click 'Start Interview'
    3. Answer questions naturally
    4. View analysis via dropdown
    5. Type 'quit' to end anytime
    """)
    
    st.markdown("---")
    
    # About
    with st.expander("ℹ️ About"):
        st.markdown("""
        This AI interview assistant uses:
        - **Gemini AI** for question generation
        - **Local SLM** for smart triage
        - **Adaptive difficulty** based on performance
        - **Real-time analysis** of your answers
        """)

# Main content area
if not st.session_state.interview_started:
    # Welcome screen
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 🚀 Ready to begin?")
        st.markdown("Enter the technical domain you'd like to be interviewed on:")
        
        domain = st.text_input(
            "Interview Domain",
            placeholder="e.g., Machine Learning, Python, Data Structures...",
            label_visibility="collapsed"
        )
        
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            if st.button("🎯 Start Interview", use_container_width=True):
                if domain:
                    with st.spinner("🔄 Initializing interview..."):
                        try:
                            st.session_state.chatbot = InterviewOrchestrator(domain)
                            
                            # Check for rate limit during initialization
                            if st.session_state.chatbot.rate_limit_hit:
                                st.error("🚨 Rate limit reached. Please try again later.")
                                st.stop()
                            
                            if not st.session_state.chatbot.current_topic:
                                st.error("❌ Failed to create interview syllabus. Please try again.")
                                st.stop()
                            
                            # Start interview
                            question = st.session_state.chatbot.start_interview()
                            
                            # Check if start_interview hit rate limit
                            if isinstance(question, dict) and question.get("status") == "TERMINATED":
                                st.error("🚨 Rate limit reached. Please try again later.")
                                st.stop()
                            
                            st.session_state.messages.append({
                                "role": "bot",
                                "content": question,
                                "analysis": None
                            })
                            st.session_state.interview_started = True
                            st.session_state.domain = domain
                            st.session_state.question_count = 1
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Error starting interview: {str(e)}")
                else:
                    st.warning("⚠️ Please enter an interview domain")

else:
    # Interview in progress
    st.markdown(f"### 📚 Domain: {st.session_state.domain}")
    
    # Display chat history
    for idx, message in enumerate(st.session_state.messages):
        display_message(
            message["role"],
            message["content"],
            message.get("analysis"),
            idx
        )
    
    # Input area
    if not st.session_state.interview_ended:
        user_input = st.chat_input("Type your answer here... (or 'quit' to end)")
        
        if user_input:
            # Add user message
            st.session_state.messages.append({
                "role": "user",
                "content": user_input,
                "analysis": None
            })
            
            # Check for quit
            if user_input.lower() in ['quit', 'exit']:
                st.session_state.interview_ended = True
                st.session_state.messages.append({
                    "role": "bot",
                    "content": "Thank you for participating! The interview has ended. 🎉",
                    "analysis": None
                })
                st.rerun()
            
            # Process answer
            with st.spinner(""):
                typing_placeholder = st.empty()
                typing_placeholder.markdown("""
                    <div class="typing-indicator">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                """, unsafe_allow_html=True)
                
                try:
                    response = st.session_state.chatbot.process_user_answer(user_input)
                    typing_placeholder.empty()
                    
                    if response['status'] == "TERMINATED":
                        st.session_state.interview_ended = True
                        if response.get("reason") == "RateLimit":
                            end_message = "🚨 Rate limit reached. Thank you for your time!"
                        elif response.get("reason") == "SyllabusFinished":
                            end_message = "🎉 That covers all topics! Thank you for your time!"
                        else:
                            end_message = "Thank you for your time. The interview has concluded."
                        
                        st.session_state.messages.append({
                            "role": "bot",
                            "content": end_message,
                            "analysis": response.get('analysis')
                        })
                    else:
                        st.session_state.question_count += 1
                        st.session_state.messages.append({
                            "role": "bot",
                            "content": response['next_question'],
                            "analysis": response.get('analysis')
                        })
                    
                    st.rerun()
                    
                except Exception as e:
                    typing_placeholder.empty()
                    st.error(f"❌ An error occurred: {str(e)}")
    else:
        # Interview ended
        st.markdown("---")
        st.markdown("### 🎊 Interview Complete!")
        st.markdown("Thank you for using the Interview Assistant Chatbot.")
        
        if st.button("🔄 Start New Interview", use_container_width=True):
            # Reset session state
            st.session_state.initialized = False
            st.session_state.chatbot = None
            st.session_state.messages = []
            st.session_state.interview_started = False
            st.session_state.interview_ended = False
            st.session_state.domain = ""
            st.session_state.question_count = 0
            st.rerun()
