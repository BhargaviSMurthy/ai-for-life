fx_service/
│
├── fx/                     # Main package
│   ├── __init__.py
│   ├── models.py          # dataclasses, dunder methods
│   ├── api_client.py      # async API calls + error handling
│   ├── processor.py       # business logic
│   ├── holidays.py        # holiday detection
│   ├── logger.py          # logging setup
│   ├── storage.py         # file saving (CSV/JSON)
│   └── exceptions.py      # custom error types
│
├── cli.py                 # CLI entry point
├── app.py                 # FastAPI endpoint
├── requirements.txt
└── tests/
    ├── test_processor.py
    └── test_api_client.py
