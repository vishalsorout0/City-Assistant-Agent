import streamlit as st
from agent import agent

st.set_page_config(
    page_title="City Assistant",
    page_icon="🌍"
)

st.title("🌍 City Assistant")
st.caption("Ask me about weather and latest news of any city.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask something...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        try:
            response = agent.stream(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                },
                stream_mode="updates"
            )

            final_answer = ""

            for chunk in response:

                if "messages" in chunk:
                    message = chunk["messages"][-1]

                    if hasattr(message, "content") and message.content:
                        final_answer = message.content
                        placeholder.markdown(final_answer)

            if not final_answer:
                result = agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    }
                )

                final_answer = result["messages"][-1].content
                placeholder.markdown(final_answer)

        except Exception as e:
            final_answer = f"❌ {e}"
            placeholder.error(final_answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_answer,
        }
    )