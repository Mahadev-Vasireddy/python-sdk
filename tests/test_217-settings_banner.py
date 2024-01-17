import datetime
from .cache import *  # will also import some globals like `britive`


def test_get():
    banner = britive.settings.banner.get()
    assert isinstance(banner, dict)


def test_set_no_schedule():
    banner = britive.settings.banner.set(message='test', display_banner=True, message_type='INFO')
    assert isinstance(banner, dict)
    for key in ['status', 'messageType', 'message']:
        assert key in banner
    assert 'messageSchedule' not in banner


def test_set_with_schedule():
    banner = britive.settings.banner.set(
        message='test',
        display_banner=True,
        message_type='INFO',
        start_datetime=datetime.datetime(year=2024, month=1, day=1),
        end_datetime=datetime.datetime(year=2024, month=1, day=31),
        time_zone='UTC'
    )
    assert isinstance(banner, dict)
    for key in ['status', 'messageType', 'message', 'messageSchedule']:
        assert key in banner
    for key in ['startDate', 'endDate', 'timeZone']:
        assert key in banner['messageSchedule']


def test_set_with_incorrect_schedule():
    with pytest.raises(ValueError):
        britive.settings.banner.set(
            message='test',
            display_banner=True,
            message_type='INFO',
            start_datetime=datetime.datetime(year=2024, month=1, day=1),
            time_zone='UTC'
        )

    with pytest.raises(ValueError):
        britive.settings.banner.set(
            message='test',
            display_banner=True,
            message_type='INFO',
            end_datetime=datetime.datetime(year=2024, month=1, day=1),
            time_zone='UTC'
        )

    with pytest.raises(ValueError):
        britive.settings.banner.set(
            message='test',
            display_banner=True,
            message_type='INFO',
            start_datetime=datetime.datetime(year=2024, month=1, day=1),
            end_datetime=datetime.datetime(year=2024, month=1, day=1)
        )

    with pytest.raises(ValueError):
        britive.settings.banner.set(
            message='test',
            display_banner=True,
            message_type='INFO',
            start_datetime=datetime.datetime(year=2024, month=1, day=1)
        )

    with pytest.raises(ValueError):
        britive.settings.banner.set(
            message='test',
            display_banner=True,
            message_type='INFO',
            end_datetime=datetime.datetime(year=2024, month=1, day=1)
        )

    with pytest.raises(ValueError):
        britive.settings.banner.set(
            message='test',
            display_banner=True,
            message_type='INFO',
            time_zone='UTC'
        )
