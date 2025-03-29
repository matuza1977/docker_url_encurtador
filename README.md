# Projeto Docker Demo

Este é um projeto simples demonstrando o uso do Docker com uma aplicação Flask.

## Estrutura do Projeto

```
docker_demo/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Como Executar

1. Certifique-se de ter o Docker e o Docker Compose instalados
2. Na pasta do projeto, execute:
   ```bash
   docker-compose up --build
   ```
3. Acesse a aplicação em: http://localhost:5000

## Comandos Úteis

- Para iniciar os containers:
  ```bash
  docker-compose up
  ```

- Para parar os containers:
  ```bash
  docker-compose down
  ```

- Para reconstruir os containers:
  ```bash
  docker-compose up --build
  ```

  ![image](https://github.com/user-attachments/assets/265f05d7-8ab1-4c14-9eeb-8049398b9235)

  ![image](https://github.com/user-attachments/assets/11973464-3dec-4278-86ab-4323d1ca5c20)

