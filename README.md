# technical_test_skaller_digital

# Teste Técnico - Microserviço de Envio de E-mails

## Instruções
Crie um microserviço simples que permita o envio de e-mails utilizando uma API RESTful. O objetivo é implementar e documentar a API de envio de e-mails e criar testes unitários para as rotas. Você pode escolher entre Node.js ou Python para a implementação, conforme sua preferência.

## Tarefas

1. **Configuração Inicial**
   - Configure um projeto Node.js utilizando Express.js ou um projeto Python utilizando Flask.
   - Crie uma estrutura básica de pastas para o projeto, incluindo `routes`, `controllers`, e `services`.

2. **Criação da API de Envio de E-mails**
   - Implemente uma rota POST `/send-email` que receba os seguintes dados no corpo da requisição:
     ```json
     {
       "to": "destinatario@example.com",
       "subject": "Assunto do E-mail",
       "body": "Conteúdo do E-mail"
     }
     ```
   - Utilize um serviço de envio de e-mails de sua escolha (por exemplo, Nodemailer, smtplib, ou qualquer outro). Documente claramente como configurar e utilizar o serviço escolhido.

3. **Documentação da API**
   - Crie uma documentação simples utilizando Swagger ou outra ferramenta de documentação para descrever a rota `/send-email`.

4. **Testes**
   - Implemente testes unitários para a rota criada utilizando uma biblioteca de testes como Jest (para Node.js) ou unittest/pytest (para Python).

## Configuração da Conta de E-mail

Para o envio de e-mails, você pode utilizar qualquer serviço de e-mail de sua escolha (por exemplo, Mailtrap, Gmail, etc.). Certifique-se de documentar claramente como configurar o serviço escolhido.

### Nota

Lembre-se de não expor credenciais sensíveis em seu código. Utilize variáveis de ambiente para configurá-las.

## Critérios de Avaliação

- **Funcionalidade**: O microserviço deve ser capaz de enviar e-mails corretamente.
- **Qualidade do Código**: O código deve ser bem estruturado, organizado e seguir boas práticas de desenvolvimento.
- **Documentação**: A API deve estar bem documentada e fácil de entender.
- **Testes**: A implementação de testes unitários é essencial para validar a robustez da aplicação.

## Recursos Disponíveis

- Documentação do Nodemailer: [Nodemailer](https://nodemailer.com/about/).
- Documentação do smtplib: [smtplib](https://docs.python.org/3/library/smtplib.html).

## Entrega

- Envie o link para o repositório do GitHub contendo o código-fonte do projeto.
- A entrega deve incluir instruções claras de como rodar a aplicação localmente.

Boa sorte! Estamos ansiosos para ver como você resolverá este desafio e demonstrará suas habilidades.
