import ssl

# Шлях до кореневого сертифіката
cert_path = 'C:\Windows\System32\config\systemprofile\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content'

# Встановлення кореневого сертифіката
ssl_context = ssl.create_default_context(cafile=cert_path)
