# Giswater API Plugin Example

This repository provides an example of a plugin for the Giswater API based on FastAPI. It serves as a reference for structuring and correctly integrating a new plugin into the system.

## 📂 Plugin Structure

The plugin follows a specific structure to ensure compatibility with the Giswater API:

```
plugin_example/
│── models/
|   |── example_model.py
│── routers/
|   |── example_router.py
│── __init__.py
│── requirements.txt [TODO]
```

### 📌 File Explanation:
- `__init__.py`: Allows the folder to be treated as a Python module. Must have the `register_plugin` method in it.
- `models`: Defines data models (Pydantic, SQLAlchemy, etc.).
- `routers`: Defines the plugin's endpoints.
- `requirements.txt`: Dependencies required for the plugin to function. [TODO]

## 🚀 Installation and Integration

To integrate this plugin into the Giswater API, follow these steps:

1. **Place the plugin folder** inside the Giswater API plugins directory:
   ```
   /path/to/giswater-api/plugins/example_plugin/
   ```

2. **Restart the Giswater API** to load the new plugin:
   ```bash
   systemctl restart giswater-api  # (if running as a service)
   ```
   ```bash
   docker-compose down  # (if running as a docker)
   docker-compose up --build -d
   ```

## 📢 Plugin Usage

Once the plugin is integrated, its endpoints will be available in the Giswater API.

If the plugin defines an endpoint like this in `routes.py`:
```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
def example_endpoint():
    return {"message": "Plugin example working!"}
```

The endpoint will be available at:
```
http://localhost:8000/api/plugin_example/example
```

## 📄 License

This project is distributed under the GPL 3.0 license. See the `LICENSE` file for more details.

