import { Link } from "react-router-dom";

import Livro from '../../assets/livro.jpg';

function Produto(){
    return(
        <div>
            <h1>Bem-Vindo à Pagina PRODUTO</h1>
            <img src={Livro} className="img" alt="livro"/>
            <Link to='/'>Home</Link>
            <Link to='/sobre'>Sobre</Link>
            <Link to='/contato'>Contato</Link>
        </div>
    );
}

export default Produto;