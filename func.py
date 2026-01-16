def get_rough_token_count(query: str, documents: list[str]) -> int:
    total_chars = len(query)
    total_chars += sum(len(d) for d in documents)
    total_chars *= len(documents)

    # 1 token ≈ 4 chars
    return max(1, total_chars // 4)