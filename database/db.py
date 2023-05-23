
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from settings  import GRAPHQL_ENDPOINT, GRAPHQL_TOKEN

headers = {
    "x-hasura-admin-secret": GRAPHQL_TOKEN
}


# Set up a transport to send the GraphQL request
transport = RequestsHTTPTransport(url=GRAPHQL_ENDPOINT, headers=headers)

# Create a GraphQL client using the transport
DB_CLIENT = Client(transport=transport)
