import requests

def get_fitness(gene):
    payload = {
            'phi1': gene[0],
            'theta1': gene[1],
            'phi2': gene[2],
            'theta2': gene[3],
            'phi3': gene[4],
            'theta3': gene[5]
    }
    url = "http://localhost:8080/antenna/simulate"

    r = requests.get(url, params=payload)
    text_response = r.text
    score = float(text_response.split()[0])
    return score