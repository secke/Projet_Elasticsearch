import sys
sys.path.append('.')
sys.path.append('..')

############ importation de elasticsearch ################
from elasticsearch import Elasticsearch


####### connection à Élastic ####################
es=Elasticsearch("http://localhost:9200",api_key=('',''))

