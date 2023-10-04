function validarSenha() {
    var senha = document.getElementById('senha').value;
    var confirmarSenha = document.getElementById('confirmar_senha').value;
    var senhaErro = document.getElementById('senha-erro');

    if (senha === confirmarSenha) {
        senhaErro.textContent = ''; // Limpa a mensagem de erro
        return true; // Senhas coincidem
    } else {
        senhaErro.textContent = 'As senhas não coincidem.';
        return false; // Senhas não coincidem
    }
}
