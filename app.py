from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie 


st.set_page_config(page_title="Gaming",page_icon=":video_game:",layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  

#local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")








lottie_gaming = load_lottieurl("https://lottie.host/fb2dcc6a-5de3-4145-9a67-a621ab9cce5c/qZmkarnC40.json")
avater = Image.open("images/avater.png")
Ryan = Image.open("images/RYAN.png")




st.subheader("Hey, I am Pelu :wave:")
st.title("Gaming Is Love")
st.write("Eat Sleep Game Repeat")
st.write("[Learn More >](https://discord.gg/EeRjN4Anz4)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
are looking for a way to leverage the power of Python in their day-to-day work.
are struggling with repetitive tasks in Excel and are looking for a way to use Python and VB
want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
are working with Excel and found themselves thinking "there has to be a better way."
    
     """
    
    )
    st.write("[YouTube Channel >](https://www.youtube.com/channel/UCOVQNTjVBvci3Acnmm63adA)")
with right_column:
    st_lottie(lottie_gaming,height=300,key="Gaming")

#-----PROJECT----
with st.container():
     st.write("---")
     st.header("My Achievements")
     st.write("##")
     image_column,text_column = st.columns((1,2))
     with image_column:
         st.image(avater)
         
         with text_column:
          st.subheader("I Am A Pro In Valorant")
          st.write(
             """
                I have being playing this game since last 3 years and I love it
             """
                 )    
          st.markdown("[Watch Video...](https://www.youtube.com/watch?v=TezeUohQpng&t=25s)")


with st.container():
         image_column,text_column = st.columns((1,2))   
         with image_column:
             st.image(Ryan)
         with text_column:
             st.subheader("I Also Do Thumbnails And Video Editing")
             st.write(
                 """
                    I use to do small youtubers thumbnails and had contacts with them and i use to edit my gaming clips and make montages
                """  
                     )    
             st.markdown("[Watch Video...](https://www.youtube.com/watch?v=0bqXqkWgfM0&t=50s)")

#---contact---

st.write("---")
st.header("Get In Touch With Me!")
st.write("##")


contact_form = """

<form action="https://formsubmit.co/utsavkarmakarpurulia@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>

"""

left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()


































