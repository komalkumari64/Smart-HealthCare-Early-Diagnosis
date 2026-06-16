import streamlit as st
from backend.mongodb import db
import bcrypt

st.title("📝 Signup")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input(
    "Password",
    type="password"
)

if st.button("Signup"):

    user = db.users.find_one(
        {"email": email}
    )

    if user:

        st.error(
            "Email already exists"
        )

    else:

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        db.users.insert_one({
            "name": name,
            "email": email,
            "password": hashed,
            "status": "active",
            "role": "user"
        })

        st.success(
            "Account Created Successfully"
        )