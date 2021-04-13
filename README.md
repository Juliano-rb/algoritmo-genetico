# Otimização de antena para padrão de radiação

Esta é minha submissão para a atividade https://github.com/aydanomachado/mlclass/tree/master/02_Optimization

Utilizei um algoritmo genético para a busca dos angulos para a construção de uma antena para a espaçonave ST5 da NASA. Na atividade foi utilizada uma simplificação do problema original.

Para testar a execução, execute o programa que simula o ambiente real ([OPServer.jar](simulation_environment/OPServer.jar)) com o comando:
```
java -jar OPServer.jar
```
Após isso, você pode iniciar o algoritmo genético rodando:
```
python3 algoritmo_genetico
```

# Avisos
O software que simula o ambiente real encontrado no diretório ``simulation environment`` foi criado pelo professor Aydano Machado (https://github.com/aydanomachado). O arquivo original pode ser encontrado no repositório https://github.com/aydanomachado/mlclass/tree/master/02_Optimization. Tomei a liberdade de fazer uma cópia para facilitar a execução do algoritmo.