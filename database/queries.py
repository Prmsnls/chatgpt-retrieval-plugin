

import requests
from settings import GRAPHQL_ENDPOINT, GRAPHQL_TOKEN

def get_ads_data():
    body = """
            query GetAllAds {
                    asyncnewui_ads(order_by: {views: desc_nulls_last}) {
                        id
                        title
                    }
                }
        """
        
    variables={}


    headers = {"x-hasura-admin-secret": GRAPHQL_TOKEN}

    gql_response = requests.post(
        url=GRAPHQL_ENDPOINT,
        headers=headers,
        json={"query": body, "variables": variables},
    )

    response = gql_response.json()

    return response