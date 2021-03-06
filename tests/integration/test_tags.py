import pytest
pytestmark = pytest.mark.django_db

from taiga.base import tags
from tests.models import TaggedModel


def test_tags():
    tags1 = TaggedModel.objects.create(tags=["foo", "bar"])
    tags2 = TaggedModel.objects.create(tags=["foo"])

    assert list(tags.filter(TaggedModel, contains=["foo"])) == [tags1, tags2]
    assert list(tags.filter(TaggedModel, contained_by=["foo"])) == [tags2]
    assert list(tags.filter(TaggedModel, overlap=["bar"])) == [tags1]

    assert list(tags.filter(TaggedModel, len=2)) == [tags1]
    assert list(tags.filter(TaggedModel, len__gte=1)) == [tags1, tags2]
    assert list(tags.filter(TaggedModel, len__lt=2)) == [tags2]

    assert list(tags.filter(TaggedModel, index__1="bar")) == [tags1]
    assert list(tags.filter(TaggedModel, index__1="bar", id__isnull=False)) == [tags1]
