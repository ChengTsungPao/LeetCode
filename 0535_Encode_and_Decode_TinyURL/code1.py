import binascii

class Codec:

    def encode(self, longUrl: str) -> str:
        return binascii.hexlify(longUrl.encode())

    def decode(self, shortUrl: str) -> str:
        return binascii.unhexlify(shortUrl).decode()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))