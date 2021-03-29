from selenium import webdriver

# 1. Criar um navegador webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 2. Navegar até um site
driver.get('https://automatize.netlify.app/')

# 3. Encontrar elementos
campo_email = driver.find_element_by_id('email')

# 4. Interagir com eles digitando ou clicando
# Clicar
campo_email.click()

# Digitar
campo_email.send_keys('jhonatan@hotmail.com')

# Encontrar elemento
campo_senha = driver.find_element_by_xpath("//input[@name='campoSenha']")
campo_senha.click()
campo_senha.send_keys('123456')

# Encontrar o botão de enviar
botao_enviar = driver.find_element_by_xpath("//button[text()='Enviar']")
botao_enviar.click()
