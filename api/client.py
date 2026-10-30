"""
HTTP 客户端封装
把常用请求方法封装成类，方便测试用例复用
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class BaseClient:
    """
    HTTP 客户端基类
    - 支持 base_url
    - 支持自定义 headers
    - 支持重试机制
    """

    def __init__(self, base_url: str, headers: dict = None, timeout: int = 10, retries: int = 3):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

        # 设置默认请求头
        self.session.headers.update(headers or {})

        # 添加重试机制（GET 请求失败自动重试）
        retry = Retry(total=retries, backoff_factor=0.3, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _url(self, path: str) -> str:
        """拼接完整 URL"""
        if path.startswith("http"):
            return path
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path, params=None, **kwargs):
        return self.session.get(self._url(path), params=params, timeout=self.timeout, **kwargs)

    def post(self, path, json=None, data=None, **kwargs):
        return self.session.post(self._url(path), json=json, data=data, timeout=self.timeout, **kwargs)

    def put(self, path, json=None, data=None, **kwargs):
        return self.session.put(self._url(path), json=json, data=data, timeout=self.timeout, **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(self._url(path), timeout=self.timeout, **kwargs)

    def close(self):
        self.session.close()
