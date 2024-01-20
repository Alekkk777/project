import streamlit as st
import streamlit.components.v1 as stc

HTML_BANNER = """
            <div style="background-color:#4645f;padding: 10px;border-radius: 10px; font-size: {}px">
            <h1 style="color:white; text-align: center;">Streamlit is Awesome </h1>
            <h1 style="color:white; text-align: center">Session State is Here!! </h1>  
            </div>          
        """

def main():
    st.title("Session States")
    menu = ["Home", "Custom Setting", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home Page")

        st.write(st.session_state)
        st.info("With Session State")
        if 'counter_one' not in st.session_state:
            st.session_state.counter_one = 0

        col1, col2 = st.columns(2)
        with col1:
            increment = st.button("Increment by one")
            if increment:
                st.session_state.counter_one += 1
        with col2:
            decrement = st.button("Decrement By one")
            if decrement:
                st.session_state.counter_one -= 1

        st.write("Counts [with session state]", st.session_state.counter_one)

    elif choice == "Custom Setting":
        st.subheader("App Custom Settings")
        if 'fontsize' not in st.session_state:
            st.session_state.fontsize = 12

        f1, f2 = st.columns(2)
        with f1:
            font_increment = st.button('Increase Font')
            if font_increment:
                st.session_state.fontsize += 5
        with f2:
            font_decrement = st.button('Decrease Font')
            if font_decrement:
                st.session_state.fontsize -= 5
        st.write("Current Font Size", st.session_state.fontsize)
        stc.html(HTML_BANNER.format(st.session_state.fontsize))
    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
