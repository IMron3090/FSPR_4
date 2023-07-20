import requests
import hashlib


def request_api_data(query_param):
    url = "https://api.pwnedpasswords.com/range/" + str(query_param)
    result = requests.get(url)
    if result.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {result.status_code}, chek an API and try again."

        )
    
    return result 


def get_psw_leaks_count(hashes,hash_to_check):
    hashes = (hash.split(":")for hash in hashes.splitlines())

    for hash ,count in hashes:
        if hash == hash_to_check:
            return count 
        
        return 0
    
