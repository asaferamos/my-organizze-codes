# My Organizze Codes

Repositório de códigos úteis para usuários do app [Organizze](https://organizze.com.br).
Utilizando a [Api pública oficial](https://github.com/organizze/api-doc).

### Config
Copie o arquivo `config-sample.py` para `config.py` e insira email e token do Organizze gerado em: https://app.organizze.com.br/configuracoes/api-keys

### Funções
#### 1 Excluíndo movimentações recorrentes em dias específicos da semana
##### 1.1 Fim de Semana

`python excludes_daily_weekends.py YEAR 'TRANSACTION NAME'`

