import pytest

from src.pedido import calcular_total_pedido


def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [
        {"preco": 10},
        {"preco": 20}
    ]

    resultado = calcular_total_pedido(itens, 15)

    assert resultado == 30


def test_deve_calcular_total_quando_valor_for_igual_ao_minimo():
    itens = [
        {"preco": 10},
        {"preco": 10}
    ]

    resultado = calcular_total_pedido(itens, 20)

    assert resultado == 20


def test_deve_lancar_erro_quando_valor_minimo_nao_for_atingido():
    itens = [
        {"preco": 5},
        {"preco": 5}
    ]

    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 20)