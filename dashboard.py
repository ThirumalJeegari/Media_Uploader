import streamlit as st
import cloudinary
import cloudinary.uploader
from db_C import cursor,con
import pandas as pd


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
            elif "video" in uploadedFile.type:
                st.video(uploadedFile)
            elif "audio" in uploadedFile.type:
                st.audio(uploadedFile)
            elif "pdf" in uploadedFile.type:
                st.write("PDF file uploaded")

            if st.button("Upload File to Cloudinary"):
                uploaded_cloudinary = cloudinary.uploader.upload(uploadedFile,resource_type="auto")
                url=uploaded_cloudinary["secure_url"]

                # SAVE TO DATABASE (IMPORTANT)
                cursor.execute("""
                    INSERT INTO files(user_id, file_name, file_type, file_url)
                    VALUES(%s,%s,%s,%s)
                """, (
                    st.session_state.user["id"],
                    uploadedFile.name,
                    uploadedFile.type,
                    url
                ))

                con.commit()



                st.write("Uploaded URL :",url)
                st.success("File Uploaded to Cloudinary")

    else:
        st.subheader("View Files")
        

        cursor.execute("""
        SELECT users.name, files.file_name, files.file_type, files.file_url, files.upload_date
        FROM files
        JOIN users ON users.id = files.user_id
        ORDER BY files.upload_date DESC
        """)

        data = cursor.fetchall()

        if data:
            df = pd.DataFrame(data)
            st.dataframe(df)

            for row in data:
                st.markdown(f"**User:** {row['name']}")
                st.write(row["file_name"])

                if "image" in row["file_type"]:
                    st.image(row["file_url"])

                elif "video" in row["file_type"]:
                    st.video(row["file_url"])

                elif "audio" in row["file_type"]:
                    st.audio(row["file_url"])


                else:
                    st.markdown(f"[Open File]({row['file_url']})")

                st.divider()

        else:
            st.info("No files uploaded yet")
    
    if log_out:
        st.session_state.user = None
        st.success("Logout Successfully")
        st.rerun()

            


        


