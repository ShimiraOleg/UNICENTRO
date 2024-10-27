import { Link } from "react-router-dom";

function Home(){
    return(
        <div>
            <h1>ERRO! Página Inválida</h1>

            <Link to='/sobre'>Sobre</Link>
            <Link to='/contato'>Contato</Link>
            <Link to='/produto'>Produto</Link>
        </div>
    );
}

export default Home;