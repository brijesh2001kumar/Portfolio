import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title='My_Portfolio',
    page_icon='desktop_computer',
)



#settimng up background image for app
st.markdown(
   f'''
   <style>
   .stApp {{
             background: url("https://img.freepik.com/premium-photo/abstract-communication-technology-network-concept_34629-641.jpg?w=1380");
             background-size: cover
         }}
   </style>
   ''',
   unsafe_allow_html=True)

with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image('images/my_image1.png')
        with r:
            st.empty()
    
    choose = option_menu(
                        "Brijesh Kumar", 
                        ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Competitions", "Volunteering", "Resume", "Testimonials", "Contact"],
                        # ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Competitions", "Volunteering", "Blog", "Gallery", "Resume", "Testimonials", "Contact"],
                        #  icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'heart', 'pencil square', 'image', 'paperclip', 'star fill', 'envelope'],
                         icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'heart', 'image', 'paperclip', 'star fill', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "black"},
        "icon": {"color": "white", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    })


    linkedin_url = "https://in.linkedin.com/in/brijesh-kumar-a9236a271"
    github_url = "https://github.com/brijesh2001kumar"
    email_url = "brijesh_k@me.iitr.ac.in"

    linkedin_icon = "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png"
    email_icon = "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
    github_icon = "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png"

    

    a, left,middle, right,b = st.columns((.25,1,1,1,.25))
    with left:
        st.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="{linkedin_icon}" alt="Image" width=40></a>', unsafe_allow_html=True)
    with middle:
        st.markdown(f'<a href="{github_url}" target="_blank"><img src="{github_icon}" alt="Image" width=40></a>', unsafe_allow_html=True)
    with right:
        st.markdown(f'<a href="{email_url}" target="_blank"><img src="{email_icon}" alt="Image" width=40></a>', unsafe_allow_html=True)



def create_project(disp_text, project_link, github_link, video_loc):
    with st.container():
            st.markdown("<p style='text-align:left;font-size: 30px;'>{}</p>".format(disp_text), unsafe_allow_html=True)
            if video_loc[0]!='I': st.video(video_loc)
            else: st.image(video_loc)
            st.markdown("Wanna check out the project? - [link]({})<br>Don't forget to glance at the code - [Github Link]({})".format(project_link,github_link), unsafe_allow_html=True)
            st.markdown("---")

def education(image_loc, name, string):
    with st.container():
        left,right = st.columns((0.3,0.7))
        with left:
            st.image(image_loc)
        with right:
            st.subheader(name)
            st.write(string)
        st.markdown("---")

def technical_skills(category, link1, link2, link3):

    with st.container():
        st.subheader(category)
        st.text('')
        left,middle,right = st.columns((0.3,0.3,0.3))
        with left:
            if(link1!="nan"):st.image(link1,use_column_width=True)
            else: st.empty()
        with middle:
            if(link2!="nan"): st.image(link2,use_column_width=True)
            else: st.empty()
        with right:
            if(link3!="nan"): st.image(link3,use_column_width=True)
            else: st.empty()
        st.markdown("---")    


if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,.1,0.4))
        with left_column:
            st.markdown("<p style='text-align:center;font-size: 50px;'>About Me :)</p>", unsafe_allow_html=True)
            st.markdown("---")
            st.subheader("Aspiring Data Analyst/Product Manager")
            st.write("👋🏻 Hi, I'm Brijesh! I'm a Machine Learning and Deep Learning enthusiast, currently doing my BTech from IIT Roorkee. I have prior experiences in various machine learning application fields,  prior relevant experiences in tech, I am constantly seeking unique internships to broaden my horizons before embarking on my ML/DL journey upon graduation.")
            # st.write("💼 With the COVID-19 pandemic behind us, I believe there is potential for data science to be applied in the retail industry. In response to the increasing demand for data analytics from both online and brick-and-mortar sales, I am thus aiming to enter this industry for my first full-time job.")
            st.write("🏋🏻 In addition, I like to exercise in the gym, watching cricket, listening music,... enjoy eating good food in my free time!")
            st.write("👨🏼‍💻 Academic interests: Machine Learning & Deep Learning Applications, Data Visualization, Data Analysis, Computer Vision")
            # st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, Data Engineer, Business Intelligence Analyst, Product Manager")
            # st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/164EEVH6BmvC89q2M4WsBNF1JyddDAbNY/view?usp=sharing)")
        with middle_column:
            st.empty()
        with right_column:
            st.image('images/my_image2.jpg')




elif choose == 'Projects':

    st.markdown("<p style='text-align:center;font-size: 50px;'>My Projects</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    left_col, middle_col, right_col = st.columns((0.2,1,0.2))

    with left_col:
        st.empty()

    with middle_col:

        create_project(disp_text="Real-Time-Face-Verification",
                       project_link="https://realtimefaceverification-bsx4sajhzsut4fuaeccvht.streamlit.app/",
                       github_link = "https://github.com/brijesh2001kumar/Real_Time_Face_Verification",
                       video_loc="face_rec.mkv")
        
        create_project(disp_text="Real_Time_Object_Detecttion",
                       project_link="https://realtimeobjectdetecttiongit-e2wdopcrylgw2g8vb9njxx.streamlit.app/",
                       github_link = "https://github.com/brijesh2001kumar/Real_Time_Object_Detecttion",
                       video_loc="obj_det.mp4")
        
        create_project(disp_text="Knee-Bending-Medical-Exercise-Rep-Counter-and-Timer",
                       project_link="https://knee-bending-medical-exercise-rep-counter-and-timergit-snjgygk.streamlit.app/",
                       github_link = "https://github.com/brijesh2001kumar/Knee-Bending-Medical-Exercise-Rep-Counter-and-Timer",
                       video_loc="knee_bend.mp4")
        
        create_project(disp_text="Refrigeration_Parameter_Prediction",
                       project_link="https://refrigerationparameterpredictiongit-zgzhwgcacmceh8pnurugyp.streamlit.app/",
                       github_link = "https://github.com/brijesh2001kumar/Refrigeration_Parameter_Prediction",
                       video_loc="I_refrigeration.png")
        
        create_project(disp_text="Stock-Market-Prediction-Using-Numerical-and-Textual-Analysis",
                       project_link="https://stock-market-prediction-using-numerical-and-textual-analysisgi.streamlit.app/",
                       github_link = "https://github.com/brijesh2001kumar/Stock-Market-Prediction-Using-Numerical-and-Textual-Analysis",
                       video_loc="stock_price.mp4")
        
    with right_col:
        st.empty()



elif choose == 'Education':


    st.markdown("<p style='text-align:center;font-size: 50px;'>My Education</p>", unsafe_allow_html=True)
    st.markdown("---")

    college_name = "INDIAN INSTITUTE OF TECHNOLOLOGY ROORKEE"
    sen_sec_name = "NAND SINGH MEMORIAL SCHOOL,DASUYA-PUNJAB"
    sec_name = "MOUNT CARMEL SCHOOL,HOSHIARPUR-PUNJAB"

    college_pic = 'images/college.png'
    sen_sec_pic = 'images/sen_sec_school.png'
    sec_pic = 'images/sec_school.png'

    college_string = "Batchelores of Technology \n\nProduction and Industrial Engineering --- 2020-2024 \n\n**CGPA - 8.15**"
    sen_sec_string = "C.B.S.E 12th --- 2020 \n\n**Percentage - 94.2**"
    sec_string = "I.C.S.E 10th --- 2018 \n\n**Percentage - 94.6**"

    education(college_pic, college_name, college_string)
    education(sen_sec_pic, sen_sec_name, sen_sec_string)
    education(sec_pic, sec_name, sec_string)




elif choose == "Technical Skills":
    
    st.markdown("<p style='text-align:center;font-size: 50px;'>My Technical Skills</p>", unsafe_allow_html=True)
    st.markdown("---")
    

    category1 = 'Programming Languages'
    python = 'https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif'
    cplusplus = 'https://miro.medium.com/v2/resize:fit:640/0*3UD56f1LXF3Q8IrO.gif'
    technical_skills(category1,python, cplusplus,'nan')
    
    category2 = 'Academic Softwares'
    solidworks = 'https://1000logos.net/wp-content/uploads/2020/08/SolidWorks-Logo-640x400.png'
    autocad = 'https://logos-world.net/wp-content/uploads/2020/12/Autocad-Logo-2009-2014.png'
    technical_skills(category2,solidworks,autocad, 'nan')

    category3 = 'Data Visualization'
    matplotlib = 'https://image.pngaaa.com/242/4152242-middle.png'
    seaborn = 'https://seaborn.pydata.org/_images/logo-tall-lightbg.svg'
    technical_skills(category3, matplotlib, seaborn, 'nan')

    category4 = 'Cloud Platforms'
    streamlit = 'https://149695847.v2.pressablecdn.com/wp-content/uploads/2021/04/streamlit.gif'
    technical_skills(category4, streamlit, 'nan', 'nan')

    category5 = 'Version Control'
    git = 'https://assets.materialup.com/uploads/a8d3dcda-37d6-42bd-bb02-afecc006253d/preview.gif'
    docker = 'https://media.tenor.com/z3Vqx6hmE5QAAAAC/whale-docker.gif'
    technical_skills(category5, git, docker,'nan')

    category6 = 'Machine Learning Frameworks'
    sklearn = 'https://e7.pngegg.com/pngimages/39/4/png-clipart-logo-scikit-learn-python-github-machine-learning-text-orange.png'
    tensorflow = 'https://miro.medium.com/v2/resize:fit:1400/1*SB-Fu_AySBggAAxq0Q2Wew.gif'
    mediapipe = 'https://assets.codepen.io/5409376/internal/avatars/users/default.png?fit=crop&format=auto&height=512&version=1607020963&width=512'
    technical_skills(category6, sklearn, tensorflow, mediapipe)

    category7 = 'Python Libraries'
    numpy = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1280px-NumPy_logo_2020.svg.png'
    pandas = 'https://i.pinimg.com/1200x/28/ce/bf/28cebfa3c75ff7815999b0c81a826af6.jpg'
    opencv = 'https://opencv.org/wp-content/uploads/2020/07/OpenCV_logo_black-2.png'
    technical_skills(category7, numpy, pandas, opencv)

