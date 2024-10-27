import { Link } from "react-router-dom";

function Sobre(){
    return(
        <div>
            <h1>Bem-Vindo à Pagina SOBRE</h1>

            <Link to='/'>Home</Link>
            <Link to='/contato'>Contato</Link>
            <Link to='/produto'>Produto</Link>
        </div>
    );
}

export default Sobre;