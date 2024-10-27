import { Link } from "react-router-dom";

function Contato(){
    return(
        <div>
            <h1>Bem-Vindo à Pagina CONTATO</h1>

            <Link to='/'>Home</Link>
            <Link to='/sobre'>Sobre</Link>
            <Link to='/produto'>Produto</Link>
        </div>
    );
}

export default Contato;