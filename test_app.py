from app import app

def test_home_status_code():
    """Garante que a rota principal retorna status HTTP 200"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_home_content_message():
    """Garante que a mensagem correta é retornada na rota principal"""
    client = app.test_client()
    response = client.get('/')
    assert b"Hello, DevOps CI/CD Project!" in response.data

def test_home_content_type():
    """Garante que a resposta da API é do tipo JSON"""
    client = app.test_client()
    response = client.get('/')
    assert response.content_type == 'application/json'

def test_non_existent_route():
    """Garante que rotas inexistentes retornam erro 404 (Not Found)"""
    client = app.test_client()
    response = client.get('/rota-que-nao-existe')
    assert response.status_code == 404

def test_response_json_structure():
    """Garante que a chave 'message' está presente no JSON retornado"""
    client = app.test_client()
    response = client.get('/')
    json_data = response.get_json()
    assert 'message' in json_data
    assert json_data['message'] == "Hello, DevOps CI/CD Project!"
