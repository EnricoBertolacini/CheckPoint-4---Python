const API_URL = "http://127.0.0.1:8000";

const listaLivros = document.querySelector("#listaLivros");
const listaClientes = document.querySelector("#listaClientes");

const formLivro = document.querySelector("#formLivro");
const formCliente = document.querySelector("#formCliente");

/* LISTAR LIVROS */
async function listarLivros() {

    const resposta = await fetch(`${API_URL}/livros`);

    const livros = await resposta.json();

    listaLivros.innerHTML = "";

    livros.forEach((livro) => {

        listaLivros.innerHTML += `
            <div class="item-lista">

                <p>
                    <strong>ID:</strong>
                    ${livro.id}
                </p>

                <p>
                    <strong>Nome:</strong>
                    ${livro.nome}
                </p>

                <p>
                    <strong>Preço:</strong>
                    R$ ${Number(livro.preco).toFixed(2)}
                </p>

                <div class="acoes">

                    <button
                        class="btn btn-edit"
                        onclick="editarLivro(${livro.id})"
                    >
                        Editar
                    </button>

                    <button
                        class="btn btn-delete"
                        onclick="excluirLivro(${livro.id})"
                    >
                        Excluir
                    </button>

                </div>

            </div>
        `;
    });
}


/* LISTAR CLIENTES */
async function listarClientes() {

    const resposta = await fetch(`${API_URL}/clientes`);

    const clientes = await resposta.json();

    listaClientes.innerHTML = "";

    clientes.forEach((cliente) => {

        listaClientes.innerHTML += `
            <div class="item-lista">

                <p>
                    <strong>ID:</strong>
                    ${cliente.id}
                </p>

                <p>
                    <strong>Nome:</strong>
                    ${cliente.nome}
                </p>

                <p>
                    <strong>E-mail:</strong>
                    ${cliente.email}
                </p>

                <div class="acoes">

                    <button
                        class="btn btn-edit"
                        onclick="editarCliente(${cliente.id})"
                    >
                        Editar
                    </button>

                    <button
                        class="btn btn-delete"
                        onclick="excluirCliente(${cliente.id})"
                    >
                        Excluir
                    </button>

                </div>

            </div>
        `;
    });
}


/* BUSCAR LIVRO POR ID */
async function buscarLivroPorId() {

    const id = document.querySelector("#idLivro").value;

    if (!id) {
        alert("Digite o ID do livro.");
        return;
    }

    const resposta = await fetch(`${API_URL}/livros/${id}`);

    if (!resposta.ok) {
        alert("Livro não encontrado.");
        return;
    }

    const livro = await resposta.json();

    listaLivros.innerHTML = `
        <div class="item-lista">

            <p>
                <strong>ID:</strong>
                ${livro.id}
            </p>

            <p>
                <strong>Nome:</strong>
                ${livro.nome}
            </p>

            <p>
                <strong>Preço:</strong>
                R$ ${Number(livro.preco).toFixed(2)}
            </p>

            <div class="acoes">

                <button
                    class="btn btn-edit"
                    onclick="editarLivro(${livro.id})"
                >
                    Editar
                </button>

                <button
                    class="btn btn-delete"
                    onclick="excluirLivro(${livro.id})"
                >
                    Excluir
                </button>

            </div>

        </div>
    `;
}


/* BUSCAR CLIENTE POR ID */
async function buscarClientePorId() {

    const id = document.querySelector("#idCliente").value;

    if (!id) {
        alert("Digite o ID do cliente.");
        return;
    }

    const resposta = await fetch(`${API_URL}/clientes/${id}`);

    if (!resposta.ok) {
        alert("Cliente não encontrado.");
        return;
    }

    const cliente = await resposta.json();

    listaClientes.innerHTML = `
        <div class="item-lista">

            <p>
                <strong>ID:</strong>
                ${cliente.id}
            </p>

            <p>
                <strong>Nome:</strong>
                ${cliente.nome}
            </p>

            <p>
                <strong>E-mail:</strong>
                ${cliente.email}
            </p>

            <div class="acoes">

                <button
                    class="btn btn-edit"
                    onclick="editarCliente(${cliente.id})"
                >
                    Editar
                </button>

                <button
                    class="btn btn-delete"
                    onclick="excluirCliente(${cliente.id})"
                >
                    Excluir
                </button>

            </div>

        </div>
    `;
}


/* CADASTRAR LIVRO */
formLivro.addEventListener("submit", async (event) => {

    event.preventDefault();

    const nome = document.querySelector("#nomeLivro").value;

    const preco = document.querySelector("#precoLivro").value;

    const livro = {
        nome: nome,
        preco: Number(preco)
    };

    await fetch(`${API_URL}/livros`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(livro)

    });

    formLivro.reset();

    listarLivros();
});


/* CADASTRAR CLIENTE */
formCliente.addEventListener("submit", async (event) => {

    event.preventDefault();

    const nome = document.querySelector("#nomeCliente").value;

    const email = document.querySelector("#emailCliente").value;

    const cliente = {
        nome: nome,
        email: email
    };

    await fetch(`${API_URL}/clientes`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(cliente)

    });

    formCliente.reset();

    listarClientes();
});


/* EDITAR LIVRO */
async function editarLivro(id) {

    const novoNome = prompt(
        "Digite o novo nome do livro:"
    );

    if (novoNome === null) {
        return;
    }

    const novoPreco = prompt(
        "Digite o novo preço do livro:"
    );

    if (novoPreco === null) {
        return;
    }

    const livroAtualizado = {
        nome: novoNome,
        preco: Number(novoPreco)
    };

    await fetch(`${API_URL}/livros/${id}`, {

        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(livroAtualizado)

    });

    listarLivros();
}


/* EDITAR CLIENTE */
async function editarCliente(id) {

    const novoNome = prompt(
        "Digite o novo nome do cliente:"
    );

    if (novoNome === null) {
        return;
    }

    const novoEmail = prompt(
        "Digite o novo e-mail do cliente:"
    );

    if (novoEmail === null) {
        return;
    }

    const clienteAtualizado = {
        nome: novoNome,
        email: novoEmail
    };

    await fetch(`${API_URL}/clientes/${id}`, {

        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(clienteAtualizado)

    });

    listarClientes();
}


/* EXCLUIR LIVRO */
async function excluirLivro(id) {

    await fetch(`${API_URL}/livros/${id}`, {
        method: "DELETE"
    });

    listarLivros();
}


/* EXCLUIR CLIENTE */
async function excluirCliente(id) {

    await fetch(`${API_URL}/clientes/${id}`, {
        method: "DELETE"
    });

    listarClientes();
}


/* CARREGAR DADOS */
listarLivros();

listarClientes();
