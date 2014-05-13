from lru_cache import LRUCache

cache_size = 5

lru = LRUCache(cache_size)
lru.cache("a", 1)
lru.cache("b", 2)
lru.cache("c", 3)
lru.cache("d", 4)
lru.cache("e", 5)
lru.cache("f", 6)
lru.cache("g", 7)
lru.cache("h", 8)
lru.cache("i", 9)
lru.cache("j", 10)
lru.cache("k", 11)
lru.cache("c", 3)


print lru.cache("l", 12)