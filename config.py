import os

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
# THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
# CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
# CSRF_SESSION_KEY = "ksdjfhkasdjfskdnvklsjadhvklasjdhfklsndflkajdlkfjsdfas"

# Secret key for signing cookies
# SECRET_KEY = "asdkjfhsdsdfasfuiwehfkjnsd,fmnsadfnsdfsd4341234123wdfd"

# MongoDB conenction parameters
MONGO_DBNAME = "hospitalDB"
MONGO_COLNAME= "hospitalList"
MONGO_HOST = "localhost"
MONGO_PORT = 27017

# HASH_SECRET="klsdhjfsdflkajfh82379o3ijrl.,dsasdfsac,sxmcn,sjdhasudhflaks"
#
# CONTACT_EMAILS = [
#     "jeeves@ynos.in"
# ]
