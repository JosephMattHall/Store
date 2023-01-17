from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base
from datetime import datetime
from models import File


class Storage():

    def __init__(self):
        # import all modules here that might define models so that
        # they will be registered properly on the metadata.  Otherwise
        # you will have to import them first before calling init_db()
        engine = create_engine('sqlite:///db')
        
        from models import File
        Base.metadata.create_all(bind=engine)
        self.session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
        


    def save_file(self, data):
        name = data["fname"]
        path = data["path"]
        timestamp = data["timestamp"]
        last_modified = datetime.fromtimestamp(timestamp)

        new_file = File(name=name, path=path, last_modified=last_modified)

        self.session.add(new_file)

        self.session.commit()

        return True

    def save_files(self, files):
        new_files = []
        for file in files:
            name = file["fname"]
            path = file["path"]
            timestamp = file["timestamp"]
            last_modified = datetime.fromtimestamp(timestamp)

            new_file = File(name=name, path=path, last_modified=last_modified)
            new_files.append(new_file)
        self.session.add_all(new_files)
        return True

    def get_all(self):
        files = self.session.query(File).all()
        return files

    def get_file(self, file_name):
        file = self.session.query(File.name).filter_by(name=file_name).first()
        return file

