import streamlit as st
from backend.mongodb import db
import bcrypt

# NEW
from backend.logger import log_login

st.title("🔐 Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    user = db.users.find_one(
        {"email": email}
    )

    if user:

        if bcrypt.checkpw(
            password.encode(),
            user["password"]
        ):

            # Active User Update
            db.users.update_one(
                {"email": email},
                {
                    "$set": {
                        "status": "active"
                    }
                }
            )

            # Login History Save
            log_login(email)

            st.session_state["login"] = True
            st.session_state["email"] = email
            st.session_state["role"] = user["role"]

            st.success(
                "Login Success"
            )

        else:

            st.error(
                "Wrong Password"
            )

    else:

        st.error(
            "User Not Found"
        )