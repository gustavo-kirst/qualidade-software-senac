from pytest_bdd import scenarios, given, when, then
from pages.restaurante_page import RestaurantePage

scenarios("../features/visualizacao_restaurante.feature")


@given("que o usuário acessa a página de login")
def acessar_pagina(page):
    restaurante = RestaurantePage(page)
    restaurante.acessar()


@when("realizar login com credenciais válidas")
def realizar_login(page):
    restaurante = RestaurantePage(page)
    restaurante.realizar_login(
        "kirst.gustavo@gmail.com",
        "souruivo123"
    )


@when("selecionar um restaurante")
def selecionar_restaurante(page):
    restaurante = RestaurantePage(page)
    restaurante.abrir_primeiro_restaurante()


@then("o sistema deve exibir a página de detalhes do restaurante")
def validar_pagina(page):
    assert "restaurant.html" in page.url

@given("que o usuário está na página de detalhes do restaurante")
def abrir_detalhes(page):
    restaurante = RestaurantePage(page)
    restaurante.acessar()
    restaurante.realizar_login(
        "kirst.gustavo@gmail.com",
        "souruivo123"
    )
    restaurante.abrir_primeiro_restaurante()


@when("visualizar as informações disponíveis")
def visualizar_informacoes():
    pass


@then("o nome do restaurante deve estar visível")
def validar_nome(page):
    assert page.locator("#restName").is_visible()