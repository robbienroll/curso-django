import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('nome_do_video',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1>Video Aperitivo: Nome do Video</h1>')


def test_conteudo_video(resp):
    assert_contains(resp,'<iframe src="https://player.vimeo.com/video/81396059?h=a372215d7c"')
