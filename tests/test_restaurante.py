from pages.restaurante_page import RestaurantePage


def test_deve_abrir_detalhes_do_restaurante(page):
    restaurante = RestaurantePage(page)

    restaurante.acessar()

    restaurante.realizar_login(
        "kirst.gustavo@gmail.com",
        "souruivo123"
    )

    restaurante.abrir_primeiro_restaurante()

    assert "restaurant.html" in page.url