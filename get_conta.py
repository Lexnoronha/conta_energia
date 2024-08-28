import requests

def baixar_pdf_cpfl(login_url, pdf_url, login_data, nome_arquivo):
    """
    Baixa uma conta PDF protegido por login de uma URL específica da CPFL.

    Args:
        login_url : URL da página de login.
        pdf_url : URL do PDF que se deseja baixar.
        login_data : Dicionário com os dados de login (usuário e senha).
        nome_arquivo : Nome do arquivo PDF a ser salvo localmente.
    """

    with requests.Session() as session:
        login_response = session.post(login_url, data=login_data)

        if login_response.status_code != 200:
            print(f"Erro ao fazer login: {login_response.status_code}")
            return

        response = session.get(pdf_url)

        if response.status_code == 200:
            with open(nome_arquivo, 'wb') as f:
                f.write(response.content)
            print(f"PDF baixado com sucesso como {nome_arquivo}")
        else:
            print(f"Erro ao acessar a página: {response.status_code}")

if __name__ == "__main__":
    num_conta = 914402182552
    login_url = 'https://cpflb2cprd.b2clogin.com/cpflb2cprd.onmicrosoft.com/b2c_1a_signup_signin_mfa_front/oauth2/v2.0/authorize?p=B2C_1A_SIGNUP_SIGNIN_MFA_FRONT&client_id=17d5831d-6741-4670-8085-d1d34e37aec1&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fwww.cpfl.com.br%2Fb2c-auth%2Freceive-token&scope=17d5831d-6741-4670-8085-d1d34e37aec1%20offline_access&response_type=code&prompt=login&response_mode=query'
    pdf_url = f"https://servicosonline.cpfl.com.br/agencia-webapi/api/historico-contas/conta-completa?numeroContaEnergia={num_conta}&codigoClasse=1&codEmpresaSAP=PIRA&instalacao=kb8YpPhir4UThpBR0wvKcG7vj0DdF%40ij4vpSj9T6Zps%3D&parceiroNegocio=LRZlFf*Arm2DVPk8Hd4PG2scEZIKSEranw%403xmFchZY%3D&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJUaXBvVXN1YXJpbyI6IjEiLCJDYW5hbCI6IjIiLCJMb2dpblByb3ZpZGVyIjoiSW5zdGFsYWNhbyIsIlN0YXR1c0lkIjoiMCIsIkxvZ2luQURSIjoidHJ1ZSIsIkRvY3VtZW50b1VzdWFyaW8iOiJZU0BPUG5sNHFQZ0xiVlhOaWhRSGgqZm1OdlhTMUJhS3c2UHZLSXRyRzEwPSIsIkxvZ2luVXN1YXJpbyI6IkE0ZW5sU2pTOWthbjJAMHdidW0qNFN1YzVVNVJDdHhXcG9wVzVAeG5IQ0k9IiwiQ29kaWdvVGlwb1BhcmNlaXJvIjoiNjU1MzUiLCJHcmF2YUxvZ05hdmVnYWNhbyI6InRydWUiLCJyb2xlIjpbIjUwNiIsIjUwNyIsIjUxMSIsIjkiLCI4OSIsIjk1IiwiOTkiLCIxMDYiLCIxMzIiLCI0OTkiLCI1MDAiLCI1MDEiLCI1MjEiLCI1MjIiLCI1MjMiLCI1MjYiLCIxMjgiLCIyMyIsIjM0IiwiOTAiLCIxMDAiLCIxMDMiLCIxMDkiLCIxMTAiLCIxMTEiLCIxMTIiLCIxMTQiLCIxMjIiLCI1MDMiLCI1MjAiLCI1MjQiLCI1MjUiLCI1MjgiLCI1MjkiLCI1MzAiLCI1MzEiLCI1NDAiLCI1MzMiLCI1NDgiLCI1NTAiLCI1NTIiLCI1MzYiLCI1NDMiLCI1NDEiLCI1MzciLCIxNDMiLCI1MzkiLCI1MDkiLCI1NDIiLCI1NTEiLCI1NTQiLCI1NTkiLCI1NjAiLCI1NDQiLCI1NTYiLCI1NTciXSwiSW5zdGFsYWNhbyI6IjIwOTAyNTEwODMiLCJFeGVjdXRhTG9nQ3JpcHRJbnB1dCI6ImZhbHNlIiwiRXhlY3V0YUxvZ0NyaXB0T3V0cHV0IjoiZmFsc2UiLCJQYXJhbWV0cm9DcmlwdG8iOiJmYWxzZSIsIlVzZXJDb2RlIjpbIkVWWENuaW9TRWQiLCJPNzQxMmM3dk43IiwiM1BzYW5kdnRQQyIsIkMxT08yV0NOWGYiLCJxSkN3blgzTFpsIiwiVGMyWVpZc0thcyIsImVEWE1uUzBuakwiLCJIV0x4WlR3bGtSIiwiUjhyam9NR0Z0dSIsIjZRZ0thTjZEdTEiLCJqalZ1TU92Qng3IiwidEsyaGFIQ2Y2WiIsIlhkcElNSTNkN2ciLCJoRUw2YUNKOEYwIiwiTFhBZk1EOTZHRiIsInlxd0c5RXc0SEwiLCIwUlU0TjhGWFFvIiwibWtKZTA5NlZTdSIsInpMcFJOM013Yk4iLCJhZWQyMDRDemNVIiwiRXpTY3Y1MnZkYSIsIk9Zd1AweklQbTQiLCIzcm55dnc5Tm4wIiwiQ1NJbjByUHF4YyIsInFsOE54dEZwd2kiLCJVNXh6aXU1bnlwIiwiZWZTbHhuTUc5SSIsIkl3R0xpb0JGME8iLCJTWm0weGhTaUlyIiwiNnNiamlpSWdKeiIsImpCUEpVajlmTDQiLCJ0bXY4aWRQOVRXIiwiWDZraFZlRThWZCIsImhnR1VqWFdhZTciLCJMeTU2VllMWWZDIiwieUl0ZkhaQlhnSSIsIjB0UFNWVFMxcGwiLCJuQ0U0SFVJd3FyIiwiem5rcVZOWlN5SyIsImI3WVFIT09RMlIiLCJFUE4yNFBFUDNYIiwiTzF0b0lJVnNCMSIsIjNKaE81SkxxQzciLCJDdURDSURjS0xaIiwiZThNQTU5WWtYRiIsIklRQmtxME9pWUwiLCJTMmhZNTRmQ2hvIiwiN0tXOXI1VkFpdSIsImpkS2lkNks5ajEiLCJ1RXFXcndjY3NUIl0sIkVtYWlsQjJDIjoibm9yb25oYWxleEBnbWFpbC5jb20iLCJpc3MiOiJodHRwczovL3NlcnZpY29zb25saW5lLmNwZmwuY29tLmJyLyIsImF1ZCI6ImFnZW5jaWEtdmlydHVhbC1jcGZsLXdlYiIsImV4cCI6MTcyNDgxMTY1MSwibmJmIjoxNzI0ODA4MDUxfQ.HAZxtiQbGfBzj9oO7tdtiWv-8CNaxnGLjExvPJVo0kY&contaAcumulada=false"
    login_data = {
        'username': 'noronhalex@gmail.com',
        'password': 'senha'
    }
    nome_arquivo = 'cpfl_conta_2via.pdf'

    baixar_pdf_cpfl(login_url, pdf_url, login_data, nome_arquivo)