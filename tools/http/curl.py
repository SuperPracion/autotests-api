from httpx import Request, RequestNotRead


def make_curl_from_request(request: Request) -> str:
    """
    Генерирует команду cURL из HTTP-запроса httpx.

    :param request: HTTP-запрос, из которого будет сформирована команда cURL.
    :return: Строка с командой cURL, содержащая метод запроса, URL, заголовки и тело (если есть).
    """
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    return " \\\n  ".join(result)
