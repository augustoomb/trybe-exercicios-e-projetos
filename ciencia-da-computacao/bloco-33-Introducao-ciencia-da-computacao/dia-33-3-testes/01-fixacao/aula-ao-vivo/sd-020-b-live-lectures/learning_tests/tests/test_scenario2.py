import pytest
from src.scenario1 import generate_simple_report

@pytest.fixture
def stock():
    return [
         {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus"
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi non quam nec dui luctus rutrum nulla tellus in sagittis dui vel nisl duis"
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2019-09-13",
        "data_de_validade": "2023-02-13",
        "numero_de_serie": "BA52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "morbi quis tortor id nulla ultrices aliquet maecenas leo odio condimentum id luctus nec molestie sed justo"
    },
    {
        "id": 4,
        "nome_do_produto": "Uricum acidum, Benzoicum acidum, Berber. vulg., Bryonia, Cantharis, Carduus benedictus, Ceanothus, Chelidonium majus, Chionanthus virginica, Cinchona, Dioscorea, Dolichos, Iris versicolor, Juniperus com., Nux vom.,Ptelea,Taraxacum, Carduus mar., Cynara scolymus, Solidago",
        "nome_da_empresa": "Newton Laboratories, Inc.",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum in hac habitasse platea dictumst morbi vestibulum velit id pretium iaculis diam erat fermentum"
    }
    ]

def test_report_must_contain_older_manufacturing_date(stock):
    report = generate_simple_report(stock)
    assert "Data de fabricação mais antiga: 2019-09-13" in report


def test_report_must_contain_closest_expiration_date(stock):
    report = generate_simple_report(stock)
    assert "Data de validade mais próxima: 2023-01-17" in report


def test_must_contain_the_company_with_the_largest_quantity_of_products_stocked(
    stock,
):
    report = generate_simple_report(stock)
    assert (
        "Empresa com maior quantidade de produtos estocados: sanofi-aventis U.S. LLC"
        in report
    )