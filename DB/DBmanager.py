from .DBEngine import conn,session_threaded
from .DBmodel import USERDATA,SESSION,QUESTIONHISTORY
from contextlib import contextmanager
import uuid
import hashlib
import bcrypt
import os
from cryptography.fernet import Fernet


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = session_threaded()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class DBmanagerclass:
    def __init__(self) -> None:
        self.Secret_step=Fernet(os.getenv("SALT"))
    
    def encrypt_password(self,password,userid):
        shaHash=hashlib.sha512(password)
        hashedpass=bcrypt.hashpw(shaHash,userid)
        Final_password=self.Secret_Step.encrypt(hashedpass.encode())
        return Final_password
    
    @contextmanager
    def create_user(self,username,email,password):
        #check if the user exist
        with session_scope() as thread:
            check=bool(thread.query(USERDATA).filter_by(username.lower()).first())
            if check:
                print("this username already exist")
                return "this already exist"
        #creating a data
        userID=uuid.uuid4
        hashed_password=self.encrypt_password(password=password,userid=userID)
        #saving data in database
        try:
            with session_scope() as CommitSession:
                create_user=USERDATA(id=userID,username=username,email=email,password=hashed_password)
                CommitSession.add(create_user)
                CommitSession.commit()
            return True
        except Exception as ex:
            print(ex)
            CommitSession.rollback()
            return False

    def enable_2FA(self):
        pass

    def disable_2FA(self):
        pass

    def verify_email(self,Email):
        pass

    def auth_user(self,Email,password):
        with session_threaded as thread:
            check=thread.query(USERDATA).filter_by(Email).first()
            if check is not None:
                hash_pass=self.encrypt_password(password=password,userid=check.id)
                if check.password != hash_pass:
                    print("Not the Pasword")
                    return False
                else:
                    print("password is correct")
                    return True
            else:
                print("user dosnt exist")
                return False

    def check_2FA(self):
        pass

    def create_session(self):
        pass
    
    def join_session(self):
        pass

    def end_session(self):
        pass

    def generate_questions(self):
        pass
