# O que é a Clean Architecture (Arquitetura Limpa)

The clean architecture proposed by Robert C. Martin in 2012 combines the principles of the hexagonal architecture,
the onion architecture and several other variants. It provides additional levels of detail of the component,
which are presented as concentric rings.

- Created by Bob Martin in 2012
- Aims to create loosely coupled, easy to test and replaceable software components
- It is domain logic centric instead of data/db centric
- It is a layered approach
- Each layer has specific responsibilities
- Dependencies always point inwards towards to the domain
- Encapsulates the business logic but keeps it separate from the delivery mechanism

# Visão geral da arquitetura do Django e do Flask
# MTV / MVC

![](images/rest.png)

- Simples
- Suficiente para 90% dos casos
- Insuficiente para situações em que a lógica de negócio precisa ser reutilizada em outras aplicações de outros frameworks.

# Quando utilizar Clean Architecture

- Projetos grandes com múltiplos módulos e diferentes times trabalhando ao mesmo tempo no código fonte.
- Não ter acoplamento com um framework específico
- Poder ser reutilizada independentemente da tecnologia
- Estabelecer um padrão de projeto que todos conhecem ou podem ser treinados
- Diminuir acoplamento entre os módulos do sistema
- Aumentar a coesão entre módulos
- Aumenta a coesão entre módulos
- Aumentar a testabilidade do código através de UNIT TESTS
- Proteger as regras de negócio de frameworks

# Quando NÃO utilizar Clean Architecture

- Quando você não precisar de Clean Architecture
- Projetos muito pequenos e simples
- Quando o trade off de velocidade e complexidade não fizer sentido.

# Considerações antes de aplicar as técnicas deste cursos

- Django, Flask, FastAPI não foi feito/pensado para ser utilizado dessa forma, esse curso é uma proposta de adaptação da Clean Architecture a esses frameworks.
- Estamos adicionando complexidade no projeto (Complexidade que trará ótimos resultados.)
- Você precisará saver mais do que Djanfo quando estiver trabalhando no código.
- Django e Flask agora são só um detalhe da sua arquitetura.
- Nem todos os recursos do framework poderão ser utilizados.
- Migrando um projeto existente para Clean Architecture.

# Domain Driven Design

Domain Driven Design é uma abordagem de desenvolvimento de software que visa modelar aplicações de forma compatível com as caracteristicas do domínio/problema no qual o software se propõe a resolver.

- Bounded Context
- Ubiquitous Language
- Aggregates
- Value Objects
- DTOs
- Domain Exceptions

# Considerações Finais

- TDD
- Inversão de controle através de Injeção de dependências.
