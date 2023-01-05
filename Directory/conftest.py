import pytest , datetime, pytz

@pytest.mark.fixture(autouse=True)
def getdateandtime():
    print(datetime.datetime.now(pytz.timezone('Asi/Kolkata ')))
