import streamlit as st
import cloudinary
import cloudinary.uploader


cloudinary.config(
    cloud_name =  st.secrets["cloud_name"],
    api_key = st.secrets["api_key"],	
    api_secret = st.secrets["api_secret"]
)


def dashboard():
    st.sidebar.title("Welcome")
    option = st.sidebar.selectbox("Choose options :",["Upload Files","View Files"])
    log_out = st.sidebar.button("Logout")

    if option == "Upload Files":
        st.subheader("Upload Your Files Here!")
        uploadedFile = st.file_uploader("Choose File",type=["pdf","jpg","jpeg","png","mp3","mp4"])

        if uploadedFile:
            st.write("File Name :", uploadedFile.name)
            st.write("File Type :", uploadedFile.type)

            if "image" in uploadedFile.type:
                st.image(uploadedFile)
            if "video" in uploadedFile.type:
                st.video(uploadedFile)
            if "audio" in uploadedFile.type:
                st.audio(uploadedFile)

            if st.button("Upload File to Cloudinary"):
                uploaded_cloudinary = cloudinary.uploader.upload(uploadedFile,resource_type="auto")
                url=uploaded_cloudinary["secure_url"]
                st.write("Uploaded URL :",url)
                st.success("File Uploaded to Cloudinary")

    else:
        st.subheader("View Files")
    
    if log_out:
        st.session_state.user = None
        st.success("Logout Successfully")
        st.rerun()

            


        


