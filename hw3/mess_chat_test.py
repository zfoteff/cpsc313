from logger import Logger
import requests as req
import time

TEST_URL = 'http://localhost:8000/'

logger = Logger('api_tests')

def test_successful_connection():
    start_time = time.perf_counter()
    try:
        res = req.get(TEST_URL)
        assert True
        elapsed_time = time.perf_counter() - start_time
        logger(f"Completed successfuly connection test in {elapsed_time:.5f}")
    except req.exceptions.ConnectionError:
        logger("Failed connection test. Ensure test server is running before re-running tests")
        assert False

def test_get_root():
    start_time = time.perf_counter()
    res = req.get(TEST_URL)
    message_payload = res.json()
    assert res.status_code == 200 and message_payload["message"] == "You've hit Zac's API root endpoint"
    elapsed_time = time.perf_counter() - start_time
    logger("Completed GET root test")
    
def test_send_route():
    test_message = "TEST MESSAGE FOR CONSUMPTION"
    start_time = time.perf_counter()
    res = req.post(TEST_URL+f"send/?message={test_message}")
    result_message = res.json()
    assert res.status_code == 200 and result_message["result"] == "ENQUEUED MESSAGE"
    elapsed_time = time.perf_counter() - start_time
    logger("Completed send message route test in {elapsed_time:.5f}")

def test_message_route():
    res = req.get()
    logger("Completed test_message route")
