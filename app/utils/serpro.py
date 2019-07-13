from requests import get


def serpro_response(cpf: str, token: str='4e1a1858bdd584fdc077fb7d80f39283') -> [dict, str]:
    """function to make requests in the serpro API."""
    headers = {
        'Content-Type': "application/json",
        'Authorization': f"Bearer {token}",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "apigateway.serpro.gov.br",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    base_url = f'https://apigateway.serpro.gov.br/consulta-cpf-trial/v1/cpf/{cpf}'
    response = get(base_url, headers=headers)

    if response.status_code == 200:
        return response.json(), response.status_code
    return 'Nenhum registro encontrado.', response.status_code
