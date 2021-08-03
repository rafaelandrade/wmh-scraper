from faker import Faker
from scraper.quinto_andar.resident_block.main import get_resident_block_data

fake = Faker()


def test_get_resident_block_data(mocker):
    """Should return an schema the address"""
    address = fake.address()
    mocker.patch('scraper.quinto_andar.resident_block.main.street_view', return_value=address)

    data = get_resident_block_data(uuid='111', driver={})

    assert data.street_name == address
